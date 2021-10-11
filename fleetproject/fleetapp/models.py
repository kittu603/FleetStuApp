from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Library(models.Model):
    library_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.library_id} {self.name}"


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    author_name = models.CharField(max_length=15)
    isbn_num = models.CharField("book num", max_length=15)
    genre = models.CharField(max_length=10)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}"


class LibraryActivity(models.Model):

    class ActivityChoices(models.TextChoices):
        BOOK_TAKEN = 'BT', _('BookTaken')
        BOOK_RETURNED = 'BR', _('BookReturned')

    activity_type = models.CharField(
        max_length=2,
        choices=ActivityChoices.choices,
        default=ActivityChoices.BOOK_TAKEN
    )

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    library_book = models.ForeignKey("LibraryBooks", on_delete=models.CASCADE)
    checked_in_at = models.DateTimeField(blank=True)
    checked_out_at = models.DateTimeField(blank=True)


class LibraryBooks(models.Model):
    library_book_id = models.AutoField(primary_key=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    last_library_activity = models.ForeignKey(LibraryActivity, on_delete=models.CASCADE,
                                              blank=True, null=True)

    def __str__(self):
        return f"{self.library.name} {self.book}"
