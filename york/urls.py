from django.urls import path
from .views import PuppyInfoListView, PuppyInfoDetailView,PuppyInfoCreateView

app_name = 'york'
urlpatterns = [
    path('', PuppyInfoListView.as_view()),
    path('<int:pk>/', PuppyInfoDetailView.as_view()),
    path('create/', PuppyInfoCreateView.as_view())

]