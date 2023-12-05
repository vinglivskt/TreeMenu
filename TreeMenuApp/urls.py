from django.urls import path
from TreeMenuApp.views import PageView

app_name = 'TreeMenuApp'

urlpatterns = [
    path('', PageView.as_view(), name='index')
]
