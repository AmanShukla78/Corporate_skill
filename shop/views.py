from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.
def contact_view(request):
    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if len(name)>0 and len(email)>0 and len(subject)>0 and len(message)>0 :
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()
            messages.success(request, "YOUR message has been sent successfully")
            return redirect('contact')
        else:
            messages.error(request, "Please fill in all the field")
    return render(request, 'contact.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "You are logged in successfully")
                return redirect('profile')
            else:
                messages.error(request, "Invalid username or password")
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You are logged out successfully")
    return redirect('home')
# register
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "account created successfully")
        return redirect('profile')
    return render(request,'accounts/register.html',{'form': form})

@login_required
def profile_view(request):
    profile = Profile.objects.filter(user=request.user).first()
    if not profile:
        return redirect('profile_update')

    return render(request, 'accounts/profile.html', {
        'profile': profile
    })


@login_required
def profile_update_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender =  request.POST.get('gender')
        age = request.POST.get('age')
        photo = request.FILES.get('image')
         
        corporate = request.POST.get('corporate')
        position = request.POST.get('position')
        my_skills = request.POST.get('myskills')
        needed_skills = request.POST.get('nskills')
        free_time = request.POST.get('freetime')
        if name and email:
            profile = Profile(
                name=name, 
                email=email,
                gender = gender,
                age = age,
                image = photo,
                corporate = corporate,
                position = position,
                my_skills = my_skills,
                needed_skills = needed_skills,
                free_time = free_time,
                user = request.user
            )
            profile.save()
            messages.success(request, "Profile created successfully")
            return redirect('profile')
        else:
            messages.error(request, "Please fill in all the fields")
    return render(request, 'accounts/profile_form.html')

@login_required
def profile_edit_view(request):
    profile = Profile.objects.filter(user=request.user).first()
    try:
        form = ProfileForm(instance=profile)
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request,"Profile updated")
                return redirect('profile')
        return render(request, 'accounts/profile_edit.html', {
            'form' : form
        })
    except Exception as e:
        print(e)
        return redirect('/profile')

