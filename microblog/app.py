import os
import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = MongoClient(os.getenv('MONGODB_URI'))
app.db = client.microblog

entries = []


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
            datetime.datetime.strptime(
                entry['date'], '%Y-%m-%d').strftime('%b %d')
        )
        for entry in app.db.entries.find({})
    ]
    return render_template('index.html', entries=entries_with_date)
