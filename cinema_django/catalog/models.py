from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


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
    photo = models.ImageField(upload_to='actor/images/')

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
    photo = models.ImageField(upload_to='producer/images/')

    def __str__(self):
        return (f"{self.first_name}"
                f"{self.last_name if self.last_name else ''}")


class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=400)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=False)
    photo = models.ImageField(upload_to='film/images/')

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film-detail', args=[self.pk])


class Session(models.Model):
    STATUSES = (
        ('In stock', 'In stock'),
        ('Out of stock', 'Out of stock'),

    )
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES, max_length=50, default='In stock')
    showing = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.film.title} {self.showing}"

    def get_absolute_url(self):
        return reverse('film_session-detail', args=[self.pk])


class Ticket(models.Model):
    STATUSES = (
        ('Available', 'Available'),
        ('Sold', 'Sold'),

    )
    ticket_film = models.ForeignKey(Film, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    row = models.IntegerField(null=False)
    place = models.IntegerField(null=False)
    ticket_number = models.CharField(max_length=10)
    film_date = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='tickets_date')
    status = models.CharField(choices=STATUSES, max_length=50, default='Available')

    class Meta:
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return f"{self.ticket_film.title} {self.row} {self.place} {self.film_date.showing} {self.ticket_number}"

    def get_absolute_url(self):
        return reverse('film_tickets-detail', args=[self.pk])

