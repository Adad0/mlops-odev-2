from flask import Flask, jsonify, request
from feature_eng import hash_customer_id

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    # Smoke test buraya istek atıp 200 OK alacak
    return jsonify({"status": "healthy", "service": "churn-prediction"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    customer_id = data.get('customer_id', 'UNKNOWN')
    
    # Feature engineering'i kullan
    geo_code = hash_customer_id(customer_id)
    
    # Dummy prediction (Model dosyası yüklemiyoruz, mantığı test ediyoruz)
    return jsonify({
        "customer_id": customer_id,
        "geo_code": geo_code,
        "churn_probability": 0.45,
        "prediction": 0  # Not Churn
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)