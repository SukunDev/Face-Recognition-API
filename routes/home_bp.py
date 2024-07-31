from flask import Blueprint

from controllers.homeController import index, storedFace, registerFace, validateFace

home_bp = Blueprint('home_bp', __name__)

home_bp.route('/', methods=['GET'])(index)
home_bp.route('/images/stored-face/<path:filename>', methods=['GET'])(storedFace)
home_bp.route('/register-face', methods=['POST'])(registerFace)
home_bp.route('/validate-face', methods=['POST'])(validateFace)