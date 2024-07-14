from django import forms
from .models import Event, Publication, Formation

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'location', 'description', 'image']  # Include image field

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'published_date', 'author', 'content', 'image']  # Include image field

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['title', 'description', 'date', 'image']  # Include image field
