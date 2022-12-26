from django import forms
from .models import Customer


class CustomerModelForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%;'})
        }
        labels = {
            'name': '姓名',
            'email': '電子郵件',
            'tel': '聯絡電話'
        }

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if email.endswith('@hotmail.com'):
            raise forms.ValidationError('不得使用Hotmail電子郵件')
        return email
