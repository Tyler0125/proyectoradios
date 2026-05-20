from flask import Flask, render_template, request, redirect, session
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
import os

# App Initialization
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')
bcrypt = Bcrypt(app) #Generamos un objeto llamado bcrypt //solo usar si se va a implementar encriptacion de contraseñas
