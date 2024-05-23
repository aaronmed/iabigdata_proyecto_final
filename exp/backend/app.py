import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Carga los modelos preentrenados
with open('h1n1_vaccine_model.pkl', 'rb') as f:
    h1n1_vaccine_model = pickle.load(f)

with open('seasonal_vaccine_model.pkl', 'rb') as f:
    seasonal_vaccine_model = pickle.load(f)

@app.route('/predict_h1n1', methods=['POST'])   
def predict_h1n1():
    data = request.json
    input_data = data.get('input_data')
    
    # Asumimos que input_data contiene los datos necesarios para la predicción
    prediction = h1n1_vaccine_model.predict([list(input_data.values())])
    return jsonify(prediction=int(prediction[0]))

@app.route('/predict_seasonal', methods=['POST'])
def predict_seasonal():
    data = request.json
    input_data = data.get('input_data')
    
    # Asumimos que input_data contiene los datos necesarios para la predicción
    prediction = seasonal_vaccine_model.predict([list(input_data.values())])
    return jsonify(prediction=int(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)
