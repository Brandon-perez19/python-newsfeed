from flask import Flask
from app.routes import home, dashboard

def create_app(test_config=None):
    #set up app config. Serves any static resources from root directory
  app = Flask(__name__, static_url_path='/')
    #sets trailing slashes as optional
  app.url_map.strict_slashes = False
    #sets key when creating server-side sessions
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )

  @app.route('/hello')
  def hello():
    return 'hello world'
#register routes
  app.register_blueprint(home)
  app.register_blueprint(dashboard)
  return app