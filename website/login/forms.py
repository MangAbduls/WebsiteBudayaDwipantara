# from django import forms
# from django.contrib.auth import authenticate, get_user_model


# class UserLoginForm(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField()

#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get('username')
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')

#         if username and password:
#             user = authenticate(username=username,
#                                 email=email, password=password)

#             if not user:
#                 raise forms.ValidationError('User Does Not Exist')

#             if not user.check_email(email):
#                 raise forms.ValidationError('Incorrect Email')

#             if not user.check_password(password):
#                 raise forms.ValidationError('Incorrect Password')

#         return super(UserLoginForm, self).clean(*args, **kwargs)
