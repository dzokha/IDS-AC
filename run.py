import os
from app import create_app
config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, debug = True, port=8181)
