"""
Settings module, reads the settings from a settings.json file. If it does not exist or a new setting
has appeared it will creat from the defaults in the initialise function.
"""
import random
import json
from datetime import datetime

VERSION = '1.5.1'

def initialise():
    """Setup the settings structure with default values"""
    isettings = {'LastSave': '01/01/2000 00:00:01',
                 'api-key': 'change-me',
                 'app-name': 'Oxide Line Laser Controller',
                 'logfilepath': './logs/lasercontroller.log',
                 'logappname': 'Laser-Controller-Py',
                 'loglevel': 'INFO',
                 'gunicornpath': './logs/',
                 'cputemp': '/sys/class/thermal/thermal_zone0/temp',
                 'frequency': 1000,
                 'power': 25,
                 'maxtime': 500,
                 'pyro-laseroff': 'pQCl',  # base64 encoded
                 'pyro-laseron': 'pQGk',  # base64 encoded
                 'pyro-port': '/dev/ttyUSB0',
                 'pyro-speed': 115200,
                 'pyro-readlaser': 'JQ==',  # base64 encoded
                 'pyro-readtemp': 'AQ==',  # base64 encoded
                 'pyro-min-temp': 385,
                 'pyro-running-average': 3,
                 'camera-qty': 2,
                 'camera0': {
                     'cameraID': 0,
                     'cameraFPS': 5,
                     'cameraHeight': 640,
                     'cameraWidth': 480,
                     'cameraBrightness': 128,
                     'cameraContrast': 148,
                     'cameraSaturation': 90,
                     'cameraHue': -40,
                     'cameraGamma': 4,
                     'cameraSharpness': 15,
                     'cameraGain': 0},
                 'camera1': {
                     'cameraID': 2,
                     'cameraFPS': 5,
                     'cameraHeight': 640,
                     'cameraWidth': 480,
                     'cameraBrightness': 64,
                     'cameraContrast': 32,
                     'cameraSaturation': 64,
                     'cameraHue': 0,
                     'cameraGamma': 100,
                     'cameraSharpness': 0,
                     'cameraGain': 50}
                 }
    return isettings



def generate_api_key(key_len):
    """generate a new api key"""
    allowed_characters = "ABCDEFGHJKLMNPQRSTUVWXYZ-+~abcdefghijkmnopqrstuvwxyz123456789"
    return ''.join(random.choice(allowed_characters) for _ in range(key_len))


def writesettings():
    """Write settings to json file"""
    settings['LastSave'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open('settings.json', 'w', encoding='utf-8') as outfile:
        json.dump(settings, outfile, indent=4, sort_keys=True)


def readsettings():
    """Read the json file"""
    try:
        with open('settings.json', 'r', encoding='utf-8') as json_file:
            jsettings = json.load(json_file)
            return jsettings
    except FileNotFoundError:
        print('File not found')
        return {}


def loadsettings():
    """Replace the default settings with thsoe from the json files"""
    global settings
    settingschanged = False
    fsettings = readsettings()
    for item in settings.keys():
        try:
            settings[item] = fsettings[item]
        except KeyError:
            print('settings[%s] Not found in json file using default' % item)
            settingschanged = True
    if settings['api-key'] == 'change-me':
        settings['api-key'] = generate_api_key(128)
        settingschanged = True
    if settingschanged:
        writesettings()


settings = initialise()
loadsettings()
