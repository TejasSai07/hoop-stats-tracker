import { Component, OnInit } from '@angular/core';
import { PlayerService } from 'app/_services/players.service';
import { Player, Game } from 'app/player-summary/player-summary.interface';

@Component({
  selector: 'app-player-summary-response',
  templateUrl: './player-summary-response.component.html',
  styleUrls: ['./player-summary-response.component.scss']
})
export class PlayerSummaryResponseComponent implements OnInit {
  playerList: Player[] = []; 
  playerId: number; 
  playerSummary: Player | null = null; 

  constructor(private playersService: PlayerService) {}

  ngOnInit() {
    this.fetchPlayers(); 
  }

  fetchPlayers() {
    this.playersService.getPlayers().subscribe(data => {
      this.playerList = data; // Storing the fetched players
    });
  }

  onPlayerIdChange(playerId: number) {
    this.playerId = playerId;
    this.playersService.getPlayerSummary(playerId).subscribe(data => {
      this.playerSummary = data; 
    });
  }  
}
