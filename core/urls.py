"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('search/', search),
    path('test-graph/', test_graph),
    path('debug-data/', debug_data),
    path('test-data-structure/', test_data_structure),
    path('test-dashboard/', test_dashboard),
    path('test-specific-tickers/', test_specific_tickers),
    path('debug-ticker-data/', debug_ticker_data),
    path('predict/<str:ticker_value>/<str:number_of_days>/', predict),
    path('ticker/', ticker),
    path('recent-stocks/', recent_stocks_all),
]