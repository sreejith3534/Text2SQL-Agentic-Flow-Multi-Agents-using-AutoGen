from autogen import GroupChat, GroupChatManager, register_function
from agents.user_proxy import user_proxy
from agents.schema_agent import schema_agent
from agents.sql_agent import sql_agent
from agents.validation_agent import validation_agent
from agents.sql_error_correction import sql_error_correction_agent
from agents.result_formatting import result_formatting_agent
from utils.db_utils import fetch_schema, validate_and_execute_sql_query
from config import config_list

# Register functions
register_function(fetch_schema, caller=schema_agent, executor=schema_agent, name="FetchingSchema")
register_function(validate_and_execute_sql_query, caller=sql_agent, executor=validation_agent, name="ValidateSQL")

# Define Group Chat
groupchat = GroupChat(
    agents=[user_proxy, schema_agent, sql_agent, validation_agent, sql_error_correction_agent, result_formatting_agent],
    messages=[],
    max_round=5,
    allowed_or_disallowed_speaker_transitions={
        user_proxy: [schema_agent, sql_agent, validation_agent, sql_error_correction_agent, result_formatting_agent],
        schema_agent: [user_proxy, sql_agent],
        sql_agent: [user_proxy, validation_agent],
        validation_agent: [sql_error_correction_agent, result_formatting_agent],
        sql_error_correction_agent: [user_proxy, validation_agent],
        result_formatting_agent: [user_proxy]
    },
    speaker_transitions_type="allowed",
)

# Define Manager
manager = GroupChatManager(groupchat=groupchat, llm_config={"config_list": config_list})


# Function to start the chat
def start_chat(user_query: str):
    return user_proxy.initiate_chat(manager, max_turns=3, message=f"Analyze the user query: {user_query}")
