from django.urls import path, include
from . import views
from .views import BooksViewset
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'bookall', BooksViewset)

# Class Diagram
# Database schemas
# Code 
# documents
# front
# API
# Design 

urlpatterns = [
    path("", views.get),
    path("add/", views.addBook),
    path("hello/", views.hello),
    path("books/", views.booksView),
    path('registerauthor/', views.RegisterView.as_view()),
    # or include("viewset/", router)

    
]

# urlpatterns = router.urls

