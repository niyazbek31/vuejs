from django.urls import path
from .views import FeedBackView
from . import views

urlpatterns = [
    path('', FeedBackView.as_view(), name='feedback_view'),
]
