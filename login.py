from flask import Flask,render_template,request, send_from_directory

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/register.html')
def regi():
    return render_template('register.html')

@app.route('/')
def regilogic():
    global email
    global password

    email = request.form.get('email')
    password = request.form.get('password')
    

@app.route('/correctpassword', methods=['POST'])
def loginlogic():
    em = request.form.get('em')
    pas = request.form.get('pas')

    if em==email:
        print("correct")

    if pas==password:
        print("correct password")

if __name__ == '__main__':
    app.run(debug=True)