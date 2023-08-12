from django.contrib import admin
from .models import Advertisements81

class Advertisements81Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'bu', 'created_date', 'updated_date', 'image']
    list_filter = ['auction', 'bu', 'created_time']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields':('title', 'description', 'bu', 'image'),
        }),
        ('Финансы', {
            'fields':('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisements81, Advertisements81Admin)
# Register your models here.
