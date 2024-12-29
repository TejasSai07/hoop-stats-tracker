# app/views/players.py
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from app.models import Player, PlayerStats, Shot

LOGGER = logging.getLogger('django')

def get_players(request):
    players = Player.objects.all().values('id', 'name')
    return JsonResponse(list(players), safe=False)

class PlayerStatsView(APIView):
    def get(self, request, player_id):
        stats = PlayerStats.objects.filter(player_id=player_id)
        stats_data = []
        for stat in stats:
            stats_data.append({
                'game_id': stat.game.id,
                'points': stat.points,
                'assists': stat.assists,
                # Add other fields as necessary
            })
        return Response({'player_id': player_id, 'stats': stats_data})

class PlayerSummary(APIView):
    logger = LOGGER

    def get(self, request, playerID):
        try:
            player = Player.objects.prefetch_related('playerstats_set__shots').get(id=playerID)
            player_data = {
                'name': player.name,
                'games': []
            }

            for stats in player.playerstats_set.all():
                game_data = {
                    'date': stats.game.date,
                    'isStarter': stats.is_starter,
                    'minutes': stats.minutes,
                    'points': stats.points,
                    'assists': stats.assists,
                    'offensiveRebounds': stats.offensive_rebounds,
                    'defensiveRebounds': stats.defensive_rebounds,
                    'steals': stats.steals,
                    'blocks': stats.blocks,
                    'turnovers': stats.turnovers,
                    'defensiveFouls': stats.defensive_fouls,
                    'offensiveFouls': stats.offensive_fouls,
                    'freeThrowsMade': stats.free_throws_made,
                    'freeThrowsAttempted': stats.free_throws_attempted,
                    'twoPointersMade': stats.two_pointers_made,
                    'twoPointersAttempted': stats.two_pointers_attempted,
                    'threePointersMade': stats.three_pointers_made,
                    'threePointersAttempted': stats.three_pointers_attempted,
                    'shots': [{'isMake': shot.is_make, 'locationX': shot.x_coord, 'locationY': shot.y_coord}
                              for shot in stats.shots.all()]
                }

                player_data['games'].append(game_data)

            return Response(player_data)

        except Player.DoesNotExist:
            return Response({'error': 'Player not found'}, status=404)
        except Exception as e:
            self.logger.error(f"Error fetching player data: {str(e)}")
            return Response({'error': str(e)}, status=500)
