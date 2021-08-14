from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

class MoneySources(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.author} {self.name} {self.amount}"

class Transactions(models.Model):
    choices = [
    ('Expense', 'Expense'),
    ('Income', 'Income'),
]
    value = models.IntegerField(default=0)
    transaction_type = models.CharField(max_length=10, choices=choices)
    money_source = models.ForeignKey(MoneySources, on_delete=models.CASCADE)
    note = models.TextField()
    creation_date = models.DateField()
    def __str__(self):
        return f"{self.money_source} {self.value}"

# class Incomes(models.Model):
#     value = models.IntegerField(default=0)
#     money_source = models.ForeignKey(MoneySources, on_delete=models.CASCADE)
#     note = models.TextField()
#     creation_date = models.DateField()
#     def __str__(self):
#         return f"{self.money_source} {self.value}"