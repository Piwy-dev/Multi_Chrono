from flask import Flask, render_template, request
import os
      
def create_app(test_config=None):
   """Create and configure the app."""
   app = Flask(__name__, template_folder='templates', static_folder='static')
   app.config.from_mapping(
      SECRET_KEY='dev',
   )
   
   @app.route('/')
   def home():
      return render_template('home.html')
   
   @app.route('/chronometre')
   def chronos():
      return render_template('chronometre.html')
   
   @app.route('/minuteur', methods=['GET', 'POST'])
   def minuteur():
      if request.method == 'POST':
         minutes = request.form.get('minutes', '0')
         seconds = request.form.get('seconds', '0')
         try:
            minutes = int(minutes)
            seconds = int(seconds)
         except ValueError:
            return "Invalid input. Please provide valid integers for minutes and seconds.", 400
         print(f"Minutes: {minutes}, Seconds: {seconds}")
         return render_template('minuteur.html', minutes=minutes, seconds=seconds)
      return render_template('minuteur.html')
   
   @app.route('/add-team', methods=['GET', 'POST'])
   def add_team():
      print(request.method)
      if request.method == 'POST':
         team_name = request.form.get('team_name')
         if team_name:
            print(f"Team added: {team_name}")
            return f"Team {team_name} added successfully!"
         else:
            return "Please provide a valid team name.", 400
      return render_template('add-team.html')
   
   return app
