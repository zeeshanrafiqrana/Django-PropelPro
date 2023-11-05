from django.urls import path

from . import views

urlpatterns = [
    path('sentry-debug/', views.sentry_debug_view),
]
