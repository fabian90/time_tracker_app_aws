from flask import Flask,render_template
from app import create_app
# Crear la aplicación
app = create_app()
# app = Flask(__name__)
@app.route('/')
def home():
    return render_template("activities.html")

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == "__main__":    
    host = "0.0.0.0"
    port = 5000
    app.run(host, port, True)

