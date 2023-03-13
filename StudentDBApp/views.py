from django.shortcuts import render
from StudentDBApp.models import Student

# Create your views here.
def studentview(request):
    studentlist = Student.objects.order_by('marks')
    dict1={'studentlist':studentlist}
    return render(request,'StudentDBApp/students.html',context=dict1);

from StudentDBApp.models import Student2;
def student_homepage(request):				#new
    #students= Student2.objects.all()
    #students=Student2.objects.filter(marks__lt=35)
    #students=Student2.objects.filter(name__startswith='A')
    #students=Student2.objects.all().order_by('marks')  #ASC
    students=Student2.objects.all().order_by('-marks')   #DESC
    return render(request, 'StudentDBApp/index.html', {'students':students})

#form-view(html-form)
from StudentDBApp import forms;
#Create your views here.
def studentinputview(request):
    formsObj=forms.StudentForm()
    dict1={'form1':formsObj}
    return render(request,'StudentDBApp/input.html',context=dict1)

import time;
from StudentDBApp import forms;
def studentinputverifyview(request):
    if request.method == 'POST':
        formsObj = forms.StudentForm(request.POST);
        if formsObj.is_valid():
            print('Form-Request validation success and printing data');
            time.sleep(5)
            print('Name:', formsObj.cleaned_data['name'])
            print('Marks:', formsObj.cleaned_data['marks'])
            formsObj = forms.StudentForm();     #empty-form
            dict1 = {'form1': formsObj,'msg':'Data Submitted successfully...(Enter another data)'}
    return render(request, 'StudentDBApp/input.html',context=dict1);

import time;
from django.shortcuts import render
from StudentDBApp.forms import StudentForm
#Create your views here>
def studentinputview2(request):
    sentdata=False;
    if request.method=='POST':
        formObj=StudentForm(request.POST)
        if formObj.is_valid():
            print('Form-Request-data Validation Success and printing data')
            time.sleep(5)
            print('Name:',formObj.cleaned_data['name'])
            print('Marks:',formObj.cleaned_data['marks'])
            sentdata=True;
            formObj = StudentForm();            #empty-form
            dict1 = {'form1': formObj, 'sentdata': sentdata}
            return render(request, 'StudentDBApp/thankyou.html', context=dict1);
    formObj=StudentForm();
    dict1={'form1': formObj}
    return render(request,'StudentDBApp/input2.html',context=dict1);

from django.shortcuts import render
from StudentDBApp.forms import StudentLoginForm
#Create your views here>
def studentloginpageview(request):
    formObj=StudentLoginForm(); #Empty-form
    dict1={'form1': formObj}
    return render(request,'StudentDBApp/login.html',context=dict1);

def studentloginverifypageview(request):
    sentdata = False;  # intially get-method(url)
    if request.method=='POST':
        formObj=StudentLoginForm(request.POST)
        if formObj.is_valid():
            print('Login-Form-Request-data Validation Success and printing data')
            print('User-Name : ',formObj.cleaned_data['username'])
            print('Password : ',formObj.cleaned_data['password'])
            username = formObj.cleaned_data['username'];
            password = formObj.cleaned_data['password'];
            if username=="sai" and password=="ram":
                sentdata=True;  #post-method(Form-submit)
                username = formObj.cleaned_data['username'];
                dict1 = {'sentdata': sentdata, 'username':username}
                return render(request, 'StudentDBApp/loginsuccess.html', context=dict1);
            else:
                return render(request, 'StudentDBApp/loginunsuccess.html');
    else:
        return render(request, 'StudentDBApp/loginunsuccess.html');


from django.shortcuts import render;
from StudentDBApp import forms;
def feedbackview(request):
    sentdata=False;
    formsObj = forms.FeedBackForm();
    if request.method == 'POST':
        formsObj = forms.FeedBackForm(request.POST);
        if formsObj.is_valid():
            print('Form Validation Success and printing information');
            print('Name:', formsObj.cleaned_data['name'])
            print('Roll No:', formsObj.cleaned_data['rollno'])
            print('Email:', formsObj.cleaned_data['email'])
            print('FeedBack:', formsObj.cleaned_data['feedback'])
            formsObj = forms.FeedBackForm();
            sentdata=True;
    return render(request, 'StudentDBApp/feedback.html', {'form1': formsObj,'sentdata':sentdata});


#pwd & retypepwd SignUp form...
from django.shortcuts import render;
from StudentDBApp.forms import SignupForm
def signup_form_view(request):
    sentdata = False;
    formsObj=SignupForm();      #empty-form
    if request.method=='POST':
        formsObj=SignupForm(request.POST)       #formobj with submitted-data
        if formsObj.is_valid():
            print('Basic Validation completed and Printing Data...!!!')
            print('Name:',formsObj.cleaned_data['name'])
            print('Password:',formsObj.cleaned_data['password'])
            print('Email:',formsObj.cleaned_data['email'])
            formsObj = SignupForm();  #again-empty-form
            sentdata=True;
    return render(request,'StudentDBApp/signup.html',{'form1':formsObj,'sentdata':sentdata})


