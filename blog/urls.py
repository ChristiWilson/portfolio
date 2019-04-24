from django.urls import path

from . import views

urlpatterns = [
        path("", views.blog_list, name="blog_list"),
        path("<int:b_id>/", views.blog_detail, name="blog_detail"),
        path("<category>/", views.blog_category, name="blog_category"),
        ]
