#!/usr/bin/env python

from bottle import route, run, template, get, debug, static_file
debug(True)
import sys
import datetime

sys.path.append("/Shared Items/avsys")

from av_component_LGTV import LGTV
from av_component_Marantz import MarantzRX
from av_component_system import AVSystem
from av_defs import serial_port_Marantz, serial_port_LG, DeviceError


# a simple json test main page
@route('/')
def index():
	return(str(datetime.datetime.now()));

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/Shared Items/avsys/html-static')

@route('/rc/<dev>/<opr>', method='POST')
def index(dev,opr):
    d=None
    if dev == "rx":
        d=MarantzRX(serial_port_Marantz)
    elif dev == "tv":
        d=LGTV(serial_port_LG)
    elif dev == "sys":
        d=AVSystem(
            rx=MarantzRX(serial_port_Marantz),
            tv=LGTV(serial_port_LG))

    result="Unsupported device"
    if d:
      try:
        d.talk(opr)
        result="Success"
      except DeviceError as e:
        result=e.args
                                                
    return {"Device:": dev, "Operation:": opr, "Result": result}


run(reloader=True,host='', port=8081, debug=True)
