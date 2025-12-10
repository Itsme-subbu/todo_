from django.urls import path
from . import views


urlpatterns = [
    path('addtask/',views.addtask, name='addtask'),
    path('marktask/<int:pk>/',views.marktask , name='marktask'),
    path('unmarktask/<int:pk>/', views.unmarktask, name = 'unmarktask'),
    path('edittask/<int:pk>/',views.edittask, name='edittask'),
    path('deltask/<int:pk>/',views.deltask,name='deltask')
]