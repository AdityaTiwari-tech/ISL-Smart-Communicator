from flask import Flask, request, jsonify
import sign_detection_module  # hypothetical import for the sign detection logic

app = Flask(__name__)

@app.route('/api/signs/detect', methods=['POST'])
def detect_sign():
    data = request.get_json()
    # Assuming data contains image data or path
    if 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400
    
    result = sign_detection_module.detect(data['image'])  # calls the detection logic
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')