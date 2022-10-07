from django.urls import path
from .views import ProductFeaturedListView,ProductListView, ProductDetailSlugView
app_name = "products"

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
    path('destaque', ProductFeaturedListView.as_view(), name='destaque'),
]
