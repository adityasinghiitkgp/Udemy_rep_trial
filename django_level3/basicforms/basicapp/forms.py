from django import forms
from django.core import validators



# are oun validators but individual to check name
def check_for_z(value):
    if value[0].lower()!="z":
        raise forms.ValidationError("Name neends to start with Z")



class FormName(forms.Form):
    name=forms.CharField(validators=[check_for_z])
    email=forms.EmailField()
    # to verify here only
    verify_email=forms.EmailField(label="Enter your email")
    text=forms.CharField(widget=forms.Textarea)

    # for forms validation, other then buildin
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data["botcatcher"]
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("Gotcha bot")

    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data["email"]
        vmail=all_clean_data["verify_email"]

        if email!=vmail:
            raise forms.ValidationError("email not match")
