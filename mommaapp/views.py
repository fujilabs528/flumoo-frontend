from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import TemplateView,ListView

def home(request):
    return render(request, "momma/home.html")

def health_index(request):
    return render(request, "momma/health_index.html")

def home2(request):
    return render(request, "momma/home2.html")

def search_results(request):
    return render(request, "momma/search_results.html")

def about(request):
    return render(request,"momma/about.html")

def blog(request):
    return render(request,"blog/home.html")



#class SearchResultsView(ListView):
#    model= City
#    template_name= "search_result.html"

#    def get_queryset(self):
#        return.City.objects.filter(name__icontains="MMM")

#searh_query = request.GET.get("search":"")
