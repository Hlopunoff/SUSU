from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Books

# Create your views here.
def homePageView(req):
    LIMIT, OFFSET = int(req.GET.get('limit', 3)), int(req.GET.get('offset', 0))
    books = Books.objects.all()[OFFSET:OFFSET+LIMIT]

    context = {
        'books': books,
        'pages': 0,
        'offset': OFFSET + len(books),
        'limit': LIMIT,
    }

    for book in Books.objects.all():
        if book.id % 3 == 1:
            context['pages'] += 1

    return render(req, 'booksApp/index.html', context=context)

def addPageView(req):
    return render(req, 'booksApp/newBook.html')

def deleteBook(req, book_id):
    Books.objects.filter(pk=book_id).delete()

    return redirect('/')


def editPageView(req, book_id):
    selectedBook = Books.objects.get(pk=book_id)
    context = {
        'selectedBook': selectedBook
    }

    return render(req, 'booksApp/editBook.html', context=context)

def thanksPageView(req):
    if int(req.POST['flag']) < 0:
        id = Books.objects.last().id + 1
        title = req.POST['title']
        author = req.POST['author']
        price = req.POST['price']
        descr = req.POST['descr']
        q = Books(id=id, title=title, author=author, price=price, descr=descr)
        q.save()
    else:
        id=req.POST['flag']
        updateBook = Books.objects.get(pk=id)
        updateBook.title = req.POST['title']
        updateBook.author = req.POST['author']
        updateBook.price = req.POST['price']
        updateBook.descr = req.POST['descr']
        updateBook.save()


    return render(req, 'booksApp/thanks.html')
