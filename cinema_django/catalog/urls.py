from django.urls import path, re_path
from catalog.views import FilmListView, index, FilmDetailView, FilmSessionDetail, display_tickets, reserve_ticket,owned_tickets

urlpatterns = [
    path('', index, name='index'),
    path('films/', FilmListView.as_view(), name='films'),
    re_path(r'^films/(?P<pk>\d+)/$', FilmDetailView.as_view(), name='film-detail'),
    re_path(r'^film_session/(?P<pk>\d+)/$', FilmSessionDetail.as_view(), name='film_session-detail'),
    path('display_tickets/<int:film_id>/', display_tickets, name='display_tickets'),
    path('reserve-film/<int:ticket_id>/', reserve_ticket, name='reserve_ticket'),
    path('owned-tickets/', owned_tickets, name='owned_tickets'),
]
