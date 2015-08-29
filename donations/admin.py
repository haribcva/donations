from django.contrib import admin
from donations.models import CoinsDonated
from donations.models import RoomDetails

class RoomsAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'teacher')
    search_fields = ('teacher', 'name')
    list_filter = ('grade',)
    ordering = ('-name',)
    fields = ('grade', 'name', 'teacher', 'num_students')

class CoinsAdmin(admin.ModelAdmin):
    list_display = ('week', 'numPenny', 'numDime')
    search_fields = ('week', )
    list_filter = ('week',)
    ordering = ('-week',)
    fields = ('week','room','numPenny', 'numNickel', 'numDime', 'numQuaters', 'numDollars',)

# Register your models here.
admin.site.register(CoinsDonated, CoinsAdmin)
admin.site.register(RoomDetails, RoomsAdmin)
