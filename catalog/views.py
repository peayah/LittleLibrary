from django.shortcuts import render

from catalog.models import Book, Author, BookInstance, Genre


def index(request):
    """home page View."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Counting the authors, genres, and martian books.
    num_authors = Author.objects.count()
    num_genres = Genre.objects.all().count()
    num_martian_book = Book.objects.filter(title__contains='Martian').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_martian_book':num_martian_book,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
