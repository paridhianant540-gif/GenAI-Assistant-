# Imports
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import numpy as np
import json
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os
from sentence_transformers import SentenceTransformer

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load local embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text):
    return embed_model.encode(text)

# Load documents
with open("docs.json") as f:
    docs = json.load(f)

doc_texts = [doc["content"] for doc in docs]
doc_embeddings = np.array([generate_embedding(text) for text in doc_texts])

# Retrieval function (Top 3)
def retrieve_context(query):
    query_embedding = generate_embedding(query)
    similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
    top_indices = similarities.argsort()[-3:][::-1]
    contexts = [doc_texts[i] for i in top_indices]
    return "\n\n".join(contexts)

# Chat memory
chat_history = {}

# Generate answer
def generate_answer(context, question, history):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
You are a helpful AI assistant.

Use the context if it contains the answer.
If the context does not contain the answer, answer with your general knowledge.

Context:
{context}

Conversation History:
{history}

User Question:
{question}
"""
    try:
        response = model.generate_content(
            prompt,
            generation_config={"temperature": 0.2, "max_output_tokens": 200}
        )
        return response.text if hasattr(response, "text") else "No response generated."
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while generating the response."

# Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message")
    session_id = data.get("sessionId")

    if not message:
        return jsonify({"reply": "Please enter a message."})

    # Retrieve context
    context = retrieve_context(message)

    # Get chat history
    history = chat_history.get(session_id, [])
    history_text = "\n".join(history[-6:])

    # Generate response
    reply = generate_answer(context, message, history_text)

    # Store conversation history
    history.append(f"User: {message}")
    history.append(f"Assistant: {reply}")
    chat_history[session_id] = history

    return jsonify({"reply": reply, "retrievedChunks": 3})

# Run server
if __name__ == "__main__":
    app.run(debug=True)