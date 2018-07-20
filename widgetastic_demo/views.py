from . import forms

from django.contrib.auth import views
from django.shortcuts import render
# Create your views here.


class UserView(views.FormView):
    """View to take user input and display the input."""
    form_class = forms.UserForm
    template_name = 'base.html'

    def form_valid(self, form):
        context_data = self.get_context_data()
        data = form.cleaned_data
        context_data['data'] = ['Your %s is: %s' % (k, v) if v else '' for k, v in data.items()]
        context_data['form'] = forms.UserForm()
        return render(self.request, self.template_name, context=context_data)


class DynamicView(views.FormView):
    """View to show dynamic views based on different input."""
    form_class = forms.DynamicForm
    template_name = 'dynamic.html'

    def form_valid(self, form):
        data = form.cleaned_data
        context_data = self.get_context_data()
        if 'menu_1' in data.values():
            context_data['menu_1'] = forms.DemoForm()
            return render(self.request, self.template_name, context=context_data)
        else:
            context_data['menu_2'] = True
            return render(self.request, self.template_name, context=context_data)


class DatePickerView(views.TemplateView):
    template_name = 'datepicker.html'
