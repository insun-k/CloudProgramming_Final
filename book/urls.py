from django.urls import path

from . import views

urlpatterns = [
    path('feed/', views.FeedList.as_view()),
    path('feed/<int:pk>/', views.FeedDetail.as_view()),
    path('search/', views.BookSearchView.as_view(),name='search_book'),
    path('search/create_report', views.CreateReportView.as_view(),name="create_report"),
]