from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    birth_date = models.DateField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class LibraryCard(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.book.title} - Card No. {self.user_id}"
