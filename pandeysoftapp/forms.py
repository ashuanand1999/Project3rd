from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(
        label='Enter your first name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your 1st Name'
            }
        )
    )

    lastname = forms.CharField(
        label='Enter your last name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your last Name'
            }
        )
    )

    email = forms.EmailField(
        label='Enter your Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email Id'
            }
        )
    )

    mobile = forms.IntegerField(
        label='Enter your mobile number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Mobile Number'
            }
        )
    )

    cname = forms.CharField(
        label='Enter your course name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Course name'
            }
        )
    )

class FeddbackForm(forms.Form):
    name = forms.CharField(
        label='Enter Your Name:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )

    rating = forms.IntegerField(
        label='Enter Rating:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label='Enter Your Feedback',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Feedback'
            }
        )
    )