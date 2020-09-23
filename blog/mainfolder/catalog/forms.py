from django import forms
from django.forms import ModelForm
from .models import Comments

from django.contrib.auth import get_user_model


class RenewArticleForm(forms.Form):
    new_text = forms.CharField()

    def clean_renewal_text(self):
        data = self.cleaned_data['new_text']
        return data


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']
        comments_user = get_user_model()