from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    
    # Mengirimkan nama ke template hasilnya.html
    return render_template('hasilnya.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
