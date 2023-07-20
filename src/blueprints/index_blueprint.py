from flask import Blueprint, render_template

import os
import json

index_blueprint = Blueprint('index_blueprint', __name__)
entries_dir_path = 'entries'

@index_blueprint.route('/<entry_name>', methods=['GET'])
def entry(entry_name):

    entry_dir = os.path.join(entries_dir_path, entry_name)

    with open(os.path.join(entry_dir, 'text.txt'), 'r') as f:
        text = f.read()

    with open(os.path.join(entry_dir, 'metadata.json'), 'r') as f:
        metadata = json.load(f)
        timestamp = metadata['timestamp']

    entry = {'text': text, 'timestamp': timestamp, 'path': entry_dir}

    return render_template('entry.html', entry=entry)


@index_blueprint.route('/', methods=['GET'])
def index():
    entries = []
    
    for entry_name in os.listdir(entries_dir_path):
        
        entry_dir = os.path.join(entries_dir_path, entry_name)
        
        with open(os.path.join(entry_dir, 'text.txt'), 'r') as f:
            text = f.read()

        with open(os.path.join(entry_dir, 'metadata.json'), 'r') as f:
            metadata = json.load(f)
            timestamp = metadata['timestamp']

        entries.append({'text': text, 'timestamp': timestamp, 'name': entry_name})

    return render_template('index.html', entries=entries)
    