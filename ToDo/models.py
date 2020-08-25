from django.db import models

class toDo(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    category = models.CharField(max_length = 50)
    due_date = models.DateField()

    def __str__(self):
        return self.title



# Create your models here.
