from quart import Quart
from pages.statusCodes import StatusCodes
from pages.testPages import TestPages

app = Quart(__name__)
pages = [StatusCodes, TestPages]

for i in range(0, len(pages)):
	app.register_blueprint(pages[i])

if __name__ == '__main__':
	app.run(debug=True)

#::::: END PROGRAM :::::