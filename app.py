from flask import Flask, render_template, request, redirect, url_for
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Quote:
    name: str
    email: str
    phone: str
    event_type: str
    date: str
    location: str
    quantity: int

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote', methods=['POST'])
def quote():
    quote_data = Quote(
        name=request.form['name'],
        email=request.form['email'],
        phone=request.form['phone'],
        event_type=request.form['event_type'],
        date=request.form['date'],
        location=request.form['location'],
        quantity=int(request.form['quantity'])
    )
    # Aquí podrías agregar lógica para enviar un correo o almacenar la cotización
    print(quote_data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)