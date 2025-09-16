from flask import Blueprint, render_template, request

notes_bp = Blueprint("notes", __name__)


notes: list[str] = []


@notes_bp.route("/")
def list_notes():
    return render_template("notes.html", notes=notes)


@notes_bp.route("/add", methods=["POST"])
def add_note():
    note_text = request.form.get("note")

    if note_text:
        notes.append(note_text)
    return render_template("notes.html", notes=notes)