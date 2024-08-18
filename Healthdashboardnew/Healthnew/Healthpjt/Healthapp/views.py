from django.shortcuts import render, redirect
from collections import defaultdict
from .models import diseasestreemap
from .models import Disease
from .models import Servicenew
from .models import Subservice
from .models import Subservicenew
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User


def index(request):
    return render(request, "index.html")


##for main-treemap
def treemap_view(request):
    diseases = diseasestreemap.objects.all()
    data = {"name": "root", "children": []}
    category_map = defaultdict(lambda: {"name": "", "children": []})
    for disease in diseases:
        category_map[disease.Disease_Type]["name"] = disease.Disease_Type
        category_map[disease.Disease_Type]["children"].append({"name": disease.Disease_Name, "value": disease.DALYRate})
    data["children"] = list(category_map.values())
    return render(request, 'maintreemap.html',{'data': data})


##for service treemap
def disease_treemap(request, disease_name):
    disease = get_object_or_404(Disease, name=disease_name)
    services = Servicenew.objects.filter(disease=disease)
    service_dict = {}
    for service in services:
        service_name = service.servicename
        if service_name not in service_dict:
            service_dict[service_name] = []
        service_dict[service_name].append({"name": service.subservice, "value": service.value})
    # Prepare the data for D3.js
    disease_data = {
        "name": disease.name,
        "children": [{"name": service, "children": subservices} for service, subservices in service_dict.items()]
    }
    # Return the JSON response directly
    context = {'disease_data': disease_data}
    return render(request, 'servicefdisease_treemap.html', context)

##for subservice treemap

def subservice_view(request,subservice_name):
    # Fetch data from your database
    subservice = get_object_or_404(Subservice, name=subservice_name)
    resources = Subservicenew.objects.filter(subservice=subservice)
    treemap_data = {
        "name": "Health Promotion",
        "children": defaultdict(list)
    }
    # Organize data by direct input
    for resource in resources:
        direct_input = resource.directinpts
        treemap_data["children"][direct_input].append({
            "name": resource.resources,
            "value": resource.value
        })
    # Convert defaultdict to a list
    treemap_data["children"] = [{"name": direct_input, "children": resources} for direct_input, resources in
                                treemap_data["children"].items()]
    return render(request, 'subservice.html', {'treemap_data': treemap_data})

def barchart(request):
    # Example data (replace with your actual data)
    data = {
        'categories': ['Item 1', 'Item 2', 'Item 3'],
        'items': ['SOCIO-ECONOMIC STATUS', 'GENDER', 'LOCATION'],
        'heights': [[3, 5, 2], [4, 2, 6], [1, 7, 3]],
    }
    return render(request, 'barchart.html',{'data': data})


def guagechart(request):
    return render(request, "speedometer_chart.html")

# views.py

from django.shortcuts import render

def gauge_chart(request):
    # Your data here - this should be the data you want to display in the chart
    data = {
        'value': 65,  # Example data
        'min': 0,
        'max': 100,
    }
    return render(request, 'speedometer_chart.html', {'data': data})


import json

def my_view(request):
    data = [
    {"label": "Access", "icon": "path/to/access-icon.svg", "color": "#8E44AD"},
    {"label": "Quality", "icon": "path/to/quality-icon.svg", "color": "#9B59B6"},
    {"label": "Justice", "icon": "path/to/justice-icon.svg", "color": "#3498DB"},
    {"label": "Efficiency", "icon": "path/to/efficiency-icon.svg", "color": "#2ECC71"},
    {"label": "Sustainability", "icon": "path/to/sustainability-icon.svg", "color": "#1ABC9C"}
]
    return render(request, 'my_template.html', {'data': json.dumps(data)})


def his(request):
    return render(request, "his.html")

#def Access(request):
    #return render(request, "Access.html")

def quality(request):
    return render(request, "quality.html")

def justice(request):
    data = {
        'categories': ['Item 1', 'Item 2', 'Item 3'],
        'items': ['SOCIO-ECONOMIC STATUS', 'GENDER', 'LOCATION'],
        'heights': [[3, 5, 2], [4, 2, 6], [1, 7, 3]],
    }
    return render(request, 'justicecheck.html', {'data': data})


def barchart(request):
    # Example data (replace with your actual data)
    data = {
        'categories': ['Item 1', 'Item 2', 'Item 3'],
        'items': ['SOCIO-ECONOMIC STATUS', 'GENDER', 'LOCATION'],
        'heights': [[3, 5, 2], [4, 2, 6], [1, 7, 3]],
    }

    return render(request, 'barchart.html',{'data': data})




def efficiency(request):
    data2 = [20, 40]
    return render(request, "efficiency.html", {'data2': data2})

def button(request):
    return render(request, "button.html")


def frontpage(request):
    return render(request,"frontpage.html")

def login(request):
    if request.method=='POST':
       username=request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username, password=password)
       if user is not None:
          auth.login(request,user)
          return render(request,"index.html")
       else:
           messages.info(request,"invalid credentials")
           return redirect('login')
    return render(request,"login.html")



def register(request):
    if request.method == 'POST':
       username = request.POST['username']
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       email = request.POST['email']
       password = request.POST['password']
       cpassword = request.POST['cpassword']
       if password==cpassword:
          if User.objects.filter(username=username).exists():
             messages.info(request,"Username Taken")
             return redirect('register')
          elif User.objects.filter(email=email).exists():
             messages.info(request, "Email Taken")
             return redirect('register')
          else:
             user=User.objects.create_user(username=username,password=password,first_name =first_name,last_name=last_name,email=email)
             user.save();
          # print("user created")
       else:
             messages.info(request,"password not matching")
             return redirect('register')
       return redirect('login')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return render(request,"index.html")

def barchartnew(request):
    return render(request, "trendchartnew.html")

def hf(request):
    return render(request, "doughnutchart.html")

def sustainability(request):
    data1 = [10, 30]
    data2 = [20, 40]
    line_data = [
        { "label": "item1", "value": 19 },
        { "label": "item2", "value": 25 },
        { "label": "item3", "value": 21 },
        { "label": "item4", "value": 35 },
        { "label": "item5", "value": 37 },
    ]
    return render(request, 'sustainabilitycheck.html', {'data1': data1, 'data2': data2, 'line_data': line_data})

def target(request):
    data2 = [20, 40]
    return render(request, "targetchart.html",{'data2': data2})

def speedometer_chart(request):
    return render(request, "speedometer_chart.html")


def bubble_chart(request):
    return render(request,"bubblechart.html")

def line(request):
    return render(request, "distanceplot.html")


def guagechart(request):
    # Pass data to template
    return render(request, 'guagechartfinal.html')

def progresschart(request):
    # Dummy data (replace with your actual data)
    data = [
        {"label": "Task 1", "progress": 0.7},
        {"label": "Task 2", "progress": 0.4},
        {"label": "Task 3", "progress": 0.9},
    ]
    return render(request, 'progresschart.html', {'data': data})


def access(request):
    data = [
        {"year": 2015, "value": 30},
        {"year": 2016, "value": 27},
        {"year": 2018, "value": 25},
        {"year": 2019, "value": 20},
        {"year": 2020, "value": 18},
        {"year": 2021, "value": 15},
        {"year": 2022, "value": 10},
        {"year": 2023, "value": 6 },
    ]
    target_value = 5
    return render(request, 'Access.html',{'data': data, 'target_value': target_value})

def another_page_view(request):
    return render(request, 'another_page.html')

def quality2(request):
    return render(request, 'quality2.html')

def quality3(request):
    return render(request, 'quality3.html')