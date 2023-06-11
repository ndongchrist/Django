from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


#Register an Author
class RegisterView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid() :
            name = serializer.validated_data['name']
            birth_date = serializer.validated_data['birth_date']
            country = serializer.validated_data['country']
            user  =  models.Author.objects.create(name = name, birth_date = birth_date, country = country)
            token = Token.objects.create(user=user)
            return Response({
                "your_token" : token
            })
            

#Using Viewsets
class BooksViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

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

@api_view(['GET'])
def hello(request):
    print(request)
    return Response("Hello World")

@api_view(['GET', 'POST'])
def booksView(request):
    if request.method == 'GET':
        books = Book.objects.all()
        bookSerial = BookSerializer(books, many=True)
        return Response(bookSerial.data)
    
