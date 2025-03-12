from autogen import ConversableAgent
from config import config_list

result_formatting_agent = ConversableAgent(
    name="ResultFormattingAgent",
    llm_config={"config_list": config_list},
    system_message="Format query results into a structured, human-readable format. Once done output the result and "
                   "terminate with thank you"
)
