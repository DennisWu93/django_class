from django.urls import path
from hello import views
urlpatterns = [
    path("", views.index, name="index"),
    path("Dennis", views.Dennis, name="Dennis"),
    path("<str:name>",views.greet,name ="greet")
]
