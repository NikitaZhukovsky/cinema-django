from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    pseudonym = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='cinema_django/images/')

    def __str__(self):
        return (f"{self.first_name}"
                f"{self.last_name if self.last_name else ''}"
                f"{self.pseudonym if self.pseudonym else ''}")


class Producer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='cinema_django/images/')

    def __str__(self):
        return (f"{self.first_name}"
                f"{self.last_name if self.last_name else ''}")


class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=400)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    rating = models.FloatField(null=False)
    photo = models.ImageField(upload_to='cinema_django/images/')

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])

    def __str__(self):
        return self.title


class Session(models.Model):
    STATUSES = (
        ('In stock', 'In stock'),
        ('Out of stock', 'Out of stock'),

    )
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(choices=STATUSES, max_length=50, default='Available')
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.film.title} {self.isbn}"