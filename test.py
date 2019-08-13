#!/usr/bin/env python3
"""
Test the pybinarymoip module for controlling SnapAV(tm) Binary(tm)-brand
Media Over IP systems.

Before execution, set the following environment variables:

MOIP_HOSTNAME - host or ip address of a wattbox device
MOIP_USERNAME - login username for that device
MOIP_PASSWORD - password for that user

"""

import logging
import json
from os import environ
from pybinarymoip import MoIP

_LOGGER = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

m = MoIP(environ['MOIP_HOSTNAME'],
         environ['MOIP_USERNAME'],
         environ['MOIP_PASSWORD'])
m.connect()
m.receivers[1].set_resolution(3)
m.receivers[1].switch_to_tx(m.transmitters[0])
print(m.transmitters)
print(m.receivers)


#print(json.dumps(m.transmitters[0]))
#print(json.dumps(m.receivers[0]))
#print(json.dumps(m))
