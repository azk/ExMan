from django.conf import settings
from django.db import models


class ExpenseList(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    timestamp = models.DateTimeField()
    amount = models.DecimalField(max_digits=12,
                                 decimal_places=2)
    details = models.TextField()
    expense_list = models.ForeignKey(ExpenseList)
