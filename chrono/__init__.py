from flask import *
import os
import chrono.database as db
import chrono.teams as tms
import chrono.timer_db as timer_db

      
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
      tms.delete_all_teams()
   
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
            timer_db.set_timer(minutes, seconds)
         except ValueError:
            return "Invalid input. Please provide valid integers for minutes and seconds.", 400
         teams = tms.get_all_teams()
         print (teams)
         return render_template('minuteur.html', minutes=minutes, seconds=seconds, teams=teams)
      elif request.method == 'GET':
         minutes, seconds = timer_db.get_timer()
         teams = tms.get_all_teams()
         print (teams)
         print (minutes, seconds)
         return render_template('minuteur.html', minutes=minutes, seconds=seconds, teams=teams)
   
   @app.route('/add-team', methods=['GET', 'POST'])
   def add_team():
      print(request.method)
      if request.method == 'POST':
         team_name = request.form.get('team_name')
         if team_name:
            tms.add_team_to_database(team_name) 
            return redirect('/minuteur')
         else:
            return "Please provide a valid team name.", 400
      return render_template('add-team.html')
   
   return app
