from django.db import models

class CustomUser(models.Model):
    ROLES = (
        ('student', 'Student'),
        ('technician', 'Technician'),
        ('admin','admin')
    )

    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return self.username
