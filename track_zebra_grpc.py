#!/usr/bin/python

# Set target (waypoint) positions for UAVs

import sys
import struct
import socket
import math
import time
import argparse
import glob
import subprocess
import threading
import datetime

from core.api.grpc import client
from core.api.grpc import core_pb2
import xmlrpc.client

uavs = []
mynodeseq = 0
nodecnt = 0
protocol = 'none'
mcastaddr = '235.1.1.1'
port = 9100
ttl = 64
core = None
session_id = None 

filepath = '/tmp'
nodepath = ''

thrdlock = threading.Lock()
xmlproxy = xmlrpc.client.ServerProxy("http://localhost:8000", allow_none=True)

class relay():
  def __init__(self, relay_id):
    self_relay_id = relay_id


  def harness_solar(self):

  def calculate_SWIPT(self):

class sensor():
  def __init__(self, sensor_id):
    self_sensor_id = sensor_id

  def harness_swipt(self):

  def send_data(self):

  def get_distance(self, relay):


class sink():
  def __init__(self, sink_id):
    self_sink_id = sink_id


  
  
#---------------
# main
#---------------
def main():
  global relays
  global sink
  global protocol
  global Sensors
  global core
  global session_id

  # Get command line inputs 
  parser = argparse.ArgumentParser()
  parser.add_argument('-my','--my-id', dest = 'uav_id', metavar='my id',
                      type=int, default = '1', help='My Node ID')
  parser.add_argument('-c','--covered-zone', dest = 'covered_zone', metavar='covered zone',
                       type=int, default = '1200', help='UAV covered zone limit on X axis')
  parser.add_argument('-r','--track_range', dest = 'track_range', metavar='track range',
                       type=int, default = '600', help='UAV tracking range')
  parser.add_argument('-i','--update_interval', dest = 'interval', metavar='update interval',
                      type=int, default = '1', help='Update Inteval')
  parser.add_argument('-p','--protocol', dest = 'protocol', metavar='comms protocol',
                      type=str, default = 'none', help='Comms Protocol')

  
  # Parse command line options
  args = parser.parse_args()

  protocol = args.protocol

  # Create grpc client
  core = client.CoreGrpcClient("172.16.0.254:50051")
  core.connect()
  response = core.get_sessions()
  if not response.sessions:
    raise ValueError("no current core sessions")
  session_summary = response.sessions[0]
  session_id = int(session_summary.id)
  session = core.get_session(session_id).session

  # Populate the uavs list with current UAV node information
  mynodeseq = 0
  node = CORENode(args.uav_id, -1)
  uavs.append(node)
  RedeployUAV(node)
  RecordTarget(node)
  nodecnt += 1
  
  if mynodeseq == -1:
    print("Error: my id needs to be in the list of UAV IDs")
    sys.exit()
    
  # Initialize values
  corepath = "/tmp/pycore.*/"
  nodepath = glob.glob(corepath)[0]
  msecinterval = float(args.interval)
  secinterval = msecinterval/1000

  if protocol == "udp":
    # Create UDP receiving thread
    recvthrd = ReceiveUDPThread()
    recvthrd.start()
        
  # Start tracking targets
  while 1:
    time.sleep(secinterval)

    if protocol == "udp":    
      thrdlock.acquire()
    
    TrackTargets(args.covered_zone, args.track_range)

    if protocol == "udp":
      thrdlock.release()


if __name__ == '__main__':
  main()
