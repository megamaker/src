#!/usr/bin/env python
#encoding=utf-8

from bottle import run, get, post, request


meta = '<meta name="viewport" content="width=device-width,initial-scale=2.0,user-scalable=no">'

form = '''
<form action="/motor" method="post">
<table>
	<tr>
		<td>
			<button type="submit" name="direction" value="F">F</button>
		</td>
		<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
		<td>
			<button type="submit" name="speed" value="3">3</button>
		</td>
	<tr>
	<tr>
		<td>
			<button type="submit" name="direction" value="S">S</button>
		</td>
		<td></td>
		<td>
			<button type="submit" name="speed" value="2">2</button>
		</td>
	</tr>
	<tr>
		<td>
			<button type="submit" name="direction" value="B">B</button>
		</td>
		<td></td>
		<td>
			<button type="submit" name="speed" value="1">1</button>
		</td>
	</tr>
</table>
</form>
'''
html = '<head>%s</head>%s' % (meta, form)

@get('/motor')
def blink():
	return html

@post('/motor')
def do_blink():
	direction = request.forms.get('direction')
	speed = request.forms.get('speed')
	if direction: print direction
	if speed: print speed

	return html

run(host='192.168.10.1', port=8080, debug=True)
