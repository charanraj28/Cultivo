from flask import Flask,render_template,request,redirect
import mysql.connector


app=Flask(__name__)

conn=mysql.connector.connect(host="localhost",user="root",password="",database="db")
cursor=conn.cursor()

@app.route('/')
def home():
    return render_template('Home.html')

# @app.route('/textchatbot')
# def register():
#     return render_template('register.html')
@app.route('/FM')
def FM():
    return render_template('FM.html')
@app.route('/CM')
def CM():
    return render_template('CM.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/news')
def news():
    return render_template('news1.html')
@app.route('/logout')
def logout():
    return redirect('/')
@app.route('/State')
def State():
    return redirect('State.html')
@app.route('/explore')
def explore():
    return render_template('Explore.html')
@app.route('/cm')
def cm():
    return render_template('CM.html')
@app.route('/home1')
def home1():
    return render_template('Home1.html')
@app.route('/statet')
def statet():
    return render_template('Telangana1.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'"""
                   .format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        return redirect('/home1')
    else:
        return redirect('/')
@app.route('/add_user',methods=['POST'])
def add_user():
    name=request.form.get('uname')
    mobileno=request.form.get('umobile')
    email=request.form.get('uemail')
    password=request.form.get('upassword')
    cursor.execute("""INSERT INTO `users` (`name`,`umobile`,`email`,`password`) VALUES
    ('{}','{}','{}','{}')""".format(name,mobileno,email,password))
    conn.commit()
    return redirect('/home')
if __name__=="__main__":
    app.run(debug=True)