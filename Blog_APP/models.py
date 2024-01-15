from django.db import models
import datetime


class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('marketi', 'Marketi'),
        ('aplikacia', 'Aplikacia'),
        ('xelovnuri_inteleqti', 'Xelovnuri Inteleqti'),
        ('UI_UX', 'UI/UX'),
        ('kvleva', 'Kvleva'),
        ('Figma', 'Figma'),
    ]

    image = models.ImageField(upload_to='blogs/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    publication_date = models.DateField(default=datetime.date.today)
    categories = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.title
