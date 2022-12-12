# **Making our Microblog with Flask**

## **First set up**

Let's create the folder `templates` and move the `index.html` file into it.

Now we need to create a `static` folder and move the `style.css` file into it. Don't forget about the `images` folder and move the `logo.png` file into it.

## **Configuring the virtual environment**

Let's create a virtual environment for our project. We will use the `venv` module to create the virtual environment.

```bash
python -m venv .venv
```

Now we need to activate the virtual environment.

### **Bash**

```bash
source .venv/Scripts/activate
```

### **Windows**

```cmd
.\.venv\Scripts\activate
```

### **PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

## **Installing Flask**

Let's install the `flask` module.

```bash
pip install flask
```

## **Creating the app**

Let's create the `app.py` file and import the `Flask` class from the `flask` module.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
```

## **Running the app**

Let's run the app.

```bash
flask run
```

> **Note**: You need to set the `FLASK_APP` environment variable to `app.py` before running the app.
>
> ### **Bash**
>
> ```bash
> export FLASK_APP=app.py
> ```
>
> ### **Windows**
>
> ```cmd
> set FLASK_APP=app.py
> ```
>
> ### **PowerShell**
>
> ```powershell
> $env:FLASK_APP = "app.py"
> ```
>
> Don't forget to run the `flask run` command in the folder where the `app.py` file is located.
