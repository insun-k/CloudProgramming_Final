from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('feed/', views.FeedList.as_view(),name="feed"),
    path('feed/<int:pk>/', views.FeedDetail.as_view(),name="feed_detail"),
    path('search/', views.BookSearchView.as_view(),name='search_book'),
    path('search/create_report', views.CreateReport,name="create_report"),
    path('search/update_report/<int:pk>/', views.UpdateReportView.as_view(), name="update_report"),
    path('feed/<str:slug>/', views.categories_page),
    path('feed/<int:pk>/comment_add/', views.comments_create, name='comments_create'),

]


