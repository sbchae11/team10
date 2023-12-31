from django.urls import path
from . import views

app_name = 'brd'

urlpatterns = [
    path('', views.list, name='notice_board'), 
    path('<int:no>/', views.detail, name='detail'),
    path('update/<id>/', views.post_update , name='update'),
    path('delete/<id>/', views.post_delete , name='delete'), 
    path('faq/', views.faq_view, name='faq'),
    path('new/', views.post_create, name='create'),
    path('<int:pk>/comments/', views.comments_create, name="comments_create"),
    path('<int:post_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name="comments_delete"),
]