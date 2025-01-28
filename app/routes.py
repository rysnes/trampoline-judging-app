from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Connect to SQLite
def get_db_connection():
    conn = sqlite3.connect('instance/database.db')
    conn.row_factory = sqlite3.Row
    return conn

# API to add a new challenge
@app.route('/add_challenge', methods=['POST'])
def add_challenge():
    data = request.json

    required_fields = ['video_url', 'labels', 'correct_scores', 'explanation']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO challenges (date, video_url, labels, correct_scores, explanation)
            VALUES (?, ?, ?, ?, ?)
        ''', (datetime.today().strftime('%Y-%m-%d'), data['video_url'], 
              ','.join(data['labels']), ','.join(map(str, data['correct_scores'])), data['explanation']))
        
        conn.commit()
        conn.close()
        return jsonify({'message': 'Challenge added successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'A challenge already exists for today'}), 409
