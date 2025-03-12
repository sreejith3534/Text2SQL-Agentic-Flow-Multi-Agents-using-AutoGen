from autogen import ConversableAgent
from config import config_list

sql_error_correction_agent = ConversableAgent(
    name="SQLErrorCorrectionAgent",
    llm_config={"config_list": config_list},
    system_message="Correct SQL query errors based on failure messages."
)
