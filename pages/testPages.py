from quart import Blueprint, jsonify, request, abort

TestPages = Blueprint('TestPages', __name__)

#: Index

@TestPages.route('/')
async def index():
	return jsonify({'status': 'ok',
					'message': 'Request Completed'})

#: Hello World Page

@TestPages.route('/hello')
async def hello():
	return jsonify({'status': 'ok',
					'message': 'Hello World'})

#: Error

@TestPages.route('/error')
async def error():
	try:
		code = int(request.args.get('code', 400))
	except:
		await abort(400)
	await abort(code)

#::::: END PROGRAM :::::