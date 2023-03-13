from django import forms;
class StudentForm(forms.Form):
	name=forms.CharField();
	marks=forms.IntegerField();

class StudentLoginForm(forms.Form):
	username=forms.CharField();
	password=forms.CharField(widget=forms.PasswordInput)

from django import forms;
class FeedBackForm(forms.Form):
	name = forms.CharField()
	rollno = forms.IntegerField()
	email = forms.EmailField()
	feedback = forms.CharField(widget=forms.Textarea)



#another-project-form
from django import forms;
from django.core import validators   #with validations
class FeedBackForm(forms.Form):
		name = forms.CharField()
		#name = forms.CharField(validators=[starts_with_s])
		rollno = forms.IntegerField()
		email = forms.EmailField()
		#feedback = forms.CharField(widget=forms.Textarea)
		feedback = forms.CharField(widget=forms.Textarea);


		def clean_name(self):
			print('validating name-field...');
			inputname = self.cleaned_data['name'];
			if len(inputname) < 5:
				raise forms.ValidationError('Min. no-of-chars in name-field should be 5..!!');
			return inputname;

		def clean_rollno(self):
			inputrollno = self.cleaned_data['rollno'];
			print('Validating rollno-field...');
			if inputrollno == 0:
				raise forms.ValidationError('Roll-number field cannot be EMPTY or ZERO...');
			return inputrollno;

		def clean_email(self):
			inputemail = self.cleaned_data['email'];
			print("Validating email-field...");
			if len(inputemail) < 8:
				raise forms.ValidationError('Email-field cannot be EMPTY or less than 3-chars...');
			return inputemail;

		def clean_feedback(self):
			inputfeedback = self.cleaned_data['feedback']
			print("Validating feedback-field...");
			if len(inputfeedback) < 3:
				raise forms.ValidationError('Feedback-field cannot be less than 3-chars...');
			return inputfeedback

#using single clean() method for complete form validations
from django import forms;
from django.core import validators      #with validations
class FeedBackForm(forms.Form):
	name = forms.CharField()
	rollno = forms.IntegerField()
	email = forms.EmailField()
	feedback = forms.CharField(widget=forms.Textarea);

	def clean(self):
			print('Total Form validation... is getting done!!!')
			total_cleaned_data = super().clean();  # gets complete form submitted data
			inputname = total_cleaned_data['name'];
			if inputname[0].lower() != 's':
				raise forms.ValidationError('Name parameter should start with S or s only...');
			inputrollno = total_cleaned_data['rollno'];
			if inputrollno <= 0:
				raise forms.ValidationError('Rollno should be > 0...')
			inputfeedback = total_cleaned_data['feedback'];
			if len(inputfeedback) < 10 or len(inputfeedback) > 50:
				raise forms.ValidationError('Feedback should be min 10-chars & max 50-chars...')

#password & retype-pwd are same or not using validations
from django import forms
from django.core import validators
class SignupForm(forms.Form):
    name=forms.CharField(label='Enter your name :')
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(label='Reenter Password',widget=forms.PasswordInput)
    email=forms.EmailField()
    def clean(self):
        total_cleaned_data=super().clean()
        pwd=total_cleaned_data['password']
        rpwd=total_cleaned_data['repassword']
        if pwd!=rpwd:
            raise forms.ValidationError('Both Passwords must be same...!!!')


def clean(self):
	total_cleaned_data = super().clean()
	pwd = total_cleaned_data['password']
	rpwd = total_cleaned_data['repassword']
	if pwd != rpwd:
		raise forms.ValidationError('Both Passwords must be same...!!!')
	if len(pwd) < 8 or len(pwd) > 15:
		raise forms.ValidationError('Password should be min=8 & max=15 chars...')
	if len(rpwd) < 8 or len(rpwd) > 15:
		raise forms.ValidationError('Re-Password should be min=8 & max=15 chars...')
	if not pwd.isupper() or not pwd.islower() or not pwd.isnum():
		raise forms.ValidationError('Passwaord must contain 1-upper, 1-lower, 1-digit, 1-sp-char...')



