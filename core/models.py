from django.db import models
from account.models import AccountBase as user

class tasks(models.Model):
    task_name           = models.CharField(max_length=30)
    client_name         = models.CharField(max_length=30)
    work_hours          = models.PositiveIntegerField(default=1)
    due_date            = models.DateField(auto_now=False)
    created_data        = models.DateField(auto_now_add=True)
    about_task          = models.TextField(blank=True)
    files_link          = models.TextField(blank=True)
    assigned_to         = models.ForeignKey(user, on_delete=models.DO_NOTHING )
    is_completed        = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task_name

    class Meta:
        ordering = ['due_date']


types = [
    ('Expense', 'Expense'),
    ('Income', 'Income'),
    ]
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_type = models.CharField(max_length=25, choices=types, default="Expense")
    def __str__(self):
        return self.category_name + " | " + self.category_type 

class Transaction(models.Model):
    name = models.CharField(max_length=500)
    ammount = models.DecimalField(max_digits=7, decimal_places=2)
    category_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return self.name + " " + str(self.date) + " " + str(self.ammount)
