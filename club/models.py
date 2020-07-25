from django.db import models

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

        def __str__(self):
            return self.club_name

class Post(models.Model):
    club_name = models.ForeignKey(Club, on_delete=models.CASCADE)
    uid = models.CharField(max_length=30)
    updated_on  = models.CharField(max_length=50)
    content     = models.TextField()

    def __str__(self):
        return self.content
