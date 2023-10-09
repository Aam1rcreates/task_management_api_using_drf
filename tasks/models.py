from django.db import models

# Create your models here.

# title, description, status (e.g., pending, in progress, completed), and a due date

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    due_date = models.DateField()
    # owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    
    

