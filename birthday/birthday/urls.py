"""birthday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from hbd import views

urlpatterns = [
    path('', views.user_login, name="user_login"),
    path('invalid',views.invalid_page, name = "invaliddetails"),
    path('page1',views.page1,name="page1"),
    path('page2',views.page2,name="page2"),
    path('page3',views.page3,name="page3"),
    path('page4',views.page4,name="page4"),
    path('page5',views.page5,name="page5"),
    path('page6',views.page6,name="page6"),
    path('HappyBirthdayShritama',views.page7,name="page7"),
    path('admin/', admin.site.urls),
]
