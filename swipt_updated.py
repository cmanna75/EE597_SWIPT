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
import random

from core.api.grpc import client, wrappers
from core.api.grpc import core_pb2
from core.api.grpc.wrappers import Position,NodeType
from math import floor



protocol = 'none'
mcastaddr = '235.1.1.1'
port = 9100
ttl = 64
core = None
session_id = None 

filepath = '/tmp'
nodepath = ''

#thrdlock = threading.Lock()

class relay():
  def __init__(self, relay_id,node):
    self.relay_id = relay_id
    self.node = node
    #self.iface = iface_helper.create_iface(relay_id, 0)


  #def harness_solar(self):

  #def calculate_SWIPT(self):

class sensor():
  def __init__(self, sensor_id,node):
    self.sensor_id = sensor_id
    self.node = node
    self.get_closest_relay()
    self.relay_id = self.closest_relay
    self.link_relay()
    #print("id: ",self.sensor_id, " closest relay:",self.relay_id)

  #def harness_swipt(self):

  #def send_data(self):

  #def get_distance(self, relay):

  def get_closest_relay(self):
    x = self.node.position.x
    y = self.node.position.y
    x = math.floor(x/333.33)
    y = math.floor(y/333.33)
    self.closest_relay = x + 1 + 3*y

  def link_relay(self):
    
    node2 = relays[self.closest_relay -1].node
    iface1 = iface_helper.create_iface(self.sensor_id, 0)
    #iface2 = relays[self.closest_relay -1].iface

    #test = wrappers.Link()
    session.add_link(node1=self.node, node2=node2, iface1=iface1)
    #core.add_link(session_id, node1=node1, node2=node2, iface1=iface1, iface2 = iface2)
    #link = Link(sensor_id, relay_id, LinkType.WIRELESS, 10)
    #result, iface1, iface2 = client.add_link(session_id, link)
    
    
    
    
    
    
    


class sink():
  def __init__(self, sink_id,node):
    self.sink_id = sink_id
    self.node = node
    self.link_relays()
  def link_relays(self):
    for i in range(0,9):
      node2 = relays[i].node
      iface1 = iface_helper.create_iface(self.sink_id, i)
      session.add_link(node1=self.node, node2=node2,iface1=iface1)



  
  
#---------------
# main
#---------------
def main():
  global relays
  global sink
  global protocol
  global Sensors
  global core
  global session
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
  core = client.CoreGrpcClient()
  core.connect()
  session = core.create_session()
  
  relays = []
  sensors = []
  
  
  #create relays
  for i in range(1,10):
    x = 166.66 + (i-1)%3 * 333.33
    y = 166.66 + math.floor((i-1)/3) * 333.33
    position = Position(x=x, y=y)
    node = session.add_node(i,model = "mdr",_type = NodeType.WIRELESS, position=position)
    node.icon = "/home/vboxuser/EE597_SWIPT/icons/relay.jpeg"
    node.canvas = 1
    node.name = "relay{}".format(i)
    relays.append(relay(i,node))
    
   #create sink
  position = Position(x=1000,y=1000)
  node = session.add_node(10,model = "router", position = position)
  node.icon = "/home/vboxuser/EE597_SWIPT/icons/sink.jpg"
  node.name = "sink"
  node.canvas = 1
  sink = sink(10,node)
  
  
  
   

   #create wireless sensor nodes
  for i in range(11,71):
    x = random.randint(1,999)
    y = random.randint(1,999)
    position = Position(x=x, y=y)
    node = session.add_node(i,position = position)
    node.icon = "/home/vboxuser/EE597_SWIPT/icons/zebra.jpeg"
    node.canvas = 1
    node.name = "s{}".format(i)
    sensors.append(sensor(i,node))
  
  """
  # Initialize values
  corepath = "/tmp/pycore.*/"
  nodepath = glob.glob(corepath)[0]
  #msecinterval = float(args.interval)
  #secinterval = msecinterval/1000
  print(type(core.get_session(session_id)))
  relays = []
  sensors = []
  for i in range(1,71):
    if(i < 10):
      relays.append(relay(i))
    if i == 10:
      sink = sink(i)
    if i > 10:
      sensors.append(sensor(i))
   
  """
  core.start_session(session)
  
if __name__ == '__main__':
  main()
