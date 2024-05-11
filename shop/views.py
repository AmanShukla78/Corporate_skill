from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
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
        photo = request.FILES.get('photo')
         
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

@login_required
def people_list_view(request):
    # not staff users
    users = User.objects.all().exclude(id=request.user.id).exclude(is_staff=True)
    for user in users:
        # get profile
        user.profile = Profile.objects.filter(user=user).first()
    return render(request, 'people_list.html', {
        'people': users
    })

@login_required
def person_view(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.filter(user=user).first()
    return render(request, 'person_view.html', {
        'profile': profile
    })

@login_required
def person_chat_view(request, id):
    userA = User.objects.get(id=id)
    userB = request.user

    profile = Profile.objects.filter(user=userA).first()
    if not profile:
        messages.error(request, "Profile not found")
        return redirect('people_list')
    
    # get chat messages
    messages = Chat.objects.filter(userA=userA, userB=userB) | Chat.objects.filter(userA=userB, userB=userA)

    return render(request,'chat.html', {
        'userA': userA,
        'userB': userB,
        'messages': messages
    })

@login_required
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        userAId = request.POST.get('userAId')
        userBId = request.POST.get('userBId')
        message = request.POST.get('message')
        userA = User.objects.get(id=userAId)
        userB = User.objects.get(id=userBId)

        chat = Chat(userA=User.objects.get(id=userAId), userB=User.objects.get(id=userBId), message=message, msgby=request.user)
        chat.save()
        # get messages related to users
        messages = Chat.objects.filter(userA=userA, userB=userB) | Chat.objects.filter(userA=userB, userB=userA)
        # json serializable
        messages = list(messages.values())
        userA = userA.username
        userB = userB.username
        return JsonResponse({'message': message, 'userA': userA, 'userB': userB, 'messages': messages})


# get messages
@login_required 
def get_messages(request):
    if request.method == 'GET':
        userAId = request.GET.get('userAId')
        userBId = request.GET.get('userBId')
        userA = User.objects.get(id=userAId)
        userB = User.objects.get(id=userBId)
        messages = Chat.objects.filter(userA=userA, userB=userB) | Chat.objects.filter(userA=userB, userB=userA)
        # make json serializable
        messages = list(messages.values())
        print(len(messages))
        for message in messages:
            message['msgby'] = User.objects.get(id=message['msgby_id']).username
        return JsonResponse({'messages': messages})

from django.core.mail import send_mail

@login_required
def person_video_view(request, id):
    current_user = request.user
    jitsi_url = f'https://meet.jit.si/{current_user.username}-{id}-video'
    send_mail(
        'Video call invitation',
        f'Click here to join the video call {jitsi_url}',
        settings.EMAIL_HOST_USER,
        [User.objects.get(id=id).email],
        fail_silently=False,
    )
    return redirect(jitsi_url)

@login_required
def person_report_view(request, id):
    form = ReportForm(request.POST or None)
    if form.is_valid():
        model = form.save()
        model.userA = request.user
        model.save()
        messages.success(request, "Report sent successfully")
        return redirect('people_list')
    return render(request, 'report_form.html', {
        'form': form
    })

@login_required
def person_invite(request, id):
    # get invites related to user
    send_invites = Invite.objects.filter(userA=request.user)
    receive_invites = Invite.objects.filter(userB=request.user)
    # if user has already invited this user
    if send_invites.filter(userB_id=id).exists():
        messages.error(request, "You have already invited this user")
        return redirect('invites_list')
    # if user has already been invited by this user
    if receive_invites.filter(userA_id=id).exists():
        messages.error(request, "You have already been invited by this user")
        return redirect('invites_list')
    user = User.objects.get(id=id)  
    invite = Invite(userA=request.user, userB=user, invite_status='pending')
    invite.save()
    messages.success(request, "Invite sent successfully")
    return redirect('invites_list')

@login_required
def invites_list_view(request):
    # get invites related to user
    received_invites = Invite.objects.filter(userB=request.user, invite_status='pending')
    for invite in received_invites:
        invite.profile = Profile.objects.filter(user=invite.userA).first()
    sent_invites = Invite.objects.filter(userA=request.user)
    for invite in sent_invites:
        invite.profile = Profile.objects.filter(user=invite.userB).first()
    return render(request, 'invites_list.html', {
        'recieved_invites': received_invites,
        'sent_invites': sent_invites
    })

@login_required
def skill_partner_view(request):
    # people who have accepted your invite
    partnerA = Invite.objects.filter(userA=request.user, invite_status='accepted').exclude(userB=request.user)
    partnerB = Invite.objects.filter(userB=request.user, invite_status='accepted').exclude(userA=request.user)
    for invite in partnerA:
        invite.profile = Profile.objects.filter(user=invite.userB).first()
    for invite in partnerB:
        invite.profile = Profile.objects.filter(user=invite.userA).first()

    all_partners = list(partnerA) + list(partnerB)
    return render(request, 'skill_partner.html', {
        'partners': all_partners
    })


@login_required
def invite_accept(request, id):
    invite = Invite.objects.get(id=id)
    invite.invite_status = 'accepted'
    invite.save()
    messages.success(request, "Invite accepted successfully")
    return redirect('invites_list')

@login_required
def invite_reject(request, id):
    invite = Invite.objects.get(id=id)
    invite.invite_status = 'rejected'
    invite.save()
    messages.success(request, "Invite rejected successfully")
    return redirect('invites_list')

@login_required
def invite_cancel(request, id):
    invite = Invite.objects.get(id=id)
    invite.delete()
    messages.success(request, "Invite cancelled successfully")
    return redirect('invites_list')


@login_required
def person_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.success(request, "Person deleted successfully")
    return redirect('people_list')

