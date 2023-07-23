from flask import Flask, render_template


app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'fdgjj54569*FJ$84jgf@#_fdsgf8958ea52588d4b518^%jh546c20f38c5e50cbd3ca067fe9d08dc259167c63a33bb267435hj89wq8*SRF89dsgkjs8g7*(&*(&%giodsg5ten0&r(9Br37h8'


@app.route('/')
def Main():

    return render_template('main.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port='8000', debug=True)