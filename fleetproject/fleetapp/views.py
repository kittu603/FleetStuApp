import pdb

from django.shortcuts import get_object_or_404

from .serializers import BookSerializer, LibraryBookSerializer
from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from .models import LibraryBooks, Library


# used func view as only POST required

@api_view(['POST'])
def book_view(request):
    b = JSONParser().parse(request)
    book_serializer = BookSerializer(data=b)
    if book_serializer.is_valid():
        book_serializer.save()
        return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def library_book_view(request):
    lb = JSONParser().parse(request)
    library_book_serializer = LibraryBookSerializer(data=lb)
    if library_book_serializer.is_valid():
        library_book_serializer.save()
        return JsonResponse(library_book_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(library_book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def checkout(request, pk):
    lb = get_object_or_404(LibraryBooks, pk=pk)
    if lb:
        lb.delete()
        return HttpResponse(f"Library Book {lb.book.title} checked out!", status=200)
    else:
        return HttpResponse("Book with this {pk} not available")



@api_view(['GET'])
def checkin(request, pk):
    lb = get_object_or_404(LibraryBooks, pk=pk)
    if lb:
        LibraryBooks.objects.create(pk=lb)
        return HttpResponse(f"Library Book {lb.book.title} checked in!", status=200)



# using CBV's
from rest_framework.viewsets import ModelViewSet

from .models import Book

# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
