from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일") # 이 코드를 추가하기 위해 UserCreationForm을 상속받고 거기에 이 코드를 붙임.

    class Meta:
        model = User
        fields = ("username", "email","first_name","last_name")