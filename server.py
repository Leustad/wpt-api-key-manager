from bottle import route, run, request

keys = {}
MAX_USES = 100

def _add_key(key, init=0):
	if key not in keys:
		keys[key] = init

# Initialize keys
_add_key('A.a6eb6013db149f27007da636f21872d8')
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

@route('/key-stats')
def get_key_stats():
	return keys

@route('/use-key/<key>')
def use_key(key):
	count = int(request.query.count or 1)
	keys[key] += count
	return str(keys[key])

@route('/find-key')
def get_usable_key():
	for k,v in keys.iteritems():
		if v < MAX_USES:
			return k
	return ''

run(host='localhost', port=9050)