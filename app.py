from flask import Flask, render_template
from database import user_info_capture


app = Flask(__name__)



@app.route('/')
def hello():
    return render_template('base.html', company_name='IndEvo')


@app.route('/user')

def users_info():
    user_id = user_info_capture()
    return render_template('user.html',user= user_id , company_name='IndEvo')

# Asignamos la ruta del index
if __name__ == '__main__':
    app.run(debug=True)
