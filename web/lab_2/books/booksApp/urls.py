from django.urls import path

from .views import homePageView, addPageView, editPageView, thanksPageView, deleteBook

urlpatterns = [
    path('', homePageView, name='home'),
    path('add-book/', addPageView, name='add-book'),
    path('edit-book/<int:book_id>/', editPageView, name='edit-book'),
    path('thanks/', thanksPageView, name='thanks-page'),
    path('delete/<int:book_id>', deleteBook, name='delete')
]
