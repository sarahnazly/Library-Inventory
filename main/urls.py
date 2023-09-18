from django.urls import path 
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.items, name = 'items'),
    path('borrow-books/', views.borrow_books, name='borrow-books'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<int:id>/', views.xml_by_id, name='xml_by_id'),
    path('json/<int:id>/', views.json_by_id, name='json_by_id'),
]