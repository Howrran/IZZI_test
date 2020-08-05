"""
Admin
"""
import os

from django.contrib import admin, messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.urls import path

from .models import User
from user_service.models import UserService

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    FILEPATH = 'media/users.csv'
    list_display = ('name', 'surname', 'birthday', 'registration_date')
    ordering = ('name',)
    change_list_template = 'admin/user/change_form.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('add_users', self.add_users)
        ]

        return custom_urls + urls

    def add_users(self, request):
        users = request.FILES.get('users')

        if not users:
            messages.warning(request, 'NO FILE')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        if users.name.split('.')[-1] != 'csv':
            messages.warning(request, 'WRONG TYPE')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        fs = FileSystemStorage()
        if os.path.exists('media/users.csv'):
            os.remove('media/users.csv')
        fs.save('users.csv', users)  # use users.name if u want to save file origin name

        UserService.add_users_from_csv(UserAdmin.FILEPATH)
        messages.info(request, 'Users Added')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
