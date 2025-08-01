from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField(label="Recipient's email")
    comments = forms.CharField(required=False, widget=forms.Textarea)

class RecommendPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField(label="Recipient's email")
    comments = forms.CharField(required=False, widget=forms.Textarea)
