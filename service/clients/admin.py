from django.contrib import admin

from clients.models import Client
from services.models import Plan, Service, Subscription

admin.site.register(Client)
admin.site.register(Plan)
admin.site.register(Service)
admin.site.register(Subscription)