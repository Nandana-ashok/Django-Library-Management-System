"""
URL configuration for librarymanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from book_app.views import welcome_response,library_info,book_list,book_details,contact_info
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',welcome_response ,name='hello'),
    path('library/',library_info,name='library'),
    path('books/',book_list,name='books'),
    path('book/',book_details,name='book'),
    path('contact/',contact_info,name='contact'),
]
