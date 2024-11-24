from flask import Flask, jsonify, request  
import json

app = Flask(__name__)

with open('quotes.json', encoding='utf-8') as file:
    quotes = json.load(file)


@app.route('/quotes/philosopher/<string:name>', methods=['GET'])
def get_qoutes_by_philosopher(name):
    try:
        filtered_quotes = [q for q in quotes if q['philosopher'].lower() == name.lower()]
        if filtered_quotes:
            return jsonify(filtered_quotes)
        else:
            return jsonify({"error": f"No quotes found for philosopher {name}"}), 404
    except KeyError as e:
        return jsonify({"error": f"Missing key in data: {str(e)}"}), 500


@app.route('/quotes/philosopher/<string:name>', methods=['POST'])
def add_quote(name):
    new_quote = request.get_json()

    if "quote" not in new_quote or not new_quote["quote"].strip():
        return jsonify({"error": "Required to fill in content for quote"}), 400

    duplicate_quote = any(
        q['quote'].strip().lower() == new_quote['quote'].strip().lower() and
        q['philosopher'].lower() == name.lower()
        for q in quotes
    )
    if duplicate_quote:
        return jsonify({"error": "This quote already exists for the philosopher"}), 400

    new_id = max(q['id'] for q in quotes) + 1 if quotes else 1

    quote_entry = {
        "id": new_id,
        "philosopher": name,
        "quote": new_quote['quote']
    }

    quotes.append(quote_entry)

    try:
        with open('quotes.json', 'w', encoding='utf-8') as file:
            json.dump(quotes, file, indent=4, ensure_ascii=False)
    except Exception as e:
        return jsonify({"error": "Failed to save quote to file", "details": str(e)}), 500

    return jsonify({"quote_entry": quote_entry, "message": "Quote successfully registered"}), 201


if __name__ == '__main__':
    app.run(debug=True)
