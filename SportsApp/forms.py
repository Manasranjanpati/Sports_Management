from django import forms
from multiselectfield import MultiSelectFormField




class



class CustomerForm(forms.Form):

    name = forms.CharField(
        label = "Enter Your Name",
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )

    adress = forms.CharField(
        label = "Enter Your Adress",
        widget = forms.Textarea(
            attrs = {
                'class':'form-control',
                'placeholder':'Your Adress'
            }
        )
    )

    email = forms.EmailField(
        label="Enter Your Email ID",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }
        )
    )

    mobile = forms.IntegerField(
        label="Enter Your Contact No",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Number'
            }
        )
    )

    Gender_Choices = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect, choices=Gender_Choices
    )


    SPRTS_CHOICES = (
        ('Kaba', 'Kabaddi'),
        ('Crick', 'Cricket'),
        ('Volly', 'Vollyball'),
        ('Soccer', 'Soccer'),
        ('Basket', 'Basketball'),
        ('Base', 'Baseball'),
        ('Minton', 'Badminton'),
        ('Carrom', 'Carrom'),
        ('Swim', 'Swimming'),
        ('Chess', 'Chess'),
        ('Gym', 'Gymnastics'),
    )

    sports = MultiSelectFormField(choices=SPRTS_CHOICES)



