from autogen import ConversableAgent
from config import config_list

schema_agent = ConversableAgent(
    name="SchemaAgent",
    llm_config={"config_list": config_list},
    system_message=(
        "As a database expert, inspect the database and generate a structured schema. "
        "Call fetch_schema(DB_PATH) to retrieve table names, columns, and their types. "
        "Analyze the user query and determine the relevant tables."
    )
)
