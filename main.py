from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        resp = make_response(redirect('/welcome'))
        resp.set_cookie('name', request.form.get('name'))
        resp.set_cookie('email', request.form.get('email'))
        return resp
    return render_template('home.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        resp = make_response(redirect('/'))
        resp.delete_cookie('name')
        resp.delete_cookie('email')
        return resp
    name = request.cookies.get('name')
    return render_template('welcome.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
