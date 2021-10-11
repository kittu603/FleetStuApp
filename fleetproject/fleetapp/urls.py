from rest_framework import routers
from django.urls import path, include
from .views import book_view, library_book_view, checkout, checkin

router = routers.DefaultRouter()

# router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('book-create', book_view, name="book-create"),
    path('library-book-create', library_book_view),
    path(r'checkout/<int:pk>/', checkout, name="checkout"),
    path(r'checkin/<int:pk>/', checkin)
]
