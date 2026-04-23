from flask import Flask
from v1 import v1_bp
from v2 import v2_bp

app = Flask(__name__)

# Đăng ký các phiên bản API với prefix tương ứng
app.register_blueprint(v1_bp, url_prefix='/api/v1')
app.register_blueprint(v2_bp, url_prefix='/api/v2')

@app.route('/')
def index():
    return "Payment API - API Versioning Demo"

if __name__ == '__main__':
    app.run(debug=True)