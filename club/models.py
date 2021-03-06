from django.db import models
from django.urls import reverse

CLUBS=[
    ('Coding Club','Coding Club IITG'),
    ('Electronics','Electroncis Club IITG'),
    ('Robotics','Robotics Club IITG'),
    ('LitSoc','Literary Society IITG'),
    ('Xpressions','Drama Club IITG'),
    ('Aeromodelling','Aeromodelling Club IITG'),
    ('Cadence','Dance Club IITG'),
    ('IITG.AI','Artificial intelligence Club IITG'),
]

class Club(models.Model):
        club_name = models.CharField(max_length=50, choices=CLUBS)
        secretary = models.CharField(max_length=30)
        club_id= models.CharField(max_length=50)

        def __str__(self):
            return self.club_name

        def get_absolute_url(self):
            return reverse('detail', kwargs={'pk': self.club_id })

class Post(models.Model):
    club_name = models.ForeignKey(Club, on_delete=models.CASCADE)
    uid = models.CharField(max_length=30)
    updated_on  = models.CharField(max_length=50)
    content     = models.TextField()

    def __str__(self):
        return self.content
