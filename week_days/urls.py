from django.urls import path
from . import views


urlpatterns = [
    path('<int:week_day>', views.get_info_week_days_by_number),
    path('<str:week_day>', views.get_info_week_days),
]