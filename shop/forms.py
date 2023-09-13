from django import forms
from .models import Review

class ReviewForm(forms.Form):
    rating = forms.IntegerField(label='Рейтинг', min_value=1, max_value=5)
    comment = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'rows': 5, 'cols': 60}))
