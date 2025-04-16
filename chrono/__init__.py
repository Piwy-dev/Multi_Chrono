from flask import Flask, render_template
import os
      
def create_app(test_config=None):
   """Create and configure the app."""
   app = Flask(__name__, template_folder='templates')
   app.config.from_mapping(
      SECRET_KEY='dev',
   )
   
   @app.route('/')
   def home():
      return render_template('home.html')
   
   return app
