#!/usr/bin/env python3
# coding: utf-8

from __future__ import print_function
from bottle import Bottle, static_file, run, template, request, json_dumps, cherrypy
import HAFBSF0200C2AX3
import grap


STATIC_FOLDER = '/home/pi/Desktop/app2/my_web_app/htdocs'
app = Bottle()

total = "Bitte eingabe tätigen"


@app.route('/static/:path#.+#')
def static_files(path):
    return static_file(path, root=STATIC_FOLDER)


@app.route('/index')  # index
def index():
    return template('index')


@app.route('/')  # index
def index():
    return template('index')


@app.route('/value')
def value():
    zeit = grap.grap_zeit()
    flow = grap.grap_flow()

    print(zeit)
    print(flow)
    return json_dumps({'data': flow, 'labels': zeit})


@app.route('/settings')
def index():
    return template('settings')


@app.route('/gpio')
def get_gpio_status():
    return template('gpio', status='')


@app.route('/settings', method='POST')
def set_gpio_status():
    pir_status = int(request.forms.get('pir_status'))
    print(pir_status)

    return template('settings', status='')


@app.route('/gpio', method='POST')
def set_gpio_status():
    global total
    pir_status1 = int(request.forms.get('pir_status1'))
    pir_status2 = int(request.forms.get('pir_status2'))
    total = pir_status1 + pir_status2
    print(pir_status1 + pir_status2)

    return template('gpio', status='')


@app.route('/live')
def index():
    return template('live', status='')


@app.route('/data')
def send_value():
    return '<p>Current data: {} SCCM</p>'.format(HAFBSF0200C2AX3.flow_value())


def komplet(total):
    return total


@app.route('/data2')
def send_value():
    return '<p> = {}</p>'.format(komplet(total))


run(app, server=cherrypy, host='0.0.0.0', port=8080, reloader=True, debug=True)
