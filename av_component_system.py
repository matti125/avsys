#!/usr/bin/python

from av_defs import DeviceError

                        
class AVSystem:    
  def __init__(self,rx,tv):
    self.friendlyname="AVSystem"
    self.rx=rx
    self.tv=tv

  def talk(self,c):
    rx=self.rx
    tv=self.tv
    print "cmd:", c
    if c == "tv":
      rx.talk("pwr-on")
      tv.talk("pwr-on")
      rx.talk("src-tv")
      tv.talk("src-dtv-cable")
      rx.talk("za-spkr-on")
    elif c== "mac":
      rx.talk("pwr-on")
      tv.talk("pwr-on")
      rx.talk("src-tv")
      tv.talk("src-hdmi1")
      rx.talk("za-spkr-on")
    elif c=="ps3":
      rx.talk("pwr-on")
      tv.talk("pwr-on")
      rx.talk("src-tv")
      tv.talk("src-hdmi3")
      rx.talk("za-spkr-on")
    elif c=="atv":
      rx.talk("pwr-on")
      tv.talk("pwr-on")
      rx.talk("src-dvd")
      tv.talk("src-hdmi4")
      rx.talk("za-spkr-on")
    elif c=="atv-listen":
      rx.talk("pwr-on")
      tv.talk("pwr-off")
      rx.talk("src-dvd")
      rx.talk("za-spkr-on")
    elif c=="radio":
      rx.talk("pwr-on")
      rx.talk("src-fm")
      rx.talk("za-spkr-on")
      tv.talk("pwr-off")

    elif c=="off":
      rx.talk("pwr-off-g")
      tv.talk("pwr-off")
    else:
      raise DeviceError("Unknown command" + c)

