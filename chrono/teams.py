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

def add_team_to_database(team_name):
    """
    Add a team to the database.
    
    Args:
        team_name (str): The name of the team to add.
    """
    db = database.get_db()
    db.execute("INSERT INTO teams (name) VALUES (?)", (team_name,))
    db.commit()
    
def delete_all_teams():
    """
    Delete all teams from the database.
    """
    db = database.get_db()
    db.execute("DELETE FROM teams")
    db.commit()