#!/usr/bin/python
import time
import argparse
import sys


from av_defs import serial_port_LG, serial_port_Marantz, DeviceError
from av_component_LGTV import LGTV
from av_component_Marantz import MarantzRX
from av_component_system import AVSystem

logfile="/var/log/avsys.log"


def available_commands(codes):
  for command in codes.keys():
    code = codes[command]
    print("{0} : {1}".format(command, code))

def main(argv=None):

  if argv is None:
    argv=sys.argv
  parser=argparse.ArgumentParser()
  parser.add_argument("device",help="Device to control or 'sys' for system",
    choices=["rx","tv","sys"])
  parser.add_argument("command",help="What to do")
  args=parser.parse_args()

  f=open(logfile,'a')
  sys.stdout=f
  sys.stderr=f

  print args

  if args.device == "rx":
    dev=MarantzRX(serial_port_Marantz)
  elif args.device == "tv":
    dev=LGTV(serial_port_LG)
  elif args.device == "sys":
    dev=AVSystem(
      rx=MarantzRX(serial_port_Marantz),
      tv=LGTV(serial_port_LG))
  else:
    print "unsupported for now"
    return(1)
  try:
    dev.talk(args.command)
  except DeviceError as e:
    print "Error: Device:", args.device, ", error: ", e.args
if __name__ == "__main__":
  sys.exit(main())

