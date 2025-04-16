import datetime
from chrono import database

def get_all_teams():
    """
    Retrieve all teams from the database.
    
    Returns:
        list: A list of dictionaries representing the teams.
    """
    db = database.get_db()
    teams = db.execute("SELECT * FROM teams").fetchall()
    return [dict(team) for team in teams]

def add_team_to_database(initial_minutes, initial_second, team_name):
    """
    Add a team to the database.
    
    Args:
        team_name (str): The name of the team to add.
    """
    db = database.get_db()
    db.execute("INSERT INTO teams (initial_minutes, initial_seconds, team_name, start_time, started) VALUES (?, ?, ?, ?, ?)",
               (initial_minutes, initial_second, team_name, datetime.datetime.now(), False))
    db.commit()
    
def delete_all_teams():
    """
    Delete all teams from the database.
    """
    db = database.get_db()
    db.execute("DELETE FROM teams")
    db.commit()