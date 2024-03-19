from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("URG", "Urgent"),
        ("HIGH", "High priority"),
        ("LOW", "Low priority"),
    ]

    name = models.CharField(max_length=64)
    description = models.TextField(max_length=255)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=4, choices=PRIORITY_CHOICES, default="URG")
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="workers")

    def __str__(self):
        return self.name
