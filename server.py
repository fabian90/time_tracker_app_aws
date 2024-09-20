from flask import render_template
from app import create_app
# Crear la aplicación
app = create_app()

@app.route('/')
def home():
    return render_template("activities.html")

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == "__main__":    
    host = "172.31.35.172"
    port = 80
    app.run(host, port, True)

