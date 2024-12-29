""""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""

from django.urls import re_path
from django.views.generic import TemplateView
from app.views.players import PlayerSummary, PlayerStatsView, get_players  # Importing my different views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # my current API endpoints
    re_path(r'^api/v1/playerSummary/(?P<playerID>[0-9]+)$', PlayerSummary.as_view(), name='player_summary'),
    re_path(r'^api/v1/playerStats/(?P<player_id>[0-9]+)$', PlayerStatsView.as_view(), name='player_stats'),
    re_path(r'^api/v1/players/$', get_players, name='get_players'),  
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
