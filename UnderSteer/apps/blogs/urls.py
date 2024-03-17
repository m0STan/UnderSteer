from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('<int:post_id>/', views.detail, name = 'detail'),
    path('<int:post_id>/leave_comment/',views.leave_comment, name = "leave_comment"),
]
