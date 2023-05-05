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

from core.api.grpc import client, wrappers
from core.api.grpc import core_pb2
from math import floor



protocol = 'none'
mcastaddr = '235.1.1.1'
port = 9100
ttl = 64
core = None
session_id = None 

filepath = '/tmp'
nodepath = ''

thrdlock = threading.Lock()

class relay():
  def __init__(self, relay_id):
    self_relay_id = relay_id


  #def harness_solar(self):

  #def calculate_SWIPT(self):

class sensor():
  def __init__(self, sensor_id):
    self.sensor_id = sensor_id
    self.get_closest_relay()
    self.relay_id = self.closest_relay
    self.link_relay()
    #print("id: ",self.sensor_id, " closest relay:",self.relay_id)

  #def harness_swipt(self):

  #def send_data(self):

  #def get_distance(self, relay):

  def get_closest_relay(self):
    sense_node = core.get_node(session_id, self.sensor_id).node
    x = sense_node.position.x
    y = sense_node.position.y
    x = math.floor(x/333.33)
    y = math.floor(y/333.33)
    self.closest_relay = x + 1 + 3*y

  def link_relay(self):
    node1 = core.get_node(session_id, self.sensor_id).node
    node2 = core.get_node(session_id, self.relay_id).node
    session = core.get_session(session_id).session
    #print(type(session))
    iface1 = iface_helper.create_iface(self.sensor_id, 0)
    iface1 = iface_helper.create_iface(self.relay_id, 0)

    #test = wrappers.Link()
    #session.add_link(node1=node1, node2=node2, iface1=iface1, iface2 = iface2)
    #core.add_link(session_id, node1=node1, node2=node2, iface1=iface1, iface2 = iface2)
    #link = Link(sensor_id, relay_id, LinkType.WIRELESS, 10)
    #result, iface1, iface2 = client.add_link(session_id, link)
    
    
    
    
    
    
    


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
  global iface_helper
  """
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
  """
  # Create grpc client
  iface_helper = client.InterfaceHelper(ip4_prefix="10.0.0.0/24", ip6_prefix="2001::/64")
  core = client.CoreGrpcClient("172.16.0.254:50051")
  core.connect()
  response = core.get_sessions()
  if not response.sessions:
    raise ValueError("no current core sessions")
  session_summary = response.sessions[0]
  session_id = int(session_summary.id)
  print(session_id)
  session = core.get_session(session_id).session
  nodes = core.get_node(session_id,2).node
  print(nodes.position.x)

  # Initialize values
  corepath = "/tmp/pycore.*/"
  nodepath = glob.glob(corepath)[0]
  #msecinterval = float(args.interval)
  #secinterval = msecinterval/1000
  print(type(core.get_session(session_id).session))
  relays = []
  sensors = []
  for i in range(1,71):
    if(i < 10):
      relays.append(relay(i))
    if i == 10:
      sink = sink(i)
    if i > 10:
      sensors.append(sensor(i))
   


if __name__ == '__main__':
  main()
