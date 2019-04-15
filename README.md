# Hyper Quart Rest API

This is a starter project to start serving API's with use of the new async/await keywords in Python and make use of ASGI (Asynchronous Server Gateway Interface). Ideally this should lead to performance increases vs. a traditional WSGI-served app, which is common with many Flask/Django setups - [3x faster Flask apps](https://hackernoon.com/3x-faster-than-flask-8e89bfbe8e4f "Hacker Noon")

## Installation
* Clone the repo: `git clone git@github.com:edmundpf/HyperQuartRestApi.git`
* Create the *LOGS* directory for hypercorn log files: `mkdir LOGS`
* Install the python requirements: `python3 -m pip install requirements.txt`

## Flask-to-Quart Migration
* Quart shares the same modules/functions as Flask, so replacing *flask* with *quart* and *Flask* with *Quart* in your imports/any occurences in your code will leave you with a working app.
* Additional changes are needed to take advantage of async calls though, your route functions must make use of the async/await keywords...
  * Flask example:
    ```python
    @app.route('/')
    def route():
      data = request.get_json()
      return render_template_string("Hello {{name}}", name=data['name'])
    ```
  * Quart example:
    ```python
    @app.route('/')
    async def route():
      data = await request.get_json()
      return await render_template_string("Hello {{name}}", name=data['name'])
    ```
  * The following common methods will need the *await* keyword and must be placed in an async function block
    ```python
    await request.data
    await request.get_json()
    await request.form
    await request.files
    await render_template()
    await render_template_string()
    ```
* For more information see the Quart Documentation - [Migration from Flask](https://pgjones.gitlab.io/quart/flask_migration.html "Quart Documentation")

## Deployment
* The app can be served with the command `hypercorn app:app`
* This repo includes an example *DEPLOY* shell script that will require some modifications to use:
  ```bash
  cat > /usr/bin/nonhup
  nohup "$@" </dev/null >/dev/null 2>&1 &
  ^C
  chmod +x /usr/bin/nonhup
  chmod +x DEPLOY
  ```
* Deploy with the command `./DEPLOY`
  * The *nonhup* command that was added is a wrapper for nohup that prevents a command from hanging in the console and also prevents the *nohup.out*   file from being created
* The included deployment script serves the app on *localhost:5000*, automatically reloads after adding/changing files in the app directory, and redirects the error logs to *LOGS/app.log*
* Further customization options for Hypercorn - [Hypercorn Documentation](https://pgjones.gitlab.io/hypercorn/ "Hypercorn")
