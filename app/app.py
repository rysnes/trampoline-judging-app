from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Connect to SQLite
def get_db_connection():
    conn = sqlite3.connect('instance/database.db')
    conn.row_factory = sqlite3.Row
    return conn

# API to fetch today's challenge
@app.route('/challenge', methods=['GET'])
def get_challenge():
    conn = get_db_connection()
    challenge = conn.execute('SELECT * FROM challenges ORDER BY date DESC LIMIT 1').fetchone()
    conn.close()
    
    if challenge:
        return jsonify({
            'video_url': challenge['video_url'],
            'labels': challenge['labels'].split(','),  # Skill labels
            'correct_scores': [float(x) for x in challenge['correct_scores'].split(',')],
            'explanation': challenge['explanation']
        })
    return jsonify({'error': 'No challenge found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
