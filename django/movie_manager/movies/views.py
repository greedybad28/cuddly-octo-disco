from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request,'create.html')

def edit(request):
    return render(request,'edit.html')

def list(request):
    return render(request,'list.html',movies)

def blanklayout(request):
    return render(request,"blank_layout.html")


movies ={"movies" :  [
    {
        "title": "Titanic",
        "summary": "A young couple's love story is set against the backdrop of the Titanic's ill-fated maiden voyage.",
        "release_year": 1997
    },
    {
        "title": "Avatar",
        "summary": "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        "release_year": 2009
    },
    {
        "title": "Forrest Gump",
        "summary": "The story of a man with a low IQ who rose above his challenges, and proved that determination, courage, and love can change the world.",
        "release_year": 1994
    },
    {
        "title": "Jurassic Park",
        "summary": "During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok.",
        "release_year": 1993
    },
    {
        "title": "The Matrix",
        "summary": "A computer hacker learns about the true nature of reality and his role in the war against its controllers.",
        "release_year": 1999
    }

]
}

