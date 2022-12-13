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

## **Receiving form data using Flask**

As I want to make the request action send the data to the same page, you can remove the `action` attribute from the form.

```html
<form class="form" method="POST">
```

### **Setting method types that the main route can handle**

Let's add the `methods` argument to the `@app.route()` decorator and set it to `['GET', 'POST']`.

```python
# [...] Code
@app.route('/', methods=['GET', 'POST'])
# [...] Code
```

#### **Dealing with the POST request**

Let's add the `if` statement to the `index()` function.

```python
# [...] Code
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entry_content = request.form.get('content')
        formatted_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        print(entry_content, formatted_date)
    return render_template('index.html')
```

## **Creating a list of entries**

Let's create a list of entries.

### **Python**

```python
# [...] Code
entries = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        entry_content = request.form.get('content')
        formatted_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        entries.append((entry_content, formatted_date))
    return render_template('index.html', entries)
```

### **HTML**

In the `templates/index.html` file, we are going to use the `for` loop to iterate over the `entries` list. If there are no entries, the `for` loop will not be executed and will be displayed a message.

```html
<!-- [...] Previous Tags -->
  <section class="posts">
    <h1>Recent posts</h1>

    {% if not entries %}
    <p class="posts__empty">No entries yet</p>
    {% else %} {% for entry in entries %}
    <article class="entry">
      <header class="entry__header">
        <h2 class="entry__title">{{ entry[0] | truncate(30, true) }}</h2>
        <time class="entry__date" datetime="2022-12-11"
          >• {{ entry[1] }}</time
        >
      </header>
      <p class="entry__content">{{ entry[0] }}</p>
    </article>
    {% endfor %} {% endif %}
  </section>
<!-- [...] Next Tags -->
```

## **Using MongoDB**

We are going to use `MongoDB` to store the entries, so take a look at the notes that I have created about what is MongoDB and how to set up a database and a cluster database. You can access [clicking here](MONGODB.md).

### **Installing the `pymongo` module**

Let's install the `pymongo` module.

```bash
pip install pymongo[srv]
```

> **Note**
> 
> The `[srv]` part is optional, but it is recommended to use it because it comes with some extra packages that are useful for working with MongoDB Atlas.

### **Configurating the MongoDB connection**

In the `app.py` file, let's import the `MongoClient` class from the `pymongo` module.

```python
# [...] Code
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://<username>:<password>@<cluster-address>/test')
app.db = client.<database-name>
# [...] Code
```

After doing that, inside the function that handles the POST request, let's insert the entry into the database.

```python
# [...] Code
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        entry_content = request.form.get('content')
        formatted_date = datetime.datetime.today().strftime('%Y-%m-%d')
        entries.append((entry_content, formatted_date))
        # The line below is new
        app.db.entries.insert_one(
            {'content': entry_content, 'date': formatted_date}
        )

    entries_with_date = [
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[1], '%Y-%m-%d').strftime('%b %d')
        )
        for entry in entries
    ]
    return render_template('index.html', entries=entries_with_date)
# [...] Code
```

#### **Testing the app**

Restart the app and try to add some entries. After that, go to the MongoDB Atlas dashboard and check if the entries were added to the database.

## **Hiding the MongoDB credentials**

As it's not a good practice to store the MongoDB credentials in the code, let's create a `.env` file and store the credentials there. But first, let's install the `python-dotenv` module.

```bash
pip install python-dotenv
```

### **Creating the `.env` file**

Let's create the `.env` file and store the MongoDB credentials there.

```bash
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-address>/test
```
> **Note**
>
> It's also a good practice to add the `.env` file to the `.gitignore` file and create a `.env.example` file with the same content as the `.env` file but without the credentials.

### **Loading the `.env` file**

Let's load the `.env` file in the `app.py` file, so you need to import `os` and `load_dotenv` from the `dotenv` module, like the example below:

```python
# [...] Code
import os
import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
app = Flask(__name__)

client = MongoClient(os.getenv('MONGODB_URI'))
app.db = client.<database-name>
# [...] Code
```

> **Note**
>
> To get the environment variable, you can use the `os.getenv()` function or the `os.environ.get()` function.

### **Adding the `.env` file to the `.gitignore` file**

Let's add the `.env` file to the `.gitignore` file.

```bash
# [...] Code
.env
# [...] Code
```

## **Retrieving the entries from the database**

Let's retrieve the entries from the database.

### **Python**

```python
# [...] Code
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        entry_content = request.form.get('content')
        formatted_date = datetime.datetime.today().strftime('%Y-%m-%d')
        entries.append((entry_content, formatted_date))
        app.db.entries.insert_one(
            {'content': entry_content, 'date': formatted_date})
    entries_with_date = [
        (
            entry['content'],
            entry['date'],
            datetime.datetime.strptime(entry['date'], '%Y-%m-%d').strftime('%b %d')
        )
        for entry in app.db.entries.find({})
    ]
    return render_template('index.html', entries=entries_with_date)
```

And that's it! Now, the entries are being stored in the database and retrieved from the database, as we have already configured the Jinja template to display the entries, we are done!
