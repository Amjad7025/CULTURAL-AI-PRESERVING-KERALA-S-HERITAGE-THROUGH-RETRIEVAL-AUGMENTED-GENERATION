import os
import uuid
import asyncio
import edge_tts

def text_to_speech(text, lang="en"):

    if not os.path.exists("static"):
        os.makedirs("static")

    filename = f"response_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join("static", filename)

    # Voice mapping
    voice_map = {
        "ml": "ml-IN-SobhanaNeural",
        "en": "en-IN-NeerjaNeural",
        "hi": "hi-IN-SwaraNeural",
        "ta": "ta-IN-PallaviNeural",
        "sa": "hi-IN-SwaraNeural"   # Sanskrit fallback (Hindi voice)
    }

    voice = voice_map.get(lang, "en-IN-NeerjaNeural")

    async def generate():
        communicate = edge_tts.Communicate(text, voice=voice)
        await communicate.save(filepath)

    asyncio.run(generate())

    return f"/static/{filename}"
# import os
# import uuid
# import asyncio
# import edge_tts

# async def get_voice_for_lang(lang_code: str):
#     """
#     Find the first available voice for a given language code (e.g., 'en', 'hi', 'ml').
#     Falls back to English if no match is found.
#     """
#     voices = await edge_tts.list_voices()
#     # Try exact locale match (like 'hi-IN')
#     for v in voices:
#         if v["Locale"].lower().startswith(lang_code.lower()):
#             return v["ShortName"]

#     # Fallback: English voice
#     for v in voices:
#         if v["Locale"].lower().startswith("en"):
#             return v["ShortName"]

#     return "en-IN-NeerjaNeural"  # final fallback


# def text_to_speech(text, lang="en"):
#     if not os.path.exists("static"):
#         os.makedirs("static")

#     filename = f"response_{uuid.uuid4().hex}.mp3"
#     filepath = os.path.join("static", filename)

#     async def generate():
#         voice = await get_voice_for_lang(lang)
#         communicate = edge_tts.Communicate(text, voice=voice)
#         await communicate.save(filepath)

#     asyncio.run(generate())

#     return f"/static/{filename}"