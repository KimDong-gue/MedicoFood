from django.urls import path

from best import views
from best.views import best_product



urlpatterns = [
    path('', best_product, name='best_product'),
    path('product_detail/<int:product_id>/', views.product_detail, name='best_product_detail'),
]