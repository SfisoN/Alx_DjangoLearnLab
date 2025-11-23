from django import forms
from .models import Book


class ExampleForm(forms.Form):
   
    name = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Your name"})
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={"placeholder": "Email (optional)"})
    )
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 3}),
        max_length=500
    )

    def clean_name(self):
        return " ".join(self.cleaned_data["name"].split())

    def clean_message(self):
        msg = self.cleaned_data.get("message", "")
        return msg.strip()


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
        return q.strip()
