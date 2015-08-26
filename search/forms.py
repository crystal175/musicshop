from django import forms

from .models import Order


class SearchForm(forms.Form):
    """ User search form. """

    query = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'search-text', 'required': True, 'size': 50}),
        min_length=4, max_length=20)

    def clean_query(self):
        query = self.cleaned_data['query']
        query = query.split()
        for item in query:
            if len(item) < 3 or item == '-':
                query.remove(item)
        return query


class OrderForm(forms.ModelForm):
    """ Order creation form. """

    error_css_class = 'errorlist'
    required_css_class = 'form-horizontal'
    song = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ['song', 'email', 'address', 'name', 'surname', 'comment']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
