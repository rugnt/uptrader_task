from django.contrib import admin

from .models import TreeMenu


class TreeMenuAdmin(admin.ModelAdmin):
    fields = ('name', 'parent')


admin.site.register(TreeMenu, TreeMenuAdmin)

# Register your models here.
