from django.urls import path
import marketplace.views as views

app_name="marketplace"
urlpatterns = [
    path('',views.book_list_view,name='book-list'),
    path('<slug>/',views.book_detail_view,name="book-detail"),
    path('<book_slug>/<chapter_number>',views.chapter_detail_view,name="chapter-detail"),
    path('<book_slug>/<chapter_number>/<exercise_number>',views.exercise_detail_view,name="exercise-detail"),
]