from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


STATUS = [
    ('New', 'Nowy'),
    ('RUNNING', 'W toku'),
    ('SOLVED', 'Rozwiazany')
]

class Task(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    history = HistoricalRecords()

    def __str__(self):
        return self.name