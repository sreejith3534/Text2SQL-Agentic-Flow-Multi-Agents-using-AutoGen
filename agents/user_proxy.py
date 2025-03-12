from autogen import ConversableAgent
from config import config_list

user_proxy = ConversableAgent(
    name="Admin",
    code_execution_config=False,
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",
    system_message="Analyze the user query and pass it to SchemaAgent for further processing.",
    is_termination_msg=lambda msg: msg.get("content") and "thank you" in msg["content"].lower().strip(),
)