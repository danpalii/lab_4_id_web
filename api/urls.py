from django.urls import include, path
from rest_framework import routers

from api.views import events_list, event_detail, users_list, users_details

# router = routers.DefaultRouter()
# router.register(r'event', EventViewSet)

urlpatterns = [
    # Event
    path('events_list', events_list),
    path('event/<int:pk>', event_detail),
    # User
    path('users_list', users_list),
    path('user/<int:pk>', users_details),
]