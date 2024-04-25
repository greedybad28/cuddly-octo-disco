from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def print_hello(request):
    movie_data = {"movies" :[{
        "title" : "Manjumal boys",
        'year' : 2055,
        "summary" : "story of kona kave",
        "success" : True
    },
    {
        "title" : "frends njan kong",
        "year" : 2023,
        "summary" : "kong oru killadi thenne",
        "success" : False
    }
    ]}
    
    return render(request,"index.html",movie_data)
