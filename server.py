import random
import socket
from time import gmtime, strftime

from bottle import route, run, request

keys = {}
MAX_USES = 200
PREVIOUS_DATE = strftime("%Y-%m-%d", gmtime())


def _add_key(key, init=0):
    if key not in keys:
        keys[key] = init


# Initialize keys
_add_key('A.f694d68f83cbc0cdd4fb50c443a21f25')
_add_key('A.e376e1273df03d4d29e4d647b33e9964')
_add_key('A.a018e44d8d1ecd38a45e226d228bcf64')
_add_key('A.3c9b23c45c61c645d5455bf86e9a3851')
_add_key('A.d2a7605fb0323cfd6e579ec56baf89b1')
_add_key('A.e1663b7930e0fce0560fb9a8f28340fc')
_add_key('A.f0e8e070b913611ba9bb3fb89ca6214d')
_add_key('A.b04fca72e390276331987d3c8a72dbc3')
_add_key('A.14bd95f981d5acb1205484078622479d')
_add_key('A.a6eb6013db149f27007da636f21872d8')
_add_key('A.047338ae065370eb781df491adb83b72')
_add_key('A.c3948e8dc1dd8c74de31790ca098c758')
_add_key('A.bd9cbaab52af51c42c3210cf58947792')
_add_key('A.549e222e886ede758980da89eccdf1d8')
_add_key('A.b9e760a73f9163c92b8ea5735323d2c8')
_add_key('A.c91ff9ef88a4d64beda0f1764b5abd37')
_add_key('A.7655a05ff1cd654529ef11643d09af03')
_add_key('A.222fa9b451ccd580267b218af227abe8')
_add_key('A.da7cbeca4aa82b14cfaed1b2f8f3b8d3')
_add_key('A.44999e40f3256d8646fff5f627b0cbc5')
_add_key('A.662c075364a5cd4c5215c341ffa837b3')
_add_key('A.95711f9aa3ef3ef6662337231fcfaf8c')
_add_key('A.0bd2755cc3f3f185320a258e26eb89a5')
_add_key('A.90471158f91a4c7e5cc29c788e7bbdc6')
_add_key('A.44ef92f06023053d453d7bbabd2fccaa')


@route('/key-stats')
def get_key_stats():
    return keys


@route('/reset-count')
def reset_count():
    global keys
    print('Reseting Api-Key Count')
    for key, value in keys.items():
        keys[key] = 0
    return keys


@route('/use-key/<key>')
def use_key(key):
    global PREVIOUS_DATE
    current_date = strftime("%Y-%m-%d", gmtime())

    if PREVIOUS_DATE == current_date:
        count = int(request.query.count or 1)
        keys[key] += count
        return str(keys[key])
    else:
        PREVIOUS_DATE = current_date
        reset_count()
        use_key(key)


@route('/find-key')
def get_usable_key():
    rand = random.randint(0, len(keys))

    if keys[list(keys)[rand]] < MAX_USES:
        return list(keys)[rand]
    else:
        get_usable_key()


host = socket.gethostname()
print('Host: ', host)

run(host=host, port=9050)
