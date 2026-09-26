# AI Agent Web Chat

A web-based chat application that allows users to interact with an AI agent through a simple and responsive chat interface.

The application connects a frontend chat interface with a FastAPI backend, an AI agent, and a Groq-hosted Large Language Model (LLM).

## Architecture

```text
User
  |
  v
Web Chat Interface
  |
  v
FastAPI Backend
  |
  v
AI Chat Agent
  |
  v
Groq LLM
  |
  v
AI Response
  |
  v
Web Chat Interface
```

## Features

* Web-based AI chat interface
* FastAPI backend
* Groq LLM integration
* AI agent abstraction
* Conversation memory
* Multiple conversation sessions
* New conversation functionality
* REST API
* Responsive frontend
* Environment-based API key configuration
* CORS support

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI
* Uvicorn

### AI

* Groq API
* Large Language Model (LLM)

### Other

* python-dotenv
* REST API
* In-memory conversation history

## Project Structure

```text
AI-Agent-Web-Chat/
|
├── backend/
│   ├── main.py
│   └── agent.py
|
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
|
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## How It Works

1. The user enters a message in the web interface.
2. JavaScript sends the message to the FastAPI backend.
3. FastAPI passes the message to the AI agent.
4. The AI agent sends the conversation history and the new message to the Groq LLM.
5. The LLM generates a response.
6. The backend returns the response as JSON.
7. The frontend displays the AI response in the chat interface.

## Conversation Memory

The application maintains conversation history using a conversation ID.

For example:

```text
User:
My name is Abdelrahman.

AI:
Nice to meet you, Abdelrahman!

User:
What is my name?

AI:
Your name is Abdelrahman.
```

Each conversation can have its own conversation ID.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AbdelrhmanAkl/AI-Agent-Web-Chat.git
cd AI-Agent-Web-Chat
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-20b
```

Do not share or commit your real API key.

## Running the Backend

From the project root:

```bash
uvicorn backend.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

## Running the Frontend

Open another terminal and run:

```bash
cd frontend
python -m http.server 5500
```

Then open:

```text
http://127.0.0.1:5500
```

## API Endpoints

### Health Check

```text
GET /health
```

Returns:

```json
{
  "status": "healthy"
}
```

### Chat

```text
POST /chat
```

Example request:

```json
{
  "message": "Hello",
  "conversation_id": "default"
}
```

Example response:

```json
{
  "response": "Hello! How can I help you?",
  "conversation_id": "default"
}
```

### Clear Conversation

```text
DELETE /chat/{conversation_id}
```

Clears the conversation history for the specified conversation.

## Security

The Groq API key is stored in an environment variable and is excluded from Git using `.gitignore`.

Never commit the `.env` file or expose your API key publicly.

## Future Improvements

Possible future improvements include:

* Persistent database-based conversation history
* User authentication
* Streaming responses
* Retrieval-Augmented Generation (RAG)
* Tool calling
* File upload and document processing
* Conversation history UI
* Deployment to a cloud platform
* Automated testing
* Logging and monitoring

## Project Status

Completed as a functional AI Agent Web Chat application demonstrating frontend-backend integration, LLM integration, REST APIs, and conversation memory.
