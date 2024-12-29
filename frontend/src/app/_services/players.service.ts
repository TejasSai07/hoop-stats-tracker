import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Player } from '../player-summary/player-summary.interface';

@Injectable({
  providedIn: 'root'
})
export class PlayerService {
  private baseUrl = 'http://127.0.0.1:8000/api/v1';

  constructor(private http: HttpClient) {}

  // Fetching PLayer List
  getPlayers(): Observable<Player[]> {
    return this.http.get<Player[]>(`${this.baseUrl}/players/`);
  }

  // Fetching PlayerSummary
getPlayerSummary(playerId: number): Observable<Player> {
  return this.http.get<Player>(`${this.baseUrl}/playerSummary/${playerId}`);
}

}
