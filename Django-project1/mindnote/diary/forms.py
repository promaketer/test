from django import forms
from .models import Page

# class PageForm(forms.Form):
#     title = forms.CharField(max_length=100, label='제목')
#     content = forms.CharField(widget=forms.Textarea, label='내용')
#     feeling = forms.CharField(max_length=80, label='감정 상태')
#     score = forms.IntegerField(label='감정 점수')
#     dt_created = forms.DateField(label='날짜')

class PageForm(forms.ModelForm):

    class Meta:
        model = Page 
        fields = ['title', 'content', 'feeling', 'score', 'dt_created']        