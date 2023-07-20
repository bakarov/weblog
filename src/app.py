import os

from flask import Flask
from flaskext.markdown import Markdown

from blueprints.index_blueprint import index_blueprint


if __name__ == '__main__':

    app = Flask(__name__)
    app.register_blueprint(index_blueprint)
    Markdown(app)

    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
