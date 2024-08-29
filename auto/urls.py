from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),

    # Brend uchun
    path('create-brand/', views.CreateBrandView.as_view(), name='create_brand'),
    path('update-brand/<int:id>/', views.UpdateBrandView.as_view(), name='update_brand'),
    path('delete-brand/<int:id>/', views.DeleteBrandView.as_view(), name='delete_brand'),

    # Color uchun
    path('create-color/', views.CreateColorView.as_view(), name='create_color'),
    path('update-color/<int:id>/', views.UpdateColorView.as_view(), name='update_color'),
    path('delete-color/<int:id>/', views.DeleteColorView.as_view(), name='delete_color'),

    # Cars
    path('create-car/', views.CreateCarView.as_view(), name='create_car'),
    path('update-car/<int:id>/', views.UpdateCarView.as_view(), name='update_car'),
    path('delete-car/<int:id>/', views.DeleteCarView.as_view(), name='delete_car'),
]