"""Step 7. Build the agent that ties the LLM and the search tool together"""    

from langchain.agents import create_agent
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def create_hr_agent(llm, tools):    
    """Return a Langchain agent that uses the LLM and the search tool to answer HR policy questions."""
    logger.info("Creating HR agent with %d tools.", len(tools))
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=config.SYSTEM_PROMPT,
    )
    logger.info("Created HR agent.")
    return agent

