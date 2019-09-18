from django.urls import path, include
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('accounts/', include('django.contrib.auth.urls')),
path('accounts/signup', views.signup, name='signup'),
path('profile/', views.profile_show, name='profile'),
path('parks/', views.parks_index, name='parks_index'),
path('parks/<int:park_id>/', views.parks_detail, name='parks_detail'),
path('games/', views.games_index, name='games_index'),
path('parks/<int:park_id>/games/<int:game_id>/', views.games_detail, name='games_detail'),
path('parks/<int:park_id>/add_game/', views.add_game, name='add_game'),
path('games/<int:pk>/update', views.GameUpdate.as_view(), name='games_update'),
path('games/<int:pk>/delete', views.GameDelete.as_view(), name='games_delete'),
path('games/<int:game_id>/add_photo/', views.add_photo, name='add_photo'),
]