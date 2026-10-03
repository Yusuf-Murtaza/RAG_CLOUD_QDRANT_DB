"""Step 5. Wrap the retriever as a tool the agent can call"""

from langchain.tools import tool
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def create_search_tool(retriever):
    """Return a @tool function that searches the HR policy documents"""
    @tool
    def search_hr_policy(question: str) -> str:
        """Search HR policy documents for a specific question related to leave, work from home, 
        probation, notice period, reimbursement, code of conduct, holidays, or exit process."""
        logger.info(f"Searching HR policy for question: {question}")
        matching_chunks = retriever.invoke(question)
        logger.info(f"Found {len(matching_chunks)} matching chunks for question: {question}")
        return "\n\n".join([chunk.page_content for chunk in matching_chunks])

    return search_hr_policy



