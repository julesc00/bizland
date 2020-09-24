from django.shortcuts import render


def index(request):
    context = {
        "page_title": "From Index Page",
        "title": "BizLand Theme"
    }
    return render(request, "app/index.html", context)
