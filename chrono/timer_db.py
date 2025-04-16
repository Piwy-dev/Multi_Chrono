from chrono import database

def set_timer(minutes, seconds):
    """
    Set the timer to a specific duration.
    
    Args:
        minutes (int): The number of minutes.
        seconds (int): The number of seconds.
    """
    db = database.get_db()
    # Clear the existing timer
    db.execute("DELETE FROM timer")
    # Set the new timer
    db.execute("INSERT INTO timer (minutes, seconds) VALUES (?, ?)", (minutes, seconds))
    db.commit()
    
def get_timer():
    """
    Get the current timer duration.
    
    Returns:
        tuple: A tuple containing the number of minutes and seconds.
    """
    db = database.get_db()
    timer = db.execute("SELECT minutes, seconds FROM timer").fetchone()
    if timer:
        return timer['minutes'], timer['seconds']
    else:
        return 0, 0
    
def delete_timer():
    """
    Delete the current timer.
    """
    db = database.get_db()
    db.execute("DELETE FROM timer")
    db.commit()
    