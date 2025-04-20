from chrono import database
    
def get_all_chronos():
    """
    Retrieve all chronos from the database.
    
    Returns:
        list: A list of dictionaries representing the chronos.
    """
    db = database.get_db()
    chronos = db.execute("SELECT * FROM chrono").fetchall()
    return [dict(chrono) for chrono in chronos]

def add_chrono(team_name: str):
    """
    Add a chrono to the database.
    
    Args:
        team_name (str): The name of the team to add.
    """
    db = database.get_db()
    db.execute("INSERT INTO chron (team_name) VALUES (?)",
               (team_name))
    db.commit()
    
def delete_all_chronos():
    """
    Delete all chronos from the database.
    """
    db = database.get_db()
    db.execute("DELETE FROM chrono")
    db.commit()
