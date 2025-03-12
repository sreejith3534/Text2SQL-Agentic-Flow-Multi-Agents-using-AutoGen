from autogen_setup import start_chat

if __name__ == "__main__":
    user_query = input("Enter your SQL-related query: ")
    chat_result = start_chat(user_query)
    print(chat_result)
