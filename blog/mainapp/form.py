from django import forms
from .models import Post, Post_Liblery


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category','image','title','content','excert','status','comment_status','slug',)

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'excert': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }


GalleryFormSet = forms.inlineformset_factory(Post, Post_Liblery,formset=PostForm, fields=("image",), )
