from django.shortcuts import render, redirect
from .models import Book, Author
from .forms import BookCreate, AuthorCreateForm
from django.http import HttpResponse


def index(request):
	shelf = Book.objects.all()
	return render(request, 'books/library.html', {'shelf': shelf})


def upload(request):
	upload = BookCreate()
	if request.method == 'POST':
		upload = BookCreate(request.POST, request.FILES)
		if upload.is_valid():
			upload.save()
			return redirect('index')
		else:
			return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
	else:
		return render(request, 'books/upload.html', {'upload_form':upload})

def update_book(request, book_id):
	book_id = int(book_id)
	try:
		book_sel = Book.objects.get(id = book_id)
	except Book.DoesNotExist:
		return redirect('index')
	book_form = BookCreate(request.POST or None, instance = book_sel)
	if book_form.is_valid():
	   book_form.save()
	   return redirect('index')
	return render(request, 'books/upload.html', {'upload_form':book_form})

def delete_book(request, book_id):
	book_id = int(book_id)
	try:
		book_sel = Book.objects.get(id = book_id)
	except Book.DoesNotExist:
		return redirect('index')
	book_sel.delete()
	return redirect('index')


''' class-based views '''

from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

class BookListView(ListView):
	model = Book
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['shelf'] = Book.objects.all()
		return context



class AuthorCreateView(CreateView):
  
    model = Author  
    fields = ['name']

class AuthorUpdateView(UpdateView):
	model = Author
	fields = ['name']

# class AuthorDeleteView(DeleteView):
# 	model = Author
# 	success_url = reverse_lazy('author-list')