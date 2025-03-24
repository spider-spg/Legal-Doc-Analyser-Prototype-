# Legal-Doc-Analyser-Prototype-
Protoype:

Why do we need a legal document analyser?
--> A legal document analyzer is crucial because legal documents are often lengthy, complex, and filled with technical jargon which upon signing without proper knowledge may cause massive losses.

1) Saves time and effort : Lawyers spend hours reviewing contracts ,Automating this process speeds up analysis for bunch of documents or workload.

2) Cost Efficiency : For direct consumers like us , it will help save us lawyer fees for notice/contract consultation or reviews as it give simplified summary.
   
3) Ideal for Large Document Volumes.

4) Can translate the legal document to multiple languages making it multilingual.. and so on..

How does it work??

--> The Legal Document Analyzer is designed to simplify the complex language often found in legal documents. It automatically scans the text, identifying key details like important clauses, party names, amounts, penalties, and terms and conditions. By highlighting crucial points and generating a clear summary, it helps users quickly grasp the most important aspects of a document. Whether you're reviewing contracts, agreements, or legal notices, this tool makes the process faster, easier, and reduces the chances of missing critical information.


Technologies in use: 

AI/ML:
1.NLP (Natural Language Processing)

Backend : 
1.Fast API 
2.Spacy: An advanced NLP library that efficiently extracts entities like party names, amounts, penalties, and key clauses.

Frontend : 
1. Figma /HTML /CSS / React . 
2. API integration.

Data Handling:
PyPDF2 / pdfplumber / docx
Accept PDFs, Word docs, etc.

Future Plans : 

1.Risk Scoring : will provide risk score out ot 100 points. ..For eg: document is highly risked if it has 1) vague deadline, 2) No info about penalty for delayed payment , 3) missing dispute resolution etc.

2. Using AI to provide recommendations to suggest actionable advice for reducing risk. Eg : add clear deadlines for payment.
   
3. Download reports
   
4.Keyword Searching and filtering : allow users to search specific terms or clauses.

5. Users can ask questions to AI CHATBOT , which will in return give answers from that particular uploaded document.

Screenshots of working prototype:

![image](https://github.com/user-attachments/assets/5f3993b3-84b6-414e-ac69-9fce2473453a)


Starting with FASTAPI command : uvicorn main:app --reload

![image](https://github.com/user-attachments/assets/fda90e87-7ecf-4581-adc3-4f77b624f365)

Go to : http://localhost:8000

![image](https://github.com/user-attachments/assets/ac824c8f-5a80-4bba-b43b-d8e14b01753c)

Upload document  and click on analyse dcoument:

![image](https://github.com/user-attachments/assets/091ed8fc-e417-4b16-a394-86ee793c9a68)

Output: 

![image](https://github.com/user-attachments/assets/1c13e336-cbb9-4a5f-9ee2-1fcb200aa565)

More features is to be added as per written above in "Future Plans".


Video: 

https://github.com/user-attachments/assets/868f74f0-cc41-42e8-b898-d50ac503a8e9


