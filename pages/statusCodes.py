from quart import Blueprint, jsonify

StatusCodes = Blueprint('StatusCodes', __name__)

#: 400 - Bad Request Error

@StatusCodes.app_errorhandler(400)
async def badRequest(error):
	return jsonify({'status': 'error',
					'message': 'Bad Request'}), 400

#: 401 - Unauthorized Error

@StatusCodes.app_errorhandler(401)
async def unauthorized(error):
	return jsonify({'status': 'error',
					'message': 'Unauthorized'}), 401

#: 403 - Forbidden Error

@StatusCodes.app_errorhandler(403)
async def forbidden(error):
	return jsonify({'status': 'error',
					'message': 'Forbidden'}), 403

#: 404 - Not Found

@StatusCodes.app_errorhandler(404)
async def notFound(error):
	return jsonify({'status': 'error',
					'message': 'Not Found'}), 404

#: 500 - Internal Server Error

@StatusCodes.app_errorhandler(500)
async def serverError(error):
	return jsonify({'status': 'error',
					'message': 'Internal Server Error'}), 500

#::::: END PROGRAM :::::