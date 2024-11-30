import streamlit as st
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer, util
import re

@st.cache_resource
def load_model():
    return SentenceTransformer("multi-qa-mpnet-base-dot-v1")

model = load_model()

# Extrai texto de um arquivo PDF
def process_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return safe_decode(text)

# Remove ou ignora caracteres inválidos no texto
def safe_decode(text):
    return text.encode('utf-8', 'ignore').decode('utf-8')

# Divide o texto em sentenças
def segment_text(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [sentence.strip() for sentence in sentences if len(sentence.split()) > 4]  # Ignorar frases muito curtas

# Gera embeddings para o texto
def generate_embeddings(text):
    sentences = segment_text(text)
    embeddings = model.encode(sentences, convert_to_tensor=True)
    return {"sentences": sentences, "embeddings": embeddings}

# Busca os trechos mais relevantes e retorna 3 trechos ordenados por relevância
def query_embeddings(embedding_data, question, top_k=3):
    question_embedding = model.encode(question, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(question_embedding, embedding_data["embeddings"])[0]

    top_results = scores.topk(k=top_k)
    indices = top_results.indices.tolist()
    relevances = [score.item() for score in top_results.values]

    results = []
    for idx, score in zip(indices, relevances):
        sentence = embedding_data["sentences"][idx]
        results.append({"score": score, "sentence": sentence})

    return results[:top_k]

# Interface
st.title("Assistente Conversacional")

uploaded_file = st.file_uploader("Envie um documento", type=("pdf"))

question = st.text_input(
    "Faça uma pergunta sobre o documento",
    placeholder="Qual a definição desse conceito?",
    disabled=not uploaded_file,
)

# Resposta
if uploaded_file and question:
    try:
        if uploaded_file.type == "application/pdf":
            document_text = process_pdf(uploaded_file)
        elif uploaded_file.type == "text/plain":
            document_text = safe_decode(uploaded_file.read().decode())

        embeddings_data = generate_embeddings(document_text)

        with st.spinner("Processando sua pergunta..."):
            top_answers = query_embeddings(embeddings_data, question)

        for i, answer in enumerate(top_answers, start=1):
            st.markdown(f"**Relevância: {answer['score']:.2f}**")
            st.write(answer['sentence'])

    except Exception as e:
        st.error(f"Erro ao processar o documento: {e}")
