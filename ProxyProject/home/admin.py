from django.contrib import admin

from .models import *

#admin panel customization
admin.site.site_header = "Podar Education Network"
admin.site.index_title = "Admin Panel"


@admin.register(stats)
class Stats(admin.ModelAdmin):
    list_display = ['Teacher','Acronym','Proxy']


@admin.register(Data_PRX)
class ProxyData(admin.ModelAdmin):
    list_display = ['Teacher','Acronym']


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher','Acronym']




@admin.register(Tsub1)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub2)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub3)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub4)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub5)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub6)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub7)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub8)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub9)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub10)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub11)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub12)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub13)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub14)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub15)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub16)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub17)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub18)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub19)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub20)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub21)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub22)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub23)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub24)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub25)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub26)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub27)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub28)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub29)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub30)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub31)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub32)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub33)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub34)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub35)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub36)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub37)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub38)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub39)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub40)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub41)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub42)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub43)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub44)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub45)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub46)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub47)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub48)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub49)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']
@admin.register(Tsub50)
class SubTimeTableAdmin(admin.ModelAdmin):
    list_display = ['Teacher']