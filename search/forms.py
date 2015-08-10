from django import forms

class SearchForm(forms.Form):
    """ User search form. """

    query = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'search-text','required': True,'size': 50}), 
        min_length=4, max_length=20)

    def clean_query(self):
        query = self.cleaned_data['query']
        query = query.split()
        for item in query:
            if len(item) < 3 or item == '-':
                query.remove(item)
        return query
