from django.urls import path, include
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('accounts/', include('django.contrib.auth.urls')),
path('accounts/signup', views.signup, name='signup'),
path('profile/', views.profile_show, name='profile'),
path('games/', views.games_index, name='index'),
# path('games/', views.GameList.as_views(), name='games_index'),
path('games/<int:game_id>/', views.games_detail, name='detail'),
# path('games/create/', views.GameCreate.as_view(), name='games_create'),
path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_create'),
path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    
]