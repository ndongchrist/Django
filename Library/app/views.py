from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *


# Create your views here.
@api_view(["GET"])
def get(request):
    books = Book.objects.all()
    author = Author.objects.all()
    library = LibraryCard.objects.all()
    book_serializer = BookSerializer(books, many=True)
    author_serializer = AuthorSerializer(author, many=True)
    library_card_serializer = LibraryCardSerializer(library, many=True)
    return Response({"books": book_serializer.data, "authors": author_serializer.data, "library_cards": library_card_serializer.data})


@api_view(["POST"])
def addBook(request):
    data = request.data
    book = Book.objects.create(
        title=data["title"],
        publication_date=data["publication_date"],
        isbn=data["isbn"],
        author_id=data["author_id"],
    )
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Notes.objects.create(
        body=data['body'],
    )
    serializer = NotesSerializer(note, many=False)
    return Response(serializer.data)