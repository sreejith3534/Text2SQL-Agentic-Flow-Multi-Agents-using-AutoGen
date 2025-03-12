from autogen import ConversableAgent
from config import config_list

validation_agent = ConversableAgent(
    name="ValidationAgent",
    llm_config={"config_list": config_list},
    system_message="Validate SQL query correctness using validate_and_execute_sql_query."
)
