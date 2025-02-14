
### 1. Backend Engineering

* Implemented a normalized PostgreSQL database to store the data provided in `backend/raw_data`. All information from the original data is accessible via the database.


* The skeleton of an API View `PlayerSummary` can be found in `backend/app/views/players.py`. This API returns a player summary that mimics the structure of `backend/app/views/sample_response/sample_response.json`.

*   Viewing http://localhost:4200/player-summary-api allows you to see the output of the API, given the playerID parameter provided in the user input.

### 2. Frontend Engineering

* The `player-summary` component, which is viewable at http://localhost:4200/player-summary, makes a call to an API endpoint at `/api/v1/playerSummary/{playerID}` that returns player summary data. One component of the player summary data are the player's shots in each game, note that:

   * The shot's x and y coordinates are provided and are measured in feet
   * The location of each shot is relative to the center of the basket, per `court_diagram.jpg` in this repository

* Within the `player-summary` component found in `frontend/src/app/player-summary/`, an interface that describes the player summary data returned from the API.


The backend will run on http://localhost:8000/.


## Frontend

### 1. Installing Prerequisites
Install Node.js (16.x.x), then run the following commands
```
cd /path/to/project/frontend
# Install Angular-Cli
npm install -g @angular/cli@12.1.0 typescript@4.6.4 --force
# Install dependencies
npm install --force
```

### 2. Starting the Frontend
Start the frontend by running the following commands
```
cd /path/to/project/frontend
npm start
```
The frontend will run on http://localhost:4200/. 


