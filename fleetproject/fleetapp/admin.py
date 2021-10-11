from django.contrib import admin

# Register your models here.

from .models import Book, Library, LibraryBooks, LibraryActivity

all_models = (Book, Library, LibraryBooks, LibraryActivity)

[admin.site.register(i) for i in all_models]
