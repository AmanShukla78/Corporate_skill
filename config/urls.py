# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from shop.views import *
from django.urls import re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'), name='home'),
    path('inner',TemplateView.as_view(template_name='inner.html'), name='inner'),
    path('about',TemplateView.as_view(template_name='about.html'), name='about'),
    path('chat',TemplateView.as_view(template_name='chat.html'), name='chat'),
    path('terms',TemplateView.as_view(template_name='terms.html'), name='terms'),
    path('FAQ',TemplateView.as_view(template_name='FAQ.html'), name='FAQ'),

    re_path(r'', include('django_private_chat2.urls', namespace='django_private_chat2')),

    path('person_view',TemplateView.as_view(template_name='person_view.html'), name='person_view'),
    path('login',login_view, name='login'),
    path('logout',logout_view, name='logout'),
    path('register',register_view, name='register'),
    path('contact', contact_view, name='contact'),
    path('profile', profile_view, name='profile'),
    path('profile/create', profile_update_view, name='profile_update'),
    path('profile/edit', profile_edit_view, name='profile_edit'),
    
    path('people/list', people_list_view, name='people_list'),
    path('person/<int:id>/view', person_view, name='person_view'),
    path('person/<int:id>/invite', person_invite, name='invite_person'),
    # all invites
    path('invites', invites_list_view, name='invites_list'),
    path('skill/partner', skill_partner_view, name='skill_partner'),
    # accept
    path('invite/<int:id>/accept', invite_accept, name='invite_accept'),
    # reject
    path('invite/<int:id>/reject', invite_reject, name='invite_reject'),
    # cancel
    path('invite/<int:id>/cancel', invite_cancel, name='invite_cancel'),
    path('person/<int:id>/chat', person_chat_view, name='person_chat'),
    path('person/<int:id>/video', person_video_view, name='person_call'),
    path('person/<int:id>/report', person_report_view, name='person_report'),

    path('person/<int:id>/delete', person_delete, name='person_delete'),
    # send message using htmx api
    path('send/message', send_message, name='send_message'),
    # get_messages
    path('get/messages', get_messages, name='get_messages'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    