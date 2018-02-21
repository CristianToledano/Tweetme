from django import forms
from .models import Tweet


class TweetModelForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["user", "message"]

    def clean_content(self):
        content = self.cleaned_data.get("message")
        if not content:
            raise forms.ValidationError('Is empty? Cannot!!')
        return content
