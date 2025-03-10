from django.db import models
from datetime import date

class Task(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Overdue', 'Overdue'),
        ('Completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')

    def save(self, *args, **kwargs):
        # Automatically update status based on due date
        if self.due_date < date.today() and self.status != 'Completed':
            self.status = 'Overdue'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
