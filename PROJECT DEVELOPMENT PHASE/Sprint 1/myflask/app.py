from flask import Flask,render_template
import ibm_db
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hvv22243;PWD=iXmuhK8KgBWxkJWb;",'','')
print('connection succesful')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/forgot")
def forgot():
    return render_template('forgot.html')

@app.route("/dashbord")
def about():
    return render_template('dashboard.html')
