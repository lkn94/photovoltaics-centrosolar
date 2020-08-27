from flask import Flask
from flask_restful import Api
import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
from pyquery import PyQuery

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)
api = Api(app)

pvIp = "IP_ADDRESS"
username = "USERNAME"
password = "PASSWORD"

@app.route('/')
def main():
    return "PV Connector"

@app.route('/actual')
def actual():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    state = tag.children()('font').children()('table').eq(1).children().eq(7).text().split()[1]
    string1strom = tag.children()('font').children()('table').eq(1).children().text().split()[48]
    string1spannung = tag.children()('font').children()('table').eq(1).children().eq(13).text().split()[1]
    string2strom = tag.children()('font').children()('table').eq(1).children().text().split()[75]
    string2spannung = tag.children()('font').children()('table').eq(1).children().text().split()[65]
    ltag = tag.children()('font').children()('table').eq(1).children().text().split()
    l1spannung = ltag[42]
    l1leistung = ltag[52]
    l2spannung = ltag[69]
    l2leistung = ltag[79]
    l3spannung = ltag[91]
    l3leistung = ltag[98]
    aktuell = tag.children()('font').children()('table').eq(1).children().eq(3).text().split()[1]
    return json.dumps({'actual': aktuell, 'state': state, 'string1strom': string1strom, 'string1spannung': string1spannung, 'string2strom': string2strom, 'string2spannung': string2spannung, 'l1spannung':l1spannung, 'l1leistung': l1leistung, 'l2spannung': l2spannung, 'l2leistung': l2leistung, 'l3spannung': l3spannung, 'l3leistung': l3leistung})

@app.route('/state')
def state():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    return "{}".format(tag.children()('font').children()('table').eq(1).children().eq(7).text().split()[1])

@app.route('/string1')
def string1():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    return "{}".format(tag.children()('font').children()('table').eq(1).children().eq(13))

@app.route('/string1/spannung')
def string1spannung():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    return "{}".format(tag.children()('font').children()('table').eq(1).children().eq(13).text().split()[1])

@app.route('/string1/strom')
def string1strom():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    return "{}".format(tag.children()('font').children()('table').eq(1).children().text().split()[48])

@app.route('/string2/spannung')
def string2spannung():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    return "{}".format(tag.children()('font').children()('table').eq(1).children().text().split()[65])

@app.route('/string2/strom')
def string2strom():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    return "{}".format(tag.children()('font').children()('table').eq(1).children().text().split()[75])

@app.route('/l1/spannung')
def l1spannung():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    return "{}".format(tag.children()('font').children()('table').eq(1).children().text().split()[42])

@app.route('/l1/leistung')
def l1leistung():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    return "{}".format(tag.children()('font').children()('table').eq(1).children().text().split()[52])

@app.route('/l2/spannung')
def l2spannung():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    return "{}".format(tag.children()('font').children()('table').eq(1).children().text().split()[69])

@app.route('/l2/leistung')
def l2leistung():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    return "{}".format(tag.children()('font').children()('table').eq(1).children().text().split()[79])

@app.route('/l3/spannung')
def l3spannung():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    return "{}".format(tag.children()('font').children()('table').eq(1).children().text().split()[91])

@app.route('/l3/leistung')
def l3leistung():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    return "{}".format(tag.children()('font').children()('table').eq(1).children().text().split()[98])

@app.route('/currentall')
def all():
    response = requests.get("http://{}/".format(pvIp), verify=False, auth=HTTPBasicAuth(username, password))
    html = response.text
    pq = PyQuery(html)
    tag = pq('form')
    return "{}".format(tag.children()('font').children()('table').eq(1).children().eq(3).text().split()[1])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=False)
