# memory.py

conversation_memory = []


def add_memory(user_message, assistant_message):

    conversation_memory.append({
        "user": user_message,
        "assistant": assistant_message
    })


def get_memory():

    if len(conversation_memory) == 0:
        return "No previous conversation."

    memory_text = ""

    for chat in conversation_memory:

        memory_text += (
            f"User: {chat['user']}\n"
            f"Assistant: {chat['assistant']}\n"
        )

    return memory_text
