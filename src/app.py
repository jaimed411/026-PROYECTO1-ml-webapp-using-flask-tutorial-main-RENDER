from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Cargar el archivo CSV
csv_path = r"C:\Users\Jaime\Desktop\4GEEKS\PROYECTOS\026-PROYECTO1-ml-webapp-using-flask-tutorial-main\models\avalanche_fatalities_22_23.csv"
data = pd.read_csv(csv_path)

@app.route('/')
def index():
    countries = data['Country'].unique()
    return render_template('index.html', countries=countries)

@app.route('/deaths/<country>')
def deaths(country):
    country_data = data[data['Country'] == country]
    deaths_info = country_data.groupby('Date')['Dead'].sum().reset_index()
    deaths_list = deaths_info.values.tolist()
    return render_template('deaths.html', country=country, deaths_list=deaths_list)

if __name__ == '__main__':
    app.run(debug=True)
