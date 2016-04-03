#!/usr/bin/python
import pexpect
import fdpexpect
import serial
from av_defs import DeviceError

class MarantzRX:    
    def __init__(self, port):
        self.friendlyname="Marantz"
        self.codes = {
          'pwr-off'      : b"@PWR:1\r",
          'pwr-on'       : b"@PWR:2\r",
          'pwr-off-g'    : b"@PWR:3\r",
          'pwr-stat'   : b"@PWR:?\r",
          'vol-level'   : b"@VOL:?\r",
          'vol-up'      : b"@VOL:1\r",
          'vol-down'    : b"@VOL:2\r",
          'vol-up-fast'      : b"@VOL:3\r",
          'vol-down-fast'    : b"@VOL:4\r",
          'mute-on'          : b"@AMT:2\r",
          'mute-off'        : b"@AMT:2\r",
          'mute-status'    : b"@AMT:?\r",
          'src-tv'        : b"@SRC:1\r",
          'src-dvd'       : b"@SRC:2\r",
          'src-vcr1'      : b"@SRC:3\r",
          'src-dss'       : b"@SRC:5\r",
          'src-usb'       : b"@SRC:8\r",
          'src-aux1'      : b"@SRC:8\r",
          'src-aux2'      : b"@SRC:A\r",
          'src-cd-r'      : b"@SRC:C\r",
          'src-tape'      : b"@SRC:E\r",
          'src-tuner'     : b"@SRC:F\r",
          'src-fm'        : b"@SRC:G\r",
          'src-am'        : b"@SRC:H\r",
          'src-xm'        : b"@SRC:J\r",
          'src-sirius'    : b"@SRC:K\r",
          'za-spkr-off'   : b"@MSP:1\r",
          'za-spkr-on'    : b"@MSP:2\r",
        }
        self.connection=serial.Serial(port, 9600, 8, serial.PARITY_NONE,
                serial.STOPBITS_ONE, xonxoff=0, rtscts=0, timeout=1)
        #set descriptor to be used with pexpect
        self.e=fdpexpect.fdspawn(self.connection)

    def talk(self,cmdkey):
      try:
        cmdtosend=self.codes[cmdkey]
      except KeyError:
        raise DeviceError("Unknown command for receiver: " + cmdkey)
      print "cmddkey:", cmdkey, "cmd:", cmdtosend
      self.e.send(cmdtosend)
      self.e.expect("\r")
      print self.friendlyname, ": Before:", self.e.before, "After:", self.e.after

