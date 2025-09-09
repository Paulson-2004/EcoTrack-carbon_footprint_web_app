from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import pyodbc
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'  # replace with a secure key in production

# Database configuration
db_config = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "server": os.environ.get("DB_SERVER"),
    "database": os.environ.get("DB_DATABASE"),
    "port": os.environ.get("DB_PORT", "1433"),
    "trust_cert": os.environ.get("TRUST_SERVER_CERTIFICATE", "false").lower() == "true"
}

# Connection string
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={db_config['server']},{db_config['port']};"
    f"DATABASE={db_config['database']};"
    f"UID={db_config['user']};"
    f"PWD={db_config['password']};"
    f"TrustServerCertificate={'yes' if db_config['trust_cert'] else 'no'};"
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Routes

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            session['user'] = username
            return redirect(url_for('calculate'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            return redirect(url_for('login'))
        except:
            return render_template('register.html', error="Username already exists")
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route("/", methods=["GET", "POST"])
def calculate():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == "POST":
        try:
            km = float(request.form["km"])
            mode = request.form["mode"]
            diet = request.form["diet"]
            kwh = float(request.form["kwh"])

            travel_em = calculate_travel_emission(km, mode)
            food_em = calculate_food_emission(diet)
            energy_em = calculate_energy_emission(kwh)
            total_em = travel_em + food_em + energy_em

            cursor.execute("""
                    INSERT INTO CarbonFootprintLog (
                        travel_km, transport_mode, diet_type, energy_kwh,
                        travel_emission, food_emission, energy_emission, total_emission
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, km, mode, diet, kwh, travel_em, food_em, energy_em, total_em)
            conn.commit()

            tips = suggest_reductions(mode, diet)

            return render_template("result.html",
                                   travel_em=travel_em,
                                   food_em=food_em,
                                   energy_em=energy_em,
                                   total_em=total_em,
                                   tips=tips)

        except ValueError:
            return render_template("index.html", error="Please enter valid numbers.")

    return render_template("index.html")

# Emission Calculators

def calculate_travel_emission(km, mode):
    emission_factors = {
        "car": 0.192,
        "bus": 0.105,
        "train": 0.041,
        "bike": 0.0,
        "walk": 0.0
    }
    return km * emission_factors.get(mode.lower(), 0)

def calculate_food_emission(diet_type):
    food_emissions = {
        "meat lover": 7.2,
        "average": 5.6,
        "vegetarian": 3.8,
        "vegan": 2.9
    }
    return food_emissions.get(diet_type.lower(), 5.6)

def calculate_energy_emission(kwh):
    return kwh * 0.233

def suggest_reductions(mode, diet_type):
    tips = []
    if mode.lower() == "car":
        tips.append("Try using public transport or carpooling to reduce emissions.")
    if diet_type.lower() == "meat lover":
        tips.append("Consider reducing meat consumption; try a meatless day!")
    tips.append("Switch to LED lights and unplug devices when not in use.")
    return tips

if __name__ == "__main__":
    app.run(debug=True)
