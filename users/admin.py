from django.contrib import admin

from users.models import Class, User

class UserAdmin(admin.ModelAdmin):

    list_display = ("name", "email")

admin.site.register(User, UserAdmin)

class ClassAdmin(admin.ModelAdmin):

    list_display = ("name",)

admin.site.register(Class, ClassAdmin)