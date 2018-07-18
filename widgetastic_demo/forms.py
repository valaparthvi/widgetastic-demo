from django import forms


class UserForm(forms.Form):
    fullname = forms.CharField(max_length=50)
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    dob = forms.DateField()


class DynamicForm(forms.Form):
    dropdown = forms.CharField(widget=forms.Select(
        choices=(('', ''), ('menu_1', 'Form'), ('menu_2', 'Simple Text'))))


class DemoForm(forms.Form):
    name = forms.CharField(max_length=20)
    dropdown = forms.CharField(widget=forms.Select(
        choices=(('python', 'Python'), ('ruby', 'Ruby'), ('c', 'C'), ('javascript', 'JavaScript'))))
