from django.urls import path
from .views import (
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
)

app_name = "products"

urlpatterns = [
    path("manage/", ProductListView.as_view(), name="manage"),
    path("create/", ProductCreateView.as_view(), name="create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="delete"),
]

