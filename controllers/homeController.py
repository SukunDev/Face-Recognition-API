from flask import jsonify, request, send_from_directory
from dotenv import load_dotenv
from deepface import DeepFace
import numpy as np
import os
import cv2

load_dotenv()


def index():
    return jsonify({"status": True, "message": "Face Recognition"})

def storedFace(filename):
    return send_from_directory('assets/images/stored-face/', filename)

def registerFace():
    file = request.files['file']
    face_name = request.form.get("face_name")
    if not face_name:
        return jsonify({"status": False, "message": "face_name can't empty"}), 400
    if not file:
        return jsonify({"status": False, "message": "No file uploaded"}), 400
    if not os.path.exists("./assets/images/.temp"):
        os.makedirs("./assets/images/.temp")
    if not os.path.exists("./assets/images/stored-face"):
        os.makedirs("./assets/images/stored-face")

    temp_image = f"./assets/images/.temp/{file.filename}"
    file.save(temp_image)
    results = DeepFace.extract_faces(temp_image)
    if len(results) > 1:
         return jsonify({"status": False, "message": "Multiple Face Detected"}), 400
    face_name = str(face_name).lower().replace(" ", "-")
    for i, face in enumerate(results):
        face_image = face['face']
        face_image_uint8 = (face_image * 255).astype(np.uint8)
        face_image_bgr = cv2.cvtColor(face_image_uint8, cv2.COLOR_RGB2BGR)
        cv2.imwrite(f"./assets/images/stored-face/{face_name}.jpg", face_image_bgr)
    os.unlink(temp_image)
    return jsonify({
        "status": True,
        "message": "Face stored",
        "result": {
            "file_name": f"{face_name}.jpg",
            "link": f"{os.environ.get("FLASK_URL")}/images/stored-face/{face_name}.jpg"
        }
    }), 200
        

def validateFace():
    file = request.files['file']
    file_name = request.form.get("file_name")
    if not file_name:
        return jsonify({"status": False, "message": "file_name can't empty"}), 400
    if not file:
        return jsonify({"status": False, "message": "No file uploaded"}), 400
    if not os.path.isfile(f"./assets/images/stored-face/{file_name}"):
        return jsonify({"status": False, "message": "face not stored, please register face before validate"}), 400
    if not os.path.exists("./assets/images/.temp"):
        os.makedirs("./assets/images/.temp")
    
    temp_image = f"./assets/images/.temp/{file.filename}"
    file.save(temp_image)
    df = DeepFace.verify(img1_path=temp_image, img2_path=f"./assets/images/stored-face/{file_name}", model_name="Facenet")
    os.unlink(temp_image)
    if df['verified']:
        return jsonify({
            "status": True,
            "message": "Face Matched",
        }), 200
    return jsonify({
            "status": False,
            "message": "Face not Matched",
        }), 400 