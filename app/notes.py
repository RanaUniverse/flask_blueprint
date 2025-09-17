from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
)

notes_bp = Blueprint("notes", __name__)


notes: list[str] = []


@notes_bp.route("/")
def list_notes():
    return render_template(
        "notes.html",
        notes=notes,
    )


# This will shows a form to take new note
@notes_bp.get("/add")
def show_note_list():
    return render_template(
        "add_notes.html",
    )


# This will take the data from user and then it will redirect to user
# so that the refresh will not say any issue
@notes_bp.post("/add")
def process_add_note():
    note_text = request.form.get("note")

    if note_text:
        notes.append(note_text)

    return redirect(url_for("notes.list_notes"))
