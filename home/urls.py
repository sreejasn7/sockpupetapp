from django.urls import path

from .views.counter_reflex import CounterReflexView

urlpatterns = [
    path('', CounterReflexView.as_view(), name='index'),
]