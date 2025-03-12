from autogen import ConversableAgent
from config import config_list

sql_agent = ConversableAgent(
    name="SQLAgent",
    llm_config={"config_list": config_list},
    system_message=(
        "Generate an optimized SQL query based on the provided database schema and user query."
    )
)
