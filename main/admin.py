from django.contrib import admin
from .models import Todo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "is_complete", "created")


admin.site.register(Todo, TodoAdmin)
