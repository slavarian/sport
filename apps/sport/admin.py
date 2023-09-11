from django.contrib import admin

from .models import Sport , Sportsman , Status_game , Game_start , Command , Сountry ,  Bet , UserProfile
# Register your models here.
admin.site.register(Sport)
admin.site.register(Sportsman)
admin.site.register(Status_game)
admin.site.register(Game_start)
admin.site.register(Command)
admin.site.register(Сountry)
admin.site.register(Bet)


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('bet_counter', 'bet_wins')

admin.site.register(UserProfile, UserAdmin)