[Source Youtube](https://youtu.be/DId2KP8Ykz4?si=xuQ9Gr8-unz0mVZh)

![Flavours of Rag](./img/image34.png)




1. ### **Challenges in RAG**
   - **Data Quality Issues**
     - Missing or improperly extracted information leading to incorrect or incomplete responses
   - **Chunking Strategy and Embedding Models**
     - Optimal chunking strategies and suitable embedding models tailored to specific domains
   - **Information Retrieval Challenges**
     - Determining document relevance, retrieval window size, and document ordering
     - Relevancy remains an unsolved problem in retrieval systems
   - **Response Generation Challenges**
     - Ensuring coherent and contextually accurate answers
     - Handling ambiguous or vague queries
   - **Scalability and Security**
     - Managing concurrent users
     - Ensuring data security and compliance

![Challenge of Rag](./img/image35.png)

- Data processing
- Data ingestion
- Information retrieval
- Response generation
- Query processing
- Additionnal Others

1. ### **Optimization Techniques for RAG**
   - **Improving Data Quality**
     - Data cleaning and advanced extraction methodologies
     - Using domain-specific embedding models and metadata filtering
   - **Optimizing Chunking Strategies**
     - Reducing chunk size or implementing semantic chunking
   - **Reranking Retrieved Documents**
     - Utilizing different embedding models to rerank and filter out irrelevant documents
   - **Hybrid Search Approaches**
     - Combining dense and sparse vectors to capture domain-specific terminology
     - Integrating ranking models to enhance relevance and faithfulness
   - **Context Size Optimization**
     - Determining appropriate context size to balance information retrieval and noise


![RAG improvment technics](./img/image36.png)

choose Embedding models that comprehense the terminology of our model
Data chunking -> reduce the chunk size or adding semantic chunking
indexing algorithms : hnsw bm25 or even graphs


![Domain Specific eval](./img/image37.png)
Needs evaluation dataset with [Quotient AI](https://www.quotientai.co/post/building-high-quality-rag-applications-with-qdrant-and-quotient) 

![Quotient & Quadrant](./img/image38.png)

The text in the image is:

For the evaluation, we will be considering the following metrics, with a focus on **Faithfulness**:
- Context Relevance
- Chunk Relevance
- Faithfulness
- ROUGE-L
- BERTScore
- BERT Sentence Similarity"