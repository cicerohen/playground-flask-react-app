from flask import Flask, render_template_string
import os

from api.user import user_blueprint;

app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix='/user')


if __name__ == "__main__":
    env = os.environ.get('FLASK_ENV', 'development')
    port = int(os.environ.get('PORT', 9000))
    debug = False and env == 'production' or True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=debug, port=port)
