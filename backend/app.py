from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
import base64
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Process the image (you can add more processing here if needed)
    _, buffer = cv2.imencode('.jpg', image)
    image_base64 = base64.b64encode(buffer).decode('utf-8')

    return jsonify({'image': image_base64})

if __name__ == '__main__':
    app.run(debug=True)
