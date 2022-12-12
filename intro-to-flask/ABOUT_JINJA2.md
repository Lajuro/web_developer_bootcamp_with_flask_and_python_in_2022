# **More details about Jinja2**

## **Jinja2 Expressions**

Jinja2 expressions are surrounded by double curly braces. For example, `{{ name }}` will be replaced with the value of the `name` variable.

If you want to pass many variables to the template, you can pass them as a dictionary to the `render_template()` function. For example:

```python
@app.route('/')
def hello_world():
    kwargs = {
      'name': 'Roberto',
      'last_name': 'Camargo',
      'age': 26
    }

    return render_template('index.html', **kwargs)
```

## **Jinja2 Data Structures**

Jinja2 Data Structures are used to iterate over lists and dictionaries. For example, if you have a list of names, you can iterate over it using the `for` loop:

### **List Example**

#### **Python**

```python
@app.route('/movies')
def movies():
    movies = [
        'The Shawshank Redemption',
        'The Godfather',
        'The Godfather: Part II',
        'The Dark Knight',
    ]

    return render_template('movies.html', movies=movies)
```

#### **HTML**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Movies</title>
  </head>
  <body>
    <h1>Movies</h1>
    <p>Here are some of my favorite movies:</p>
    <ul>
      <li>{{ movies[0] }}</li>
      <li>{{ movies[1] }}</li>
      <li>{{ movies[2] }}</li>
      <li>{{ movies[3] }}</li>
    </ul>
  </body>
```

### **Dictionary Example**

#### **Python**

```python
@app.route('/car_details')
def car_details():
    car = {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': 1964
    }

    return render_template('car_details.html', car=car)
```

#### **HTML**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Car Details</title>
  </head>
  <body>
    <h1>Car Details</h1>
    <p>Here are some details about my car:</p>
    <ul>
      <li>Brand: {{ car['brand'] }}</li>
      <li>Model: {{ car['model'] }}</li>
      <li>Year: {{ car['year'] }}</li>
    </ul>
  </body>
```

### **Class Example**

#### **Python**

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


@app.route('/car_details')
def car_details():
    car = Car('Ford', 'Mustang', 1964)

    return render_template('car_details.html', car=car)
```

#### **HTML**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Car Details</title>
  </head>
  <body>
    <h1>Car Details</h1>
    <p>Here are some details about my car:</p>
    <ul>
      <li>Brand: {{ car.brand }}</li>
      <li>Model: {{ car.model }}</li>
      <li>Year: {{ car.year }}</li>
    </ul>
  </body>
```

## **Conditionals Statements**

Jinja2 also supports conditional statements. For example, if you want to display a message if the user is logged in, you can do it like this:

### **Python**

```python
@app.route('/profile')
def profile():
    logged_in = True

    return render_template('profile.html', logged_in=logged_in)
```

### **HTML**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Profile</title>
  </head>
  <body>
    <h1>Profile</h1>
    {% if logged_in %}
      <p>You are logged in!</p>
    {% else %}
      <p>You are not logged in!</p>
    {% endif %}
  </body>
</html>
```

### **More Conditionals**

Let's make another scenary, where you want to display a list of frameworks based on the technology selected.

#### **Python**

```python
@app.route('/frameworks')
def frameworks():
    technology = 'python'

    return render_template('frameworks.html', technology=technology)
```

#### **HTML**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Frameworks</title>
  </head>
  <body>
    <h1>Frameworks</h1>
    <p>Here are some frameworks for {{ technology }}:</p>
    <ul>
      {% if technology == 'python' %}
        <li>Django</li>
        <li>Flask</li>
        <li>Pyramid</li>
      {% elif technology == 'javascript' %}
        <li>Angular</li>
        <li>React</li>
        <li>Vue</li>
      {% elif technology == 'ruby' %}
        <li>Ruby on Rails</li>
        <li>Sinatra</li>
      {% else %}
        <li>There are no frameworks for {{ technology }}!</li>
      {% endif %}
    </ul>
  </body>
</html>
```

## **Jinja2 Loops**

Jinja2 also supports loops. For example, if you want to display a list of planets, you can do it like this:

### **Python**

```python
@app.route('/planets')
def planets():
    planets = [
        'Mercury',
        'Venus',
        'Earth',
        'Mars',
        'Jupiter',
        'Saturn',
        'Uranus',
        'Neptune',
    ]

    return render_template('planets.html', planets=planets)
```

### **HTML**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Planets</title>
  </head>
  <body>
    <h1>Planets</h1>
    <p>Here are some planets:</p>
    <ul>
      {% for planet in planets %}
        <li>{{ planet }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

> That's it about Jinja2.