from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

class MoneySources(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return f"{self.author} {self.name} {self.amount}"

class Transactions(models.Model):
    choices = [
    ('Expense', 'Expense'),
    ('Income', 'Income'),
]
    categories = [
        ('Food-Drinks','Food-Drinks'),
        ('Shopping', 'Shopping'),
        ('Housing', 'Housing'),
        ('Transportation', 'Transportation'),
        ('Vehicle', 'Vehicle'),
        ('Entertainment', 'Entertainment'),
        ('PC', 'PC'),
        ('Investemnts', 'Investemnts'),
        ('Other', 'Other'),
    ]

    value = models.IntegerField(default=0)
    transaction_type = models.CharField(max_length=10, choices=choices)
    money_source = models.ForeignKey(MoneySources, on_delete=models.CASCADE)
    note = models.TextField()
    category = models.CharField(max_length=50,choices=categories)
    creation_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-creation_date']
    def __str__(self):
        return f"{self.money_source} {self.value}"

class Ads(models.Model):
    read = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.TextField()
    ad_type = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    class Meta:
        ordering = ['-creation_date']
    def __str__(self):
        return f"{self.title} {self.vendor}"

class Quotes(models.Model):
    source = models.CharField(max_length=50)
    quote = models.TextField()
    image = models.TextField()
    def __str__(self):
        return f"{self.source}"


# class Incomes(models.Model):
#     value = models.IntegerField(default=0)
#     money_source = models.ForeignKey(MoneySources, on_delete=models.CASCADE)
#     note = models.TextField()
#     creation_date = models.DateField()
#     def __str__(self):
#         return f"{self.money_source} {self.value}"