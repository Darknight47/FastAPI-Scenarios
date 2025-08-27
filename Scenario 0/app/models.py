from pydantic import BaseModel
# BaseModel from pydantic, lets FastAPI automatically validate incoming data.

# Note class.
# When we send a POST request to create a note, FastAPI will check that the 'title' and 'content' are both strings and present.
class Note(BaseModel):
    title: str
    content: str