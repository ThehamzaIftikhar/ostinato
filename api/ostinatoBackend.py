from flask import Flask, request, jsonify, render_template

from core.manager import CoreManager

app = Flask(__name__)

#acting as a database.
data_storage = []
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ostinato_home', methods=['POST'])
def ostinato_home():
    form_data = request.form #request.form is basically a dictionary/hash map object
    tempo = int(form_data.get('tempo'))
    genre = form_data.get('genre')
    chaos_factor = float(form_data.get('chaos_factor'))
    key_signature = form_data.get('key_signature')
    emotion = form_data.get('emotion')

    form_entry = {
        'tempo': tempo,
        'genre': genre,
        'chaos_factor': chaos_factor,
        'key_signature': key_signature,
        'emotion': emotion
    }

    
    data_storage.append(form_entry)
    print()
    print(data_storage)

    core_instance = CoreManager()

    # Return a response
    return jsonify({'message': 'Form data received successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)

