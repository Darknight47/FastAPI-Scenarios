# FastAPI-Scenarios
## Scenario 0
### Digital Post-It Notes
You’ve been asked to build a super simple backend for a web app that lets users create digital sticky notes. Think of it like a minimalist version of Google Keep, no login, no fancy features, just a place to store and retrieve notes.

The frontend team wants to be able to:

1. Create a note
2. Get all notes
3. Get a specific note by ID
4. Delete a note

Storage: Start with in-memory storage (a Python list or dictionary). No database yet — just keep it simple.

---
## Scenario 1
### Sticky Notes with Memory
Your digital post-it notes app was a hit with the frontend team, but now they want it to be more realistic. The biggest issue? Every time the server restarts, all notes vanish. That’s not acceptable anymore.

You’ve been asked to upgrade the backend so that:

1. Notes are stored in a database!
2. Each note has a timestamp for when it was created!
3. The codebase is modular, separating routes, models, and database logic!

Storage: Use SQLite to persist notes!

---
## Scenario 2
### Task Tracker for Freelancers
You’ve been hired by a small freelance platform to build the backend for a task tracking system. Freelancers want to log tasks they’re working on, track their status, and view their progress over time.

The frontend team wants:

1. A clean API to create, update, and retrieve tasks!
2. Status tracking (e.g. pending, in_progress, completed)!
3. Filtering by status or date!
4. Optional due dates!
5. A scalable structure for future features like user accounts or billing!

Storage: Use SQLite

---
## Scenario 3
### SkillSync — A Collaborative Learning Platform
You’ve been hired to build the backend for a platform that helps people learn new skills through structured challenges, peer feedback, and progress tracking. Users can enroll in learning paths, complete challenges, and receive feedback from others in the community. The platform also supports tagging, sorting, and filtering based on difficulty, topic, and completion status.

The system should allow:

1. Users to track their progress across multiple learning paths
2. Challenges to be completed, rated, and commented on
3. Feedback to be stored and retrieved efficiently
4. Filtering and sorting of challenges based on relevance, difficulty, and popularity
5. Pagination for browsing large sets of challenges or feedback entries

The platform is designed to be scalable, with thousands of users and tens of thousands of challenges. Your API must be clean, performant, and intuitive for frontend developers to consume.

**Example Use Cases:**

1. A user wants to browse all challenges tagged with “Python” and sorted by difficulty
2. A mentor wants to view all feedback left on a specific challenge
3. A learner wants to see their progress across multiple learning paths
4. A challenge designer wants to update the difficulty level and description of a challenge
5. A user wants to paginate through feedback entries, 10 per page