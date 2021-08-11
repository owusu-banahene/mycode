#!/usr/bin/env python3 

from flask import Flask
from flask import redirect
from flask import session
from flask import request
from flask import render_template
from flask import url_for

app.secrek_key ='A long variable'
app = Flask(__name__)

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/")
def displayPorts():
    return render_template("port.html",ports=groups)

@app.route("/input")
def getInuts():
    return render_template("addform.html")

@app.route("/data",methods=["POST"])
def addData():
    if request.form.get("ip") and request.form.get("hostname") and request.form.get("fqdn"):
        ip = request.form.get("ip")
        hostname=request.form.get("hostname")
        fqdn = request.form.get("fqdn")
        groups.append({'hostname':hostname,'ip':ip,'fqdn':fqdn})

    return redirect(url_for("displayPorts"))

if __name__=="__main__":
    app.run(host="0.0.0.0",port=2224)
