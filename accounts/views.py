from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Vista de registro
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = False
        user.is_superuser = False
        user.save()
        return super().form_valid(form)

# Vista de login
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

# Vista protegida para usuarios autenticados
@login_required
def home_view(request):
    return render(request, 'accounts/home.html')

# Vista para gestionar usuarios (solo administradores)
@staff_member_required
def gestionar_usuarios(request):
    usuarios = User.objects.all()
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        user.is_staff = True
        user.save()
        messages.success(request, f"El usuario '{user.username}' ahora es administrador.")
        return redirect('gestionar_usuarios')
    return render(request, 'accounts/gestionar_usuarios.html', {'usuarios': usuarios})
