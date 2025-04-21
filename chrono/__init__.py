from flask import *
import os
import chrono.database as db
import chrono.timer_db as tdb
import chrono.chrono_db as cdb
      
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
   
   @app.route('/')
   def home():
      return render_template('home.html')
   
   @app.route('/chronometre')
   def chronometre():
      chronos = cdb.get_all_chronos()
      return render_template('chronometre.html', chronos=chronos)
   
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
   
   @app.route('/add-team/chrono', methods=['GET', 'POST'])
   def add_team_chrono():
      if request.method == 'POST':
         team_name = request.form.get('team_name')
         if team_name:
            print(f"Adding team: {team_name}")
            cdb.add_chrono(team_name)
            return redirect('/chronometre')
         else:
            return "Please provide a valid team name.", 400
      elif request.method == 'GET':
         return render_template('add-team.html', functionality='chrono')
         
   @app.route('/add-team/timer', methods=['GET', 'POST'])
   def add_team_timer():
      if request.method == 'POST':
         team_name = request.form.get('team_name')
         if team_name:
            initial_minutes, initial_seconds = tdb.get_timer_duration()
            tdb.add_timer(team_name, initial_minutes, initial_seconds)
            return redirect('/minuteur')
         else:
            return "Please provide a valid team name.", 400
      elif request.method == 'GET':
         return render_template('add-team.html', functionality='timer')
   
   """   
   @app.route('/delete-team/chrono', methods=['POST'])
   def delete_team_chrono():
      team_name = request.form.get('team_name')
      if team_name:
         cdb.delete_chrono(team_name)
         return redirect('/chronometre')
      else:
         return "Please provide a valid team name.", 400
      
   @app.route('/delete-team/timer', methods=['POST'])
   def delete_team_timer():
      team_name = request.form.get('team_name')
      if team_name:
         tdb.delete_timer(team_name)
         return redirect('/minuteur')
      else:
         return "Please provide a valid team name.", 400
   """
      
   @app.route('/delete-all/chrono', methods=['POST'])
   def delete_all_chronos():
      cdb.delete_all_chronos()
      return redirect('/chronometre')
   
   @app.route('/delete-all/timer', methods=['POST'])
   def delete_all_timers():
      tdb.delete_all_timers()
      return redirect('/minuteur')
   
   return app
