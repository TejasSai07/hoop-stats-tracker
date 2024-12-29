import { Component, OnInit } from '@angular/core';
import { PlayerService } from '../_services/players.service';
import { Player, Game } from './player-summary.interface';

@Component({
  selector: 'app-player-summary',
  templateUrl: './player-summary.component.html',
  styleUrls: ['./player-summary.component.scss']
})
export class PlayerSummaryComponent implements OnInit {
  players: Player[] = []; 
  player: Player | null = null; // Player data
  shots: { x: number; y: number; isMake: boolean }[] = []; 
  totalGames: number = 0;
  totalPoints: number = 0;
  totalAssists: number = 0;

  courtWidth: number = 600; // Width of the court 
  courtHeight: number = (47/50) * this.courtWidth; // Height of the court

  constructor(private playerService: PlayerService) {}

  ngOnInit(): void {
    this.fetchPlayers(); // Fetch players when the component initializes
  }

  fetchPlayers(): void {
    this.playerService.getPlayers().subscribe(
      data => {
        this.players = data as Player[]; 
      },
      error => {
        console.error('Error fetching players:', error);
      }
    );
  }

  onPlayerSelected(playerId: number): void {
    this.playerService.getPlayerSummary(playerId).subscribe(
      data => {
        this.player = data as Player;
        if (this.player) {
          this.totalGames = this.player.games.length;
          this.totalPoints = this.calculateTotalPoints();
          this.totalAssists = this.calculateTotalAssists();
          this.extractShots(this.player.games);
        }
      },
      error => {
        console.error('Error fetching player summary:', error);
        alert('Error loading player summary data.');
      }
    );
  }

  // total points from player's games
  calculateTotalPoints(): number {
    return this.player?.games.reduce((sum, game) => sum + game.points, 0) || 0;
  }

  // total assists from player's games
  calculateTotalAssists(): number {
    return this.player?.games.reduce((sum, game) => sum + game.assists, 0) || 0;
  }

  // extracting shots from player's games
extractShots(games: Game[]): void {
  if (games && Array.isArray(games)) {
    this.shots = [];
    games.forEach(game => {
      if (game.shots && Array.isArray(game.shots)) {
        game.shots.forEach(shot => {
          this.shots.push({
            x: shot.locationX,
            y: shot.locationY,
            isMake: shot.isMake
          });
        });
      }
    });
    console.log(this.shots); 
  } else {
    this.shots = [];
  }
}


getXPosition(x: number): number {
  const courtWidthFeet = 50; // Full court width in feet
  const halfCourtWidthFeet = courtWidthFeet / 2; // Half-court width
  
  // Map X-coordinate in feet to pixels
  const pixelX = (x + halfCourtWidthFeet) * (this.courtWidth / courtWidthFeet);

  // was helpful for me to decode
  console.log(`Shot X-coordinate in feet: ${x}, Mapped X in pixels: ${pixelX}`);
  
  return pixelX;
}



getYPosition(y: number): number {
  const courtHeightFeet = 47;  // Full court length in feet
  const basketToBaseline = 5.25;  // Distance from basket to baseline in feet -> got from research
  const totalCourtLength = courtHeightFeet + basketToBaseline;  // Full court length to map
  let pixelY;

  // had to use 2 logics since initially y values under the basket were giving me issues
  if (y >= 0) {
    // For shots above the basket (positive y-values)
    pixelY = this.courtHeight - ((y + basketToBaseline) / totalCourtLength) * this.courtHeight;
    console.log(`Above basket: Y-coordinate (feet): ${y}, Transformed Y (pixels): ${pixelY}`);
  } else {

    const adjustedY = y * 0.75; // Adjust this scaling factor as needed for your court size
    pixelY = this.courtHeight - ((adjustedY + basketToBaseline) / totalCourtLength) * this.courtHeight;
    console.log(`Below basket: Y-coordinate (feet): ${y}, Transformed Y (pixels): ${pixelY}`);
  }

  return pixelY;
}














}
