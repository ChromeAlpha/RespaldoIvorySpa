from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff 
    def handle_no_permission(self):
        from django.shortcuts import redirect
        return redirect("login")


class ProductListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Product
    template_name = "accounts/product_list.html"   # <- antes era products/product_list.html
    context_object_name = "products"
    paginate_by = 10

class ProductCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Product
    fields = ["name", "description", "price", "image", "stock"]
    template_name = "accounts/product_form.html"
    success_url = reverse_lazy("products:manage")

class ProductUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Product
    fields = ["name", "description", "price", "image", "stock"]
    template_name = "accounts/product_form.html"
    success_url = reverse_lazy("products:manage")

class ProductDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Product
    template_name = "accounts/product_confirm_delete.html"
    success_url = reverse_lazy("products:manage")
