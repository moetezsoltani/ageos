from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

class MyAdminSite(AdminSite):
    site_header = _("AGEOS Administration")
    site_title = _("AGEOS Admin Portal")
    index_title = _("Welcome to AGEOS Administration")

admin_site = MyAdminSite(name='myadmin')

# Register your models here
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin_site.register(User, UserAdmin)
