
from django import forms
from django.core import validators


class contactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100,initial="Your Name",help_text="Enter your name")    
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'rows': 5, 'cols': 20,'placeholder': "Message" },),help_text="Enter your message",required=False)    
    # file = forms.FileField(label='File')
    # image = forms.ImageField(label='Image')
    # email = forms.EmailField(label='Email', max_length=100) 
    birthday = forms.DateField(label='Birthday',widget=forms.DateInput(attrs={'type': 'date'}),required=False)
    # age = forms.IntegerField(label='Age')
    appointment = forms.DateTimeField(label='Appointment',widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),required=False)  
    CHOICES = [('L', 'Large'), ('M', 'Medium'), ('S', 'Small')]
    size = forms.ChoiceField(label='Size', choices=CHOICES,widget=forms.RadioSelect(),required=False)   
    MEAL = [('P','Pizza'), ('B','Burger'), ('H','Hotdog')]
    meal = forms.MultipleChoiceField(label='Meal', choices=MEAL,widget=forms.CheckboxSelectMultiple(),required=False)   
    # check = forms.BooleanField(label='Check')   
    # password = forms.CharField(label='Password', widget=forms.PasswordInput())
    
# class StudentData(forms.Form):
#     name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': "Name" }))  
#     email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': "Email" }))  
#     # def clean_name(self):
#     #     name = self.cleaned_data['name']
#     #     if len(name) < 4:
#     #         raise forms.ValidationError("Name is too short")
#     #     return name   
#     def clean(self):
#         cleaned_data = self.super().clean()
#         val_name = cleaned_data.get('name')
#         val_email = cleaned_data.get('email')
#         if len(val_name) < 4:
#             raise forms.ValidationError("Name is too short")
#         if ".com" not in val_email:
#             raise forms.ValidationError("Invalid Email") 
def length(value):
    if len(value) < 10:
        raise forms.ValidationError("Message is too short")
    
 
class StudentData(forms.Form):
     name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': "Name" }),validators=[validators.MinLengthValidator(4,message="Name is too short")])  
     email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': "Email" }),validators=[validators.EmailValidator(message="Invalid Email")]) 
    #  age = forms.IntegerField(label='Age',widget=forms.NumberInput(attrs={'placeholder': "Age" }),validators=[validators.MinValueValidator(18,message="Age is too low"),validators.MaxValueValidator(70,message="Age is too high")])    
    #  file = forms.FileField(label='File',validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','docx'],message="Only pdf and docx files are allowed")])
     message = forms.CharField(label='Message', widget=forms.Textarea(),required=False,validators=[length])
     

class PasswordValidation(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': "Name" }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput()) 
    def clean(self):
        cleaned_date = self.super().clean()
        name = cleaned_date.get('name')
        password = cleaned_date.get('password')
        confirm_password = cleaned_date.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password does not match")
        if len(name) < 4:
            raise forms.ValidationError("Name is too short")