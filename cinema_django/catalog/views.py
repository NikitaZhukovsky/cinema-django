from django.shortcuts import render
from catalog.models import Film, Session, Tickets, Genre, Actor
from django.views.generic import ListView, DetailView


def index(request):
    num_films = Film.objects.all().count()
    num_actors = Actor.objects.all().count()
    num_session = Session.objects.all().count()

    return render(request, 'index.html', {
        "num_films": num_films,
        "num_actors": num_actors,
        "num_session": num_session,
    })


class FilmListView(ListView):
    model = Film
    template_name = 'films_list.html'
    context_object_name = 'films_list'


class FilmDetailView(DetailView):
    model = Film
    template_name = 'film_detail.html'
