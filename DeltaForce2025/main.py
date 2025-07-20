# main
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/operators')
def operators():
    return render_template('operators.html')

@app.route('/weapons')
def weapons():
    return render_template('weapons.html')

@app.route('/weapon/<int:weapon_id>')
def weapon_detail(weapon_id):
    return render_template('weapon_detail.html', weapon_id=weapon_id)

if __name__ == '__main__':
    app.run(debug=True)
