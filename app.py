from flask import Flask, request, render_template, redirect , url_for,session

app = Flask(__name__)

app.secret_key = "200615"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form.get("username")
        num = request.form.get("number")
        mail = request.form.get("email")
        password = request.form.get("password")

        session['user'] = name
        session['number'] = num
        session['mail'] = mail
        session['password'] = password

        return render_template('dashboard.html',user = name)


    return render_template('login.html')    

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/feedback', methods=["GET","POST"])
def feedback():
    if request.method =='POST':
        name = request.form.get('username')
        message = request.form.get('message')

        return render_template('thankyou.html',user=name,message=message)
    
    return render_template('feedback.html')

@app.route('/profile',methods=["GET","POST"])
def profile():
    
    if request.method == "POST":
        password = request.form.get("password")
        if password == session.get('password'):
            name = session.get('user')
            number = session.get('number')
            mail = session.get('mail')
            return render_template('profile.html',user = name, number=number,mail=mail)
        
    
    return render_template('password.html')


if __name__ == '__main__':
    from os import environ
    app.run(host='0.0.0.0', port=int(environ.get('PORT', 5000)))
if __name__=="__main__":
    app.run(debug=True)
