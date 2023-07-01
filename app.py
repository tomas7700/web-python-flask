from flask import Flask, render_template
from database import user_info_capture, load_info

app = Flask(__name__)



@app.route('/')
def hello():
    id = user_info_capture()
    return  render_template('index.html',info= id ,company_name='IndEvo')



@app.route('/user/<id>')
def show_info(id):
    info = load_info(id)
    if not info:
        return 'not found', 404
    
    return render_template('user.html', info=info, company_name='IndEvo')




# Asignamos la ruta del index
if __name__ == '__main__':
    app.run(debug=True)
