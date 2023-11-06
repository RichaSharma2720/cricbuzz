from flask import jsonify

def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

def global_error_handler(error):
    return jsonify({'error': 'Server error'}), 500
