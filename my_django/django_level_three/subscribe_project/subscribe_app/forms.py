from django import forms
from subscribe_app.models import Customer  # Ganti dengan model yang Anda gunakan

class NewSubscriber(forms.ModelForm):
    class Meta:
        model = Customer  # Pastikan model ini benar sesuai dengan yang Anda gunakan
        fields = ['first_name', 'last_name', 'email']  # Ganti dengan field yang Anda inginkan
