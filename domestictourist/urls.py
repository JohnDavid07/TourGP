"""domestictourist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from tourguideportal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexview),
    path('delhi',views.delhiview),
    path('vizag',views.vizagview),
    path('hyderabad',views.hyderabadview),
    path('goa',views.goaview),
    path('kolkata',views.kolkataview),
    path('chennai',views.chennaiview),
    path('about',views.aboutview),
    path('contact',views.contactview),
    path('beachroad',views.beachroadview),
    path('moreplaces',views.moreplacesview),
    path('kailasagiri',views.kailasagiriview),
    path('araku',views.arakuview),
    path('mumbai',views.mumbaiview),
    path('rushikonda',views.rushikondaview),
    path('harbour',views.harbourview),
    path('vparks',views.vparksview),
    path('vhotels',views.vhotelsview),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout',views.logout_view),
    path('signup/', views.signup_view),
    path('bangalore', views.bangaloreview),
]


