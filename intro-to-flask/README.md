# Creating a Hello World Flask App

> This is a simple Flask app that will be used to demonstrate how to create a Flask app.

## Creating a Virtual Environment

> A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.

To create a virtual environment, run the following command:

```bash
python3 -m venv .venv
```

This will create a folder called `.venv` in the current directory. To activate the virtual environment, run the following command:

### Bash

```bash
source .venv/bin/activate
```

### Windows

```cmd
.venv\Scripts\activate
```

### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

## Installing Flask

To install Flask, run the following command:

```bash
pip install flask
```

## Creating the Flask App

To create the Flask app, create a file called `app.py` and add the following code:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
```

## Running the Flask App

To run the Flask app, you need to set the `FLASK_APP` environment variable to the name of the file containing the Flask app, and also set the `FLASK_DEBUG` environment variable to `1` to enable debug mode. To set the environment variables, run the following commands:

### Bash

```bash
export FLASK_APP=app.py
export FLASK_DEBUG=1
```

### Windows

```cmd
set FLASK_APP=app.py
set FLASK_DEBUG=1
```

### PowerShell

```powershell
$env:FLASK_APP = "app.py"
$env:FLASK_DEBUG = "1"
```

To run the Flask app, run the following command:

```bash
flask run
```

> **Output:**<br>
>  \* Serving Flask app "app.py"<br>
>  \* Debug mode: on<br>
> WARNING: Do not use the development server in a production environment. Use a production WSGI server instead.<br>
>  \* Running on http://127.0.0.1:5000<br>
> Press CTRL+C to quit<br>
>  \* Restarting with stat<br>
>  \* Debugger is active!<br>
>  \* Debugger PIN: 123-456-789<br>

> **Note:**<br>
> In the past, instead of running `FLASK_DEBUG` environment variable, you would have to run `FLASK_ENV=development` environment variable. However, this is no longer required as of Flask 1.0.

## Testing the Flask App

To test the Flask app, open a browser and navigate to `http://127.0.0.1:5000`. You should see the following output:

> Hello, World!

## Creating a fancier Hello World using HTML template system

To create a fancier Hello World, let's create a new route that will render a HTML tag. To do this, add the following code to the `app.py` file:

```python
# [...] Code

@app.route('/fancy')
def fancy_hello_world():
    return """
    <html>
        <body>

            <h1>Greetings!</h1>
            <p>Hello, World!</p>

        </body>
    </html>
    """
```

To test the new route, navigate to `http://127.0.0.1:5000/fancy`.

## Creating a fancier Hello World using render_template method

To create a fancier Hello World using the `render_template` method, let's create a new route that will render a HTML tag. To do this, add the following code to the `app.py` file:

```python
from flask import Flask, render_template
# [...] Code

@app.route('/first_page')
def first_page():
    return render_template('first_page.html')
```

### Creating the HTML template

To create the HTML template, create a folder called `templates` and add a file called `first_page.html` to it. Add the following code to the `first_page.html` file:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>First Page</title>
  </head>
  <body>
    <h1>First Page</h1>
    <p>This is the first page of your static content.</p>
  </body>
</html>
```

> You can also create more pages, in my case I created a `second_page.html` file. So youu have to add the route to the `app.py` file and create the `second_page.html` file in the `templates` folder.

To test the new route, navigate to `http://127.0.0.1:5000/first_page`.

## Using Jinja2 template engine

### What is Jinja2?

Jinja2 is a modern and designer-friendly templating language for Python, modelled after Django’s templates. It is fast, widely used and secure with the optional sandboxed template execution environment. It is an open-source project, BSD licensed.

### Using Jinja2

To use Jinja2, let's reset our `app.py` file to the following code:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

```