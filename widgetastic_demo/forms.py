from django import forms


class UserForm(forms.Form):
    fullname = forms.CharField(max_length=50, required=False)
    username = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(required=False)


class DynamicForm(forms.Form):
    dropdown = forms.CharField(widget=forms.Select(
        choices=((' ', ' '), ('menu_1', 'Form'), ('menu_2', 'Text Image'))))


class DemoForm(forms.Form):
    name = forms.CharField(max_length=20, required=False)
    languages = forms.CharField(widget=forms.Select(
        choices=(('python', 'Python'), ('ruby', 'Ruby'), ('c', 'C'), ('javascript', 'JavaScript'))))
