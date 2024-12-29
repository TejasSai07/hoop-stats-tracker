# -*- coding: utf-8 -*-
"""Contains models related to stats"""
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Game(models.Model):
    date = models.DateField()
    home_team = models.ForeignKey(Team, related_name='home_games', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_games', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} on {self.date}"

class PlayerStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    minutes = models.IntegerField()
    points = models.IntegerField()
    assists = models.IntegerField()
    offensive_rebounds = models.IntegerField(null=True, blank=True)  
    defensive_rebounds = models.IntegerField(null=True, blank=True)  
    steals = models.IntegerField(null=True, blank=True)  
    blocks = models.IntegerField(null=True, blank=True)  
    turnovers = models.IntegerField(null=True, blank=True)  
    defensive_fouls = models.IntegerField(null=True, blank=True)  
    offensive_fouls = models.IntegerField(null=True, blank=True)  
    free_throws_made = models.IntegerField(null=True, blank=True) 
    free_throws_attempted = models.IntegerField(null=True, blank=True)  
    two_pointers_made = models.IntegerField(null=True, blank=True)  
    two_pointers_attempted = models.IntegerField(null=True, blank=True)  
    three_pointers_made = models.IntegerField(null=True, blank=True)  
    three_pointers_attempted = models.IntegerField(null=True, blank=True)  
    is_starter = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.player.name} Stats in {self.game.date}"

class Shot(models.Model):
    player_stats = models.ForeignKey(PlayerStats, related_name='shots', on_delete=models.CASCADE)
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    is_make = models.BooleanField()

    def __str__(self):
        return f"Shot by {self.player_stats.player.name} at ({self.x_coord}, {self.y_coord}) - {'Made' if self.is_make else 'Missed'}"
