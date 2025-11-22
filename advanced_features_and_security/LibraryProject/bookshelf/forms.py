

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "pub_date", "summary"]
        widgets = {
            "summary": forms.Textarea(attrs={"rows": 4}),
        }

class BookSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Search title or author"})
    )

    def clean_q(self):
        q = self.cleaned_data.get("q", "")
        # optional sanitization: strip dangerous characters, etc.
        return q.strip()
