from fastapi import FastAPI
from app.models import Note

# App Instance
app = FastAPI()

# Root URL
@app.get("/")
def read_root():
    return "Scenario 0 - Digital Post IT-Notes"


# Temporary Storage
notes = [] # DB
# Note ID
note_id_counter = 1

# POST (Creating notes)
@app.post("/notes")
def create_note(note: Note):
    global note_id_counter

    new_note = {
        "id": note_id_counter,
        "title": note.title,
        "content": note.content
    }

    notes.append(new_note)
    note_id_counter += 1

    return new_note

# When called, it simply returns the full list of notes stored in memory.
# FastAPI automatically converts the Python list of dictionaries into JSON.
@app.get("/notes")
def get_all_notes():
    return notes


# note_id is captured from the URL path.
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    # We loop through the notes list to find a note with a matching id.
    for note in notes:
        if(note['id'] == note_id):
            return note
    return {"Error": f"Note with the {note_id} not found"}


# Deleting a Note with an ID.
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    # Loops through the notes list to find the note with the matching id.
    for index, note in enumerate(notes):
        if(note['id'] == note_id):
            deleted_note = notes.pop(index)
            return {"message": "Note deleted", "note: ": deleted_note}
    return {"Error: Note Not Found"}