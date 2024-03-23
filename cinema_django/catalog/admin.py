from django.contrib import admin
from catalog.models import Actor, Genre, Producer, Film, Session, Country, Ticket


class FilmInLine(admin.TabularInline):
    model = Film


class SessionInLine(admin.StackedInline):
    model = Session


class ActorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'pseudonym']
    search_fields = ['pseudonym', 'first_name']
    inlines = [FilmInLine]


class ProducerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name']
    inlines = [FilmInLine]


class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'producer', 'display_genre', 'description', 'actor', 'rating']
    search_fields = ['title', 'actor__pseudonym', 'actor__first_name', 'actor__last_name', 'genre__name', 'producer__first_name', 'producer__last_name']
    inlines = [SessionInLine]


class SessionAdmin(admin.ModelAdmin):
    list_display = ['film', 'status', 'showing']
    fieldsets = (
        ('Group 1', {
            'fields': ('film', 'status', 'showing')
        }),
    )


class TicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_film', 'row', 'place', 'film_date', 'status']
    fieldsets = (
        ('Group 1', {
            'fields': ('ticket_film', 'row', 'place', 'film_date', 'status')
        }),
    )


admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Film, FilmAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Ticket, TicketAdmin)
