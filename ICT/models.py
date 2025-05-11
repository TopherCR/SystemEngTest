from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('engineer', 'Ingeniero'),
        ('technician', 'Técnico'),
        ('operator', 'Operador'),
    )

    PLATFORMS = (
        ('AOI', 'AOI'),
        ('AXI', 'AXI'),
        ('ICT', 'ICT'),
        ('FLASH', 'FLASH'),
        ('EOL', 'EOL'),
        ('CAL', 'CAL'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='technician',
        verbose_name='Rol'
    )

    platform = models.CharField(
        max_length=20,
        choices=PLATFORMS,
        default='ICT',
        verbose_name='Plataforma'
    )

    def __str__(self):
        return f"{self.username} ({self.role} - {self.platform})"
