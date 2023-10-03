from django.urls import path 
from . import views

# Definisi Namespace
app_name = 'main'

# Kumpulan route ke views.p
urlpatterns = [
    path('', views.items, name = 'items'),
    path('books/', views.book_views, name = 'books'),
    path('added-books/', views.added_books, name='added-books'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<int:id>/', views.xml_by_id, name='xml_by_id'),
    path('json/<int:id>/', views.json_by_id, name='json_by_id'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add-stock/<int:item_id>/', views.add_stock, name='add-stock'),
    path('reduce-stock/<int:item_id>/', views.reduce_stock, name='reduce-stock'),
    path('edit-books/<int:item_id>/', views.edit_books, name='edit-books'),
    path('delete-item/<int:item_id>/', views.delete_item, name='delete-item'),
]