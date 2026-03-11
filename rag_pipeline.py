import os
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaLLM  # <-- changed here

VECTOR_PATH = "vector_store/cultural_index"

# Multilingual embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-base"
)

# Initialize Ollama LLM (local)
llm = ChatGroq(
    model="-",
    temperature=0,
    api_key="--"
)  # <-- choose model installed locally

LLM=OllamaLLM(model="mistral",temperature=0)

def load_all_documents():
    texts = []

    # ---------------- TEXT FILES ----------------
    text_files = os.listdir("data/text")
    print("Text files found:", text_files)
    for file in text_files:
        with open(f"data/text/{file}", "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                texts.append(content)

    # ---------------- PDF FILES ----------------
    pdf_files = os.listdir("dataa/pdf")
    print("PDF files found:", pdf_files)
    for file in pdf_files:
        loader = PyPDFLoader(f"dataa/pdf/{file}")
        docs = loader.load()
        for doc in docs:
            if doc.page_content.strip():
                texts.append(doc.page_content)

    # ---------------- AUDIO FILES ----------------
    from audio_processing import transcribe_audio

    audio_files = os.listdir("dataaa/audio")
    print("Audio files found:", audio_files)

    for file in audio_files:
        audio_path = f"dataaa/audio/{file}"
        try:
            transcript = transcribe_audio(audio_path)
            if transcript.strip():
                texts.append(transcript)
        except Exception as e:
            print(f"Error processing audio {file}: {e}")

    print("Total documents loaded:", len(texts))
    return texts



def create_vector_store():

    texts = load_all_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = []
    for text in texts:
        chunks.extend(splitter.split_text(text))

    vectorstore = FAISS.from_texts(chunks, embeddings)
    vectorstore.save_local(VECTOR_PATH)

def load_vector_store():
    # Check if index exists
    if not os.path.exists(f"{VECTOR_PATH}/index.faiss"):
        print("Vector store not found, creating a new one...")
        create_vector_store()
    return FAISS.load_local(VECTOR_PATH, embeddings, allow_dangerous_deserialization=True)


def answer_question(question, language="en"):

    vectorstore = load_vector_store()

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(question)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a Kerala cultural historian AI.
Answer using only the provided cultural memory.
Preserve traditional tone.

Give output strictly in the same language as the question.
Keep and give only meaningfull and accurate and natural output.

Language: {language}

Context:
{context}

Question:
{question}
"""

    # Ollama predict
    if llm is False:
        response = LLM.invoke(prompt)
    else:
        response = llm.invoke(prompt)
    if hasattr(response, "content"):
        response = response.content
    return response
