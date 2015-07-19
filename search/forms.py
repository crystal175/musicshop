from django import forms

class SearchForm(forms.Form):
    """ User search form. """

    query = forms.CharField(widget=forms.TextInput, min_length=4)
