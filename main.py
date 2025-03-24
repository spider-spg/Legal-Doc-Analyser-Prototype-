from fastapi import FastAPI, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
import spacy
import re

app = FastAPI()


nlp = spacy.load("en_core_web_sm")


templates = Jinja2Templates(directory="templates")


amount_pattern = re.compile(r"\$\d+(?:,\d{3})*(?:\.\d{2})?")
penalty_pattern = re.compile(r"(penalt(y|ies)|fine) .*?\d+", re.IGNORECASE)


@app.get("/")
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze/")
async def analyze_document(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

   
    doc = nlp(text)

    
    clauses = [sent.text for sent in doc.sents if "clause" in sent.text.lower()]
    parties = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "PERSON"]]
    amounts = amount_pattern.findall(text)

    penalties_with_context = []
    for sent in doc.sents:
        if re.search(r"(penalt(y|ies)|fine)", sent.text, re.IGNORECASE):
            penalties_with_context.append(sent.text.strip())

    return {
        "important_clauses": clauses,
        "parties": list(set(parties)),
        "amounts": amounts,
        "penalties_with_context": penalties_with_context
    }
