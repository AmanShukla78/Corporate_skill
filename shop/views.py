from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

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