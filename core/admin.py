from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin 
from .models import *
import nested_admin



class ProfileInline(nested_admin.NestedStackedInline):
    model = Profile

class PostImageInline(nested_admin.NestedTabularInline):
    model = Image
    extra = 1
    
class PostInline(nested_admin.NestedStackedInline):
    model = Post
    inlines = [PostImageInline]
    extra = 1


class CustomUserAdmin(UserAdmin, nested_admin.NestedModelAdmin):
    fieldsets = (
        (None, {'fields': ('username',)}),  # Only include the 'username' field
    )
    inlines = [ProfileInline, PostInline]


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Comment)

# admin.site.register(Post)


