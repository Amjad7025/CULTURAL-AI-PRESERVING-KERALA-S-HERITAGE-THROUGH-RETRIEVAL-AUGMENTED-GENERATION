# app.py

# from flask import Flask, request, jsonify, render_template
# from rag_pipeline import answer_question, create_vector_store
# from audio_processing import transcribe_audio
# from translation import detect_language
# from tts import text_to_speech
# import os
# import asyncio
# import edge_tts

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("indexx.html")


# @app.route("/build_index", methods=["POST"])
# def build_index():
#     create_vector_store()
#     return jsonify({"message": "Vector store created successfully"})


# @app.route("/ask", methods=["POST"])
# def ask():

#     if "audio" in request.files:
#         audio = request.files["audio"]
#         path = "dataaa/audio/temp.wav"
#         audio.save(path)
#         question = transcribe_audio(path)
#         selected_language = request.form.get("language", "en")

#     else:
#         data = request.get_json()
#         question = data.get("question")
#         selected_language = data.get("language", "en")

#     answer = answer_question(question)

#     audio_file = text_to_speech(answer, lang=selected_language)

#     return jsonify({
#         "question": question,
#         "language": selected_language,
#         "answer": answer,
#         "audio": audio_file
#     })
# app.py

from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from rag_pipeline import answer_question, create_vector_store
from audio_processing import transcribe_audio
from tts import text_to_speech
import os

app = Flask(__name__)
app.secret_key = "kerala_cultural_secret_key"  # Needed for login session


# ---------------- LOGIN SYSTEM ----------------

USERNAME = "admin"
PASSWORD = "1234"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect(url_for("loading"))
        else:
            return render_template("indexx.html", error="Invalid Credentials")

    return render_template("indexx.html")


@app.route("/loading")
def loading():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("indexx.html")


@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("indexx.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# ---------------- BUILD INDEX ----------------

@app.route("/build_index", methods=["POST"])
def build_index():
    create_vector_store()
    return jsonify({"message": "Vector store created successfully"})


# ---------------- ASK QUESTION ----------------

@app.route("/ask", methods=["POST"])
def ask():

    if "audio" in request.files:
        audio = request.files["audio"]
        path = "dataaa/audio/temp.wav"
        audio.save(path)
        question = transcribe_audio(path)
        selected_language = request.form.get("language", "en")

    else:
        data = request.get_json()
        question = data.get("question")
        selected_language = data.get("language", "en")

    answer = answer_question(question, selected_language)

    audio_file = text_to_speech(answer, lang=selected_language)

    return jsonify({
        "question": question,
        "language": selected_language,
        "answer": answer,
        "audio": audio_file
    })


if __name__ == "__main__":
    app.run(debug=True)


# if __name__ == "__main__":
#     app.run(debug=True)

