from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import TemplateView,ListView

def home(request):
    return render(request, "momma/home.html")

def health_index(request):
    return render(request, "momma/health_index.html")

def health_index_share(request):
    return render(request, "momma/health_index_share.html")

def home2(request):
    return render(request, "momma/home2.html")

def search_results(request):
    return render(request, "momma/search_results.html")

def about(request):
    return render(request,"momma/about.html")

def about_share(request):
    return render(request,"momma/about_share.html")

def blog(request):
    return render(request,"blog/home.html")

def home_share(request):
    return render(request,"momma/home_share.html")

def do_not_buy(request):
    return render(request, "momma/do_not_buy.html")

def do_not_buy2(request):
    return render(request, "momma/do_not_buy2.html")

def do_not_buy_share(request):
    return render(request, "momma/do_not_buy_share.html")

def outliers(request):
    return render(request, "momma/outliers.html")

def outliers_share(request):
    return render(request, "momma/outliers_share.html")

def eps(request):
    return render(request,"momma/xxx1eps.html")

def averagevolume(request):
    return render(request,"momma/xxx2averagevolume.html")

def marketcap(request):
    return render(request,"momma/xxx3marketcap.html")

def assets(request):
    return render(request,"momma/xxx4assets.html")

def liabilities(request):
    return render(request,"momma/xxx5liabilities.html")

def equity(request):
    return render(request,"momma/xxx6equity.html")

def revenue(request):
    return render(request,"momma/xxx7revenue.html")

def grossprofit(request):
    return render(request,"momma/xxx8grossprofit.html")

def opincome(request):
    return render(request,"momma/xxx9opincome.html")

def netincome(request):
    return render(request,"momma/xxx10netincome.html")

def opcash(request):
    return render(request,"momma/xxx11opcash.html")

def ficash(request):
    return render(request,"momma/xxx12ficash.html")

def invcash(request):
    return render(request,"momma/xxx13invcash.html")

def endcash(request):
    return render(request,"momma/xxx14endcash.html")

def behind(request):
    return render(request,"momma/xxx15behind.html")

def dom(request):
    return render(request,"momma/xxx16dom.html")

def health(request):
    return render(request,"momma/xxx18health.html")

def orglean(request):
    return render(request,"momma/xxx19orglean.html")

def top2bot(request):
    return render(request,"momma/xxx20top2bot.html")







#class SearchResultsView(ListView):
#    model= City
#    template_name= "search_result.html"

#    def get_queryset(self):
#        return.City.objects.filter(name__icontains="MMM")

#searh_query = request.GET.get("search":"")
