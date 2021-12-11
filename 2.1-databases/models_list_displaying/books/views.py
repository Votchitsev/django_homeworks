from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def search_page_number(pagi: Paginator, date):

    for p in pagi.page_range:
        if str(pagi.get_page(p).object_list[0].pub_date) == date:
            return p


def books_view(request):
    template = 'books/books_list.html'
    context = {
        'books': Book.objects.all().order_by('pub_date')
    }
    return render(request, template, context)


def books_view_with_date(request, pub_date):

    template = 'books/book_pagi.html'
    books = Book.objects.all().order_by('pub_date')

    paginator = Paginator(books, 1)

    page = paginator.get_page(search_page_number(paginator, pub_date))

    next_date = None

    if page.has_next():
        next_page = paginator.get_page(page.next_page_number())
        next_date = next_page.object_list[0].pub_date

    previous_date = None

    if page.has_previous():
        previous_page = paginator.get_page(page.previous_page_number())
        previous_date = previous_page.object_list[0].pub_date

    context = {
        'date': pub_date,
        'page': page,
        'books': books,
        'next_date': str(next_date),
        'previous_date': str(previous_date)
    }
    return render(request, template, context)
