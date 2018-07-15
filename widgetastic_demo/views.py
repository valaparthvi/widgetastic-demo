from django.contrib.auth import views
from . import forms
# Create your views here.


class UserView(views.FormView):
    """View to take user input and display the input."""
    form_class = forms.UserForm
    template_class = 'base.html'


class DynamicView(views.FormView):
    """View to show dynamic views based on different input."""

    pass
