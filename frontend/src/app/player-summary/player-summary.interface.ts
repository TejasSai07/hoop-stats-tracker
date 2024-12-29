
export interface Shot {
  isMake: boolean; // Whether the shot was made
  locationX: number; // X-coordinate of the shot
  locationY: number; // Y-coordinate of the shot
}


export interface Game {
  date: string; 
  isStarter: boolean; 
  minutes: number; 
  points: number; 
  assists: number; 
  offensiveRebounds: number; 
  defensiveRebounds: number; 
  steals: number; 
  blocks: number; 
  turnovers: number; 
  defensiveFouls: number; 
  offensiveFouls: number; 
  freeThrowsMade: number; 
  freeThrowsAttempted: number; 
  twoPointersMade: number; 
  twoPointersAttempted: number; 
  threePointersMade: number; 
  threePointersAttempted: number; 
  shots: Shot[]; // Array of shots in the game
}

export interface Player {
  name: string; 
  games: Game[]; 
}
