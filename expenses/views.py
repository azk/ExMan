from authtools.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView

from . import models


class HomeView(LoginRequiredMixin, ListView):
    model = models.Expense

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def total(self):
        qs = self.get_queryset()
        return sum(x.amount for x in qs)


class AddView(LoginRequiredMixin, CreateView):
    model = models.Expense
    fields = (
        'expense_list',
        'timestamp',
        'amount',
        'details',
    )
    success_url = reverse_lazy("home")

    def get_queryset(self):
        return super().get_queryset().filter(expense_list__user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form =  super().get_form(form_class)
        form.fields['expense_list'].queryset = models.ExpenseList.objects.filter(user=self.request.user)

        return form


class AddListView(LoginRequiredMixin,CreateView):
    model = models.ExpenseList
    fields = (
        'name',
    )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("home")
