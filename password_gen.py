from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    try:
        length = int(data.get('length', 12))
        use_upper = data.get('uppercase', True)
        use_lower = data.get('lowercase', True)
        use_digits = data.get('digits', True)
        use_symbols = data.get('symbols', True)

        if length < 4 or length > 128:
            return jsonify({'error': 'Length must be between 4 and 128'}), 400

        characters = ''
        guaranteed = []

        if use_lower:
            characters += string.ascii_lowercase
            guaranteed.append(random.choice(string.ascii_lowercase))
        if use_upper:
            characters += string.ascii_uppercase
            guaranteed.append(random.choice(string.ascii_uppercase))
        if use_digits:
            characters += string.digits
            guaranteed.append(random.choice(string.digits))
        if use_symbols:
            symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?'
            characters += symbols
            guaranteed.append(random.choice(symbols))

        if not characters:
            return jsonify({'error': 'Select at least one character type'}), 400

        remaining = [random.choice(characters) for _ in range(length - len(guaranteed))]
        password_list = guaranteed + remaining
        random.shuffle(password_list)
        password = ''.join(password_list)

       
        strength = len([x for x in [use_upper, use_lower, use_digits, use_symbols] if x])
        if length < 8 or strength == 1:
            level = 'Weak'
        elif length < 12 or strength == 2:
            level = 'Fair'
        elif length < 16 or strength == 3:
            level = 'Strong'
        else:
            level = 'Very Strong'

        return jsonify({'password': password, 'strength': level})

    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
