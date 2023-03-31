from django import forms
from .models import Review

from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 5, 'cols': 40, 'class': 'form-control'}),
        }
        labels = {
            'rating': 'Rating (out of 10)',
            'comment': 'Comments',
        }
        error_messages = {
            'rating': {'required': 'Please enter a rating.'},
            'comment': {'required': 'Please enter a comment.'},
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].widget.attrs.update({'class': 'form-control mb-3', 'min': 1, 'max': 5})
