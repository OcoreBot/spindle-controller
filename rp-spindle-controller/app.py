from flask import Flask,render_template
app = Flask(__name__)

#app.config["CACHE_TYPE"] = "null"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/Setting", methods=["GET","POST"])
def Setting():
    return render_template("Setting.html")

@app.route("/Setting/GroupSettings", methods=["GET","POST"])
def GroupSettings():
    return render_template("GroupSettings.html")

@app.route("/Setting/GroupLengthSettings", methods=["GET","POST"])
def GroupLengthSettings():
    return render_template("GroupLengthSettings.html")    

@app.route("/FactorySetting", methods=["GET","POST"])
def FactorySetting():
    return render_template("FactorySetting.html") 

@app.route("/MachineSetting", methods=["GET","POST"])
def MachineSetting():
    return render_template("MachineSetting.html") 

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')
