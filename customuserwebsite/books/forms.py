from django import forms
from .models import Book, Author


class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ('name','picture','author','email')

class AuthorCreateForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ('name',)