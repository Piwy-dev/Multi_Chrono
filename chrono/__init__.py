from flask import *
import os
import chrono.database as db
import chrono.timer_db as tdb

      
def create_app(test_config=None):
   """Create and configure the app."""
   app = Flask(__name__, template_folder='templates', static_folder='static')
   app.config.from_mapping(
      SECRET_KEY='dev',
      DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
   )
   
   # ensure the instance folder exists
   try:
      os.makedirs(app.instance_path)
   except OSError:
      pass

   # register the database commands
   db.init_app(app)

   with app.app_context():
      db.init_db()
      tdb.delete_all_timers()
      tdb.delete_timer_duration()
   
   @app.route('/')
   def home():
      return render_template('home.html')
   
   @app.route('/chronometre')
   def chronometre():
      return render_template('chronometre.html')
   
   @app.route('/minuteur', methods=['GET', 'POST'])
   def minuteur():
      if request.method == 'POST':
         minutes = request.form.get('minutes', '0')
         seconds = request.form.get('seconds', '0')
         try:
            minutes = int(minutes)
            seconds = int(seconds)
            tdb.set_timer_duration(minutes, seconds)
         except ValueError:
            return "Invalid input. Please provide valid integers for minutes and seconds.", 400
         timers = tdb.get_all_timers()
         return render_template('minuteur.html', minutes=minutes, seconds=seconds, timers=timers)
      elif request.method == 'GET':
         minutes, seconds = tdb.get_timer_duration()
         timers = tdb.get_all_timers()
         return render_template('minuteur.html', minutes=minutes, seconds=seconds, timers=timers)
   
   @app.route('/add-team', methods=['GET', 'POST'])
   def add_team():
      print(request.method)
      if request.method == 'POST':
         team_name = request.form.get('team_name')
         if team_name:
            initial_minutes, initial_seconds = tdb.get_timer_duration()
            tdb.add_timer(team_name, initial_minutes, initial_seconds)
            return redirect('/minuteur')
         else:
            return "Please provide a valid team name.", 400
      return render_template('add-team.html')
   
   return app
