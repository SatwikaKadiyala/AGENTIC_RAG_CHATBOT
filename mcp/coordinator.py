from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_agent import LLMResponseAgent

class CoordinatorAgent:
    def __init__(self):
        self.ingestion_agent = IngestionAgent()
        self.retrieval_agent = RetrievalAgent()
        self.llm_agent = LLMResponseAgent()

    def process_query(self, query, uploaded_files):
        chunks = self.ingestion_agent.ingest(uploaded_files)
        relevant_chunks = self.retrieval_agent.retrieve(query, chunks)
        answer = self.llm_agent.generate_response(query, relevant_chunks)
        return answer, relevant_chunks
