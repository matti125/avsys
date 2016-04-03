#!/usr/bin/python
import pexpect
import fdpexpect
import serial
from av_defs import DeviceError

class LGTV:    
    def __init__(self, port):
        self.friendlyname="tv"
        self.codes = {
          'aspect-43'      : b"kc 00 01",
          'aspect-169'     : b"kc 00 02",
          'aspect-stat'  : b"kc 00 ff",
          'pwr-off'      : b"ka 00 00",
          'pwr-on'       : b"ka 00 01",
          'pwr-stat'   : b"ka 00 ff",
          'vol-level'   : b"kf 00 ff",
          'mute-on'          : b"ke 00 00",
          'mute-off'             : b"ke 00 01",
          'mute-stat'            : b"ke 00 ff",
          'src-dtv-air'          : b"xb 00 00",
          'src-dtv-cable'         : b"xb 00 01",
          'src-dtv-satellite'    : b"xb 00 02",
          'src-analog-air'    : b"xb 00 10",
          'src-analog-cable'      : b"xb 00 11",
          'src-av1'              : b"xb 00 20",
          'src-av2'              : b"xb 00 21",
          'src-comp'             : b"xb 00 40",
          'src-rgbpc'            : b"xb 00 60",
          'src-hdmi1'            : b"xb 00 90",
          'src-hdmi2'            : b"xb 00 91",
          'src-hdmi3'            : b"xb 00 92",
          'src-hdmi4'            : b"xb 00 93",
          'src-status'           : b"xb 00 ff",
          'btn-chn-up'		:b"mc 00 00",
          'btn-chn-down'	:b"mc 00 01",
          'btn-menu-q'		:b"mc 00 45",
          'btn-home'		:b"mc 00 43",
          'btn-0'		:b"mc 00 10",
          'btn-1'		:b"mc 00 11",
          'btn-2'		:b"mc 00 12",
          'btn-3'		:b"mc 00 13",
          'btn-4'		:b"mc 00 14",
          'btn-5'		:b"mc 00 15",
          'btn-6'		:b"mc 00 16",
          'btn-7'		:b"mc 00 17",
          'btn-8'		:b"mc 00 18",
          'btn-9'		:b"mc 00 19",
          'btn-list'		:b"mc 00 4c",
          'btn-qview'		:b"mc 00 1a",
          'btn-mute'		:b"mc 00 09",
          'btn-vol-up'		:b"mc 00 02",
          'btn-vol-down'	:b"mc 00 03",
          'btn-mark'		:b"mc 00 1e",
          'btn-c-up'		:b"mc 00 40",
          'btn-c-down'		:b"mc 00 41",
          'btn-c-left'		:b"mc 00 07",
          'btn-c-right'		:b"mc 00 06",
          'btn--enter'		:b"mc 00 44",
          'btn-back'		:b"mc 00 28",
          'btn-info'		:b"mc 00 aa",
          'btn-red'		:b"mc 00 72",
          'btn-green'		:b"mc 00 71",
          'btn-yellow'		:b"mc 00 63",
          'btn-blue'		:b"mc 00 61",
          'btn-tv'		:b"mc 00 1a",
          'btn-exit'		:b"mc 00 1a",          
        }
        self.connection=serial.Serial(port, 9600, 8, serial.PARITY_NONE,
                serial.STOPBITS_ONE, xonxoff=0, rtscts=0, timeout=1)
        #set descriptor to be used with pexpect
        self.e=fdpexpect.fdspawn(self.connection)

    def talk(self,cmdkey):
      cr="\r"
      print "cmddkey:", cmdkey
      try:
        cmdtosend=self.codes[cmdkey]
      except KeyError:
        raise DeviceError('Unknown command for TV: ' + cmdkey )
      gotresponse=False
      triesleft=20
      while not gotresponse and (triesleft > 0) :
        triesleft = triesleft - 1
        self.e.send(cmdtosend)
        self.e.send(cr)
        i=self.e.expect(['x',pexpect.EOF, pexpect.TIMEOUT],timeout=1)
        if i==0:
          print self.friendlyname,": Before:", self.e.before, "After:", self.e.after
          gotresponse=True
        elif i== 1:
            raise DeviceError("End of file reached while reading response from device")
            triesleft = 0
        elif i==2:
          pass
      if not gotresponse:  
        raise DeviceError("Timed out while waiting for response from device")  
                        

