from flask import Flask
from src.main.routes.routes import cliente_route_bp, contato_route_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(cliente_route_bp)
app.register_blueprint(contato_route_bp)
