from django.shortcuts import render
from django.views import generic
from catalog.models import Book, Author, BookInstance, Genre
from django.shortcuts import get_object_or_404


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

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 10)
    request.session['visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_martian_book': num_martian_book,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request,
                      'catalog/book_detail.html',
                      context={'book': book})


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, primary_key):
        author = get_object_or_404(Author, pk=primary_key)
        return render(request,
                      'catalog/author_detail.html',
                      context={'author': author})
