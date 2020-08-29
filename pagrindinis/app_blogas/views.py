from django.shortcuts import render, get_object_or_404
from .models import Field
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q

from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,CreateView,DeleteView,UpdateView


# Create your views here.
class BlogListView(generic.ListView):
     model = Field
     template_name = 'index.html'
     paginate_by = 3

class BlogDetailView(generic.DetailView):
     model = Field
     template_name = 'comment.html'


class BlogsByUserListView(LoginRequiredMixin, generic.ListView):
    model=Field
    template_name = 'user_blogs.html'
    paginate_by = 10

    def get_queryset(self):
        return Field.objects.filter(author=self.request.user)


class BlogsByUserCreateView(LoginRequiredMixin, CreateView):
    model = Field
    fields = ['title','text']
    success_url = "/blog/myblog/"
    template_name = 'user_blog_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)






@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


#
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)

