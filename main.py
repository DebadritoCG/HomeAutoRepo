# M-1 Using IFTTT API

import requests

def turn_on_light():
    url = "https://maker.ifttt.com/trigger/turn_on_light/with/key/AINT_THAT_DUMB_TO_PROVIDE_U_THE_ACCESS_OF_MY_LIGHTS"
    requests.post(url)

def turn_off_light():
    url = "https://maker.ifttt.com/trigger/turn_off_light/with/key/AINT_THAT_DUMB_TO_PROVIDE_U_THE_ACCESS_OF_MY_LIGHTS"
    requests.post(url)


# M-2 Using TinyTuya Api

# pip install tuya-api
import tinytuya

d = tinytuya.BulbDevice(dev_id='84045520807d3a2888ff', address='OK_NIGG', local_key='GET_URS')
d.set_version(3.1)
d2 = tinytuya.OutletDevice(dev_id='d7ecd706db05186fefcwvv', address='OK_CHICC', local_key='GET_URS')
d2.set_version(3.3)

def set_colour(colour: str):
    if 'white' in colour:
        d.set_colour(255, 0, 255)
    
    elif 'red' in colour:
        d.set_colour(255, 0, 0)
    
    elif 'blue' in colour:
        d.set_colour(0, 0, 255)
    
    elif 'green' in colour:
        d.set_colour(0, 255, 0)
    
    else:
        return None

def turn_on_light_2():
    d.turn_on()

def turn_off_light_2():
    d.turn_off()
