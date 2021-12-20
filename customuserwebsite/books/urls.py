from django.urls import path
from . import views

# app_name='books'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book),
    path('booklist/', views.BookListView.as_view(template_name="books/library.html")),
    path('author/add/', views.AuthorCreateView.as_view(template_name="books/author_form.html"), name='author-add'),
    path('author/<int:pk>/', views.AuthorUpdateView.as_view(), name='author-update'),
    # path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author-delete'),
]



