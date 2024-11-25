from flask import Flask, request, jsonify, render_template
import pickle
import xgboost as xgb
import os

# Initialize Flask app
app = Flask(__name__)

# Load the model and DictVectorizer
model_file = 'model_xgb.bin'

if not os.path.exists(model_file):
    raise FileNotFoundError(f"Model file not found: {model_file}")

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input JSON data
        input_data = request.json
        if not input_data:
            return jsonify({"error": "No input data provided"}), 400

        # Transform input data using the DictVectorizer
        input_dict = [input_data]
        X_input = dv.transform(input_dict)

        # Convert to XGBoost DMatrix
        dmatrix_input = xgb.DMatrix(X_input, feature_names=dv.feature_names_)

        # Predict using the model
        prediction = model.predict(dmatrix_input)[0]

        # Return prediction result
        result = {"prediction": float(prediction)}
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a simple test interface
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=9696)
