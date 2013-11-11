from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class NewAccountForm(forms.Form):
	first_name= forms.CharField(label="First name", widget=forms.TextInput())
	last_name= forms.CharField(label="Last name", widget=forms.TextInput())
	email= forms.EmailField(label="Email", widget=forms.TextInput())
	username=forms.CharField(label="Username", widget=forms.TextInput())
	password=forms.CharField(label="Password", widget=forms.PasswordInput())
		
class UploadVideoForm(forms.Form):
	name	= forms.CharField(label="Name", widget=forms.TextInput())
	video	= forms.FileField(label="Video")
	#date	= forms.DateTimeField()
	message	= forms.CharField(label="Message", widget=forms.TextInput())
	#datepublish = forms.DateTimeField()

	def clean(self):
		return self.cleaned_data

class RegisterForm(forms.Form):
	nombre = forms.CharField(label="Nombre", widget=forms.TextInput())
	apellidos = forms.CharField(label="Apellidos", widget=forms.TextInput())
	email = forms.EmailField(label="Email", widget=forms.TextInput())
	password_1=forms.CharField(label="Password", widget=forms.PasswordInput(render_value=False))
	password_2=forms.CharField(label="Confirmar Password", widget=forms.PasswordInput(render_value=False))
	
