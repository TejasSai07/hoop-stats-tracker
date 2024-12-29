
### 1. Backend Engineering

* Architect and implement a normalized PostgreSQL database to store the data provided in `backend/raw_data`. All information from the original data should be accessible via the database.

* Write a brief description of your database architecture (<250 words). Feel free to provide a visual representation as an aide. Submit relevant responses in the `written_responses` folder provided.

* In the programming language of your choice, write a process to load the dataset into your PostgreSQL database. Ensure that this process can run repeatedly without duplicating or obscuring references in the database. Include the source code of your process in the `backend/scripts` folder. Note: You can feel free to utilize the power of Django models and migrations to achieve this step.


* The skeleton of an API View `PlayerSummary` can be found in `backend/app/views/players.py`. Implement this API to return a player summary that mimics the structure of `backend/app/views/sample_response/sample_response.json`. Feel free to import additional modules/libraries in order to do this, but ensure that the `backend/requirements.txt` is updated accordingly. Viewing http://localhost:4200/player-summary-api allows you to see the output of your API, given the playerID parameter provided in the user input.

### 2. Frontend Engineering

* The `player-summary` component, which is viewable at http://localhost:4200/player-summary, makes a call to an API endpoint at `/api/v1/playerSummary/{playerID}` that returns player summary data. One component of the player summary data are the player's shots in each game, note that:

   * The shot's x and y coordinates are provided and are measured in feet
   * The location of each shot is relative to the center of the basket, per `court_diagram.jpg` in this repository

* Within the `player-summary` component found in `frontend/src/app/player-summary/`, create an interface that describes the player summary data returned from the API.

* Feel free to import additional modules of your choice, and design the interface however you wish. Just make sure that the `package.json` and `package-lock.json` are updated accordingly.


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


