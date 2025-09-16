from flask import Flask


from app.home import home_bp
from app.notes import notes_bp


app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(notes_bp, url_prefix="/notes")

if __name__ == "__main__":
    app.run(debug=True)
