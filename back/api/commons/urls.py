from django.urls import path

from .views import HealthView

app_name = 'commons'

urlpatterns = [
    path('health/', HealthView.as_view()),
]
