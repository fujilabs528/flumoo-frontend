from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("health-index/", views.health_index,
         name="health_index"),
    path("health-index-share/", views.health_index_share,
         name="health_index_share"),
    path("home-this-week/", views.home2, name= "home2"),
    path("search-results/",views.search_results,name="search_results"),
    path("about/",views.about,name="about"),
    path("about-share/",views.about_share,name="about_share"),
    path("blog/",views.blog,name="blog"),
    path("home-share/",views.home_share,name="home_share"),
    path("do-not-buy/",views.do_not_buy,name="do_not_buy"),
    path("do-not-buy2/",views.do_not_buy2,name="do_not_buy2"),
    path("do-not-buy-share/",views.do_not_buy_share,name="do_not_buy_share"),
    path("outliers/", views.outliers,name="outliers"),
    path("outliers-share/", views.outliers_share,name="outliers_share"),
    path("eps/", views.eps,name="eps"),
    path("averagevolume/", views.averagevolume, name="averagevolume"),
    path("marketcap/", views.marketcap, name="marketcap"),
    path("assets/", views.assets, name="assets"),
    path("liabilities/", views.liabilities, name="liabilities"),
    path("equity/", views.equity, name="equity"),
    path("revenue/", views.revenue, name="revenue"),
    path("grossprofit/", views.grossprofit, name="grossprofit"),
    path("opincome/", views.opincome, name="opincome"),
    path("netincome/", views.netincome, name="netincome"),
    path("opcash/", views.opcash, name="opcash"),
    path("ficash/", views.ficash, name="ficash"),
    path("invcash/", views.invcash, name="invcash"),
    path("endcash/", views.endcash, name="endcash"),
    path("behind/", views.behind, name="behind"),
    path("dom/", views.dom, name="dom"),
    path("health/", views.health, name="health"),
    path("orglean/", views.orglean, name="orglean"),
    path("top2bot/", views.top2bot, name="top2bot"),




    ]



