"""
Add user from csv on admin page
"""
import os

from django.contrib import admin, messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.urls import path

from user_service.models import UserService
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Custom user admin page
    """
    FILEPATH = 'media/users.csv'  # path where file with users is stored
    list_display = ('name', 'surname', 'birthday', 'registration_date')
    ordering = ('name',)
    change_list_template = 'admin/user/change_form.html'

    def get_urls(self):
        """
        Url for custom user model

        :return: str
        """
        urls = super().get_urls()
        custom_urls = [
            path('add_users', self.add_users)
        ]

        return custom_urls + urls

    # pylint: disable=no-self-use
    def add_users(self, request):
        """
        Save uploaded file and add users from it

        :param request:
        :return: Http response
        """
        users = request.FILES.get('users')  # get file from request

        if not users:
            messages.warning(request, 'NO FILE')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        if users.name.split('.')[-1] != 'csv':
            messages.warning(request, 'WRONG TYPE')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        file_system = FileSystemStorage()

        if os.path.exists('media/users.csv'):  # if such file already exist
            os.remove('media/users.csv')
        file_system.save('users.csv', users)  # use users.name if u want to save file origin name

        UserService.add_users_from_csv(UserAdmin.FILEPATH)
        messages.info(request, 'Users Added')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
