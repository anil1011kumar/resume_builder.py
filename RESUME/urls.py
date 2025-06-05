from django.urls import path
from RESUME import views


urlpatterns = [
    path('',views.accept,name='accept'),
    path('<int:id>/',views.resume,name="resume")
]