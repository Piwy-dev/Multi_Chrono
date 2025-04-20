from chrono import database
import datetime

def set_timer_duration(minutes, seconds):
    """
    Set the timer duration in the database.
    
    Args:
        minutes (int): The number of minutes.
        seconds (int): The number of seconds.
    """
    db = database.get_db()
    db.execute("DELETE FROM timerduration")
    db.execute("INSERT INTO timerduration (minutes, seconds) VALUES (?, ?)", (minutes, seconds))
    db.commit()
    
def get_timer_duration():
    """
    Get the current timer duration.
    
    Returns:
        A tuple containing the number of minutes and seconds.
    """
    db = database.get_db()
    timer = db.execute("SELECT minutes, seconds FROM timerduration").fetchone()
    if timer:
        return timer['minutes'], timer['seconds']
    else:
        return 0, 0
    
def delete_timer_duration():
    """
    Delete the current timtimerdurationer.
    """
    db = database.get_db()
    db.execute("DELETE FROM timerduration")
    db.commit()
    
def get_all_timers():
    """
    Retrieve all timers from the database.
    
    Returns:
        list: A list of dictionaries representing the timers.
    """
    db = database.get_db()
    timers = db.execute("SELECT * FROM timer").fetchall()
    return [dict(team) for team in timers]

def add_timer(team_name: str, initial_minutes: int, initial_second: int):
    """
    Add a timer to the database.
    
    Args:
        team_name (str): The name of the team to add.
        initial_minutes (int): The initial number of minutes.
        initial_seconds (int): The initial number of seconds.
    """
    db = database.get_db()
    db.execute("INSERT INTO timer (team_name, initial_minutes, initial_seconds) VALUES (?, ?, ?)",
               (team_name, initial_minutes, initial_second))
    db.commit()
    
def delete_all_timers():
    """
    Delete all timers from the database.
    """
    db = database.get_db()
    db.execute("DELETE FROM timer")
    db.commit()
