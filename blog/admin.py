from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from loginsystem.forms import SignupForm
from .models import *


# Register User Model
@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    add_form = SignupForm
    fieldsets = (*UserAdmin.fieldsets,('user roll',{'fields':('image',)}))


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title','show_contant','user')

    def show_contant(self,obj):
        return obj.contant[:50]

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user','post','comment')
