import json
from django.db import transaction
from app.models import Team, Player, Game, PlayerStats, Shot

def load_json(file_path):
    """Load the JSON data from a file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def insert_teams(teams_data):
    """Insert teams into the database."""
    for team in teams_data:
        Team.objects.get_or_create(id=team['id'], name=team['name'])
    print(f"Inserted {len(teams_data)} teams.")

def insert_players(players_data):
    """Insert players into the database."""
    for player in players_data:
        Player.objects.get_or_create(id=player['id'], name=player['name'])
    print(f"Inserted {len(players_data)} players.")

def insert_games(games_data):
    """Insert games and player stats into the database."""
    for game in games_data:
        try:
            home_team = Team.objects.get(id=game['homeTeam']['id'])
            away_team = Team.objects.get(id=game['awayTeam']['id'])

            # Check if the game already exists
            game_obj, created = Game.objects.get_or_create(
                id=game['id'],
                defaults={
                    'date': game['date'],
                    'home_team': home_team,
                    'away_team': away_team
                }
            )

            # Only insert player stats and shots if the game was newly created
            if created:
                for player_stats in game['homeTeam']['players'] + game['awayTeam']['players']:
                    player = Player.objects.get(id=player_stats['id'])

                    stats_obj = PlayerStats.objects.create(
                        player=player, game=game_obj,
                        minutes=player_stats['minutes'], points=player_stats['points'],
                        assists=player_stats['assists'], offensive_rebounds=player_stats.get('offensiveRebounds', 0),
                        defensive_rebounds=player_stats.get('defensiveRebounds', 0), steals=player_stats.get('steals', 0),
                        blocks=player_stats.get('blocks', 0), turnovers=player_stats.get('turnovers', 0),
                        defensive_fouls=player_stats.get('defensiveFouls', 0), offensive_fouls=player_stats.get('offensiveFouls', 0),
                        free_throws_made=player_stats.get('freeThrowsMade', 0), free_throws_attempted=player_stats.get('freeThrowsAttempted', 0),
                        two_pointers_made=player_stats.get('twoPointersMade', 0), two_pointers_attempted=player_stats.get('twoPointersAttempted', 0),
                        three_pointers_made=player_stats.get('threePointersMade', 0), three_pointers_attempted=player_stats.get('threePointersAttempted', 0),
                        is_starter=player_stats.get('isStarter', False)  # Ensure the starter status is inserted
                    )

                    # Insert shots
                    for shot in player_stats.get('shots', []):
                        Shot.objects.create(player_stats=stats_obj, x_coord=shot['locationX'], y_coord=shot['locationY'], is_make=shot['isMake'])

                print(f"Inserted stats and shots for game ID {game['id']}.")

            else:
                print(f"Game ID {game['id']} already exists. Skipping player stats insertion.")

        except Team.DoesNotExist as e:
            print(f"Error: Team not found - {e}")
        except Player.DoesNotExist as e:
            print(f"Error: Player not found - {e}")
        except Exception as e:
            print(f"An error occurred while inserting data for game ID {game['id']}: {e}")


if __name__ == "__main__":
    with transaction.atomic():  # Start a transaction
        teams_data = load_json('/Users/tejas/Desktop/OKC_Backend_Django/technical-project-deadline-10-14-23-TejasSai07/backend/raw_data/teams.json')
        players_data = load_json('/Users/tejas/Desktop/OKC_Backend_Django/technical-project-deadline-10-14-23-TejasSai07/backend/raw_data/players.json')
        games_data = load_json('/Users/tejas/Desktop/OKC_Backend_Django/technical-project-deadline-10-14-23-TejasSai07/backend/raw_data/games.json')

        insert_teams(teams_data)
        insert_players(players_data)
        insert_games(games_data)

    print("Data insertion completed!")
