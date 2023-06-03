from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),    #name="index"对应html文件中的 {% url 'index' %} 和 views中的函数名
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")           #
]