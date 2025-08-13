from django.shortcuts import render
from .models import Post

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/home.html', {'posts': posts})

####### AUTHENTICATION #######

class UserLoginView(LoginView):
    template_name = 'registration/login.html'  # we’ll create this
    # optional: redirect authenticated users away from login
    redirect_authenticated_user = True

class UserLogoutView(LogoutView):
    template_name = 'registration/logout.html'  # display a simple "you logged out"

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # password hashing handled by UserCreationForm
            login(request, user) # auto-login after registration
            messages.success(request, "Account created successfully. Welcome!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # If you skipped Profile model, remove p_form & avatar handling
        p_form = ProfileUpdateForm(
            request.POST, request.FILES,
            instance=getattr(request.user, 'profile', None)
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('profile')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=getattr(request.user, 'profile', None))
    return render(request, 'registration/profile.html', {'u_form': u_form, 'p_form': p_form})

# --- Post detail (from earlier step, if you added it) ---

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

