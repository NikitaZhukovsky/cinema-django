from django.shortcuts import render, get_object_or_404
from catalog.models import Film, Session, Tickets, Genre, Actor
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required


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


class FilmSessionDetail(DetailView):
    model = Session
    template_name = 'film_session.html'


def display_tickets(request, film_id):
    available_tickets = Tickets.objects.filter(ticket_film_id=film_id)
    return render(request, 'tickets.html', {'available_tickets': available_tickets})


@login_required
def owned_tickets(request):
    user = request.user
    tickets = Tickets.objects.filter(borrower=user)
    context = {
        'tickets': tickets
    }

    return render(request, 'reserved_detail.html', context)


@login_required
def reserve_ticket(request, ticket_id):
    ticket = get_object_or_404(Tickets, id=ticket_id)
    ticket.status = 'Sold'
    ticket.borrower = request.user
    ticket.save()
    return render(request, 'reserved_ticket.html', {'ticket': ticket})

