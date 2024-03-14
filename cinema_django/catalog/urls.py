from django.urls import path, re_path
from catalog.views import FilmListView, index, FilmDetailView

urlpatterns = [
    path('', index, name='index'),
    path('films/', FilmListView.as_view(), name='films'),
    re_path(r'^films/(?P<pk>\d+)/$', FilmDetailView.as_view(), name='film-detail'),
]
