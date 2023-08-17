from django.urls import path 
from order import views 

urlpatterns = [
    path('order/',views.orderp, name='order'),
    path('order/<int:giftcard_id>/history/', views.OrderHistoryView.as_view(), name='order-history'),
    
]