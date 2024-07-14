from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:id>/', views.event_detail, name='event_detail'),
    path('publications/', views.publication_list, name='publication_list'),
    path('publications/<int:id>/', views.publication_detail, name='publication_detail'),
    path('delete/event/<int:id>/', views.event_delete, name='event_delete'),  # Add this line
    path('delete/publication/<int:id>/', views.publication_delete, name='publication_delete'),  # Add this line
    path('formations/', views.formation_list, name='formation_list'),
    path('formations/<int:formation_id>/', views.formation_detail, name='formation_detail'),
]
