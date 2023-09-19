from django.urls import path

from .views import homePageView, \
    addPageView, \
    editPageView, \
    thanksPageView, \
    deleteBook, \
    loginPageView, \
    registerPageView, \
    auth

urlpatterns = [
    path('', homePageView, name='home'),
    path('add-book/', addPageView, name='add-book'),
    path('edit-book/<int:book_id>/', editPageView, name='edit-book'),
    path('thanks/', thanksPageView, name='thanks-page'),
    path('delete/<int:book_id>', deleteBook, name='delete'),
    path('register/', registerPageView, name='register'),
    path('login/', loginPageView, name='login'),
    path('auth/', auth, name='auth')
]
