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

The platform is designed to be scalable, with thousands of users and tens of thousands of challenges. Your API must be clean, performant, and intuitive for frontend developers to consume.

**Example Use Cases:**

1. A user wants to browse all challenges tagged with “Python” and sorted by difficulty
2. A learner wants to see their progress across multiple learning paths
3. A challenge designer wants to update the difficulty level and description of a challenge

---
## Scenario 4 🧑‍💼🧮📎
### Collaborative Project Management Platform
You’ve been hired to build the backend for a collaborative project management tool used by remote software teams.

The platform allows teams to manage projects, assign tasks, track progress, and collaborate in real time. Users can belong to multiple teams. 
Each team has multiple projects, and each project contains tasks. Tasks can be assigned to users, updated with status changes (e.g. todo, in_progress, done), and commented on.

#### Key features include:

**Team Management**
1. Users can join or leave teams
2. Each team has admins who can manage projects and members

**Project & Task Management**
1. Projects belong to teams
2. Tasks belong to projects and are assigned to users
3. Tasks have statuses, priorities, and due dates
4. Comments on tasks for collaboration

**Activity Logs**
1. Every key action (e.g., task assignment, status change, comment) is logged with a timestamp

**Filtering & Sorting**
1. Tasks should be filterable by assignee, status, priority, due date, etc.
2. Sorting options for project views

**Scalability Focus**
1. The system is expected to support large distributed teams (1000+ users, 10,000+ tasks per team)

---
## Scenario 5 🍟🍳👨‍🍳
### “Chef’s Companion” — A Smart Recipe Generator for Home Cooks
You’ve been hired to build the backend for Chef’s Companion, a web-based platform that helps users discover and generate recipes based on what they have in their fridge. The platform is designed to be intuitive, personalized, and scalable, supporting thousands of users and a growing library of ingredients, dietary preferences, and recipe templates.

#### Core Concept
Users log in to a visual fridge interface where they see a randomized selection of food items. They can select ingredients they currently have, and the system will generate a recipe using those items. Recipes are generated using a custom NLP model trained on real-world cooking data.

#### 🧪 Example Use Cases
1. A user selects “tomato”, “onion”, and “spinach” and wants a vegan recipe under 30 minutes.
2. A user wants to regenerate a recipe using the same ingredients but with a different cuisine style.
3. A user wants to browse all saved recipes tagged “gluten-free” and sorted by prep time.
4. A user wants to see the step-by-step instructions for a previously generated recipe.
5. A user wants to update their dietary preferences and regenerate recipes accordingly.