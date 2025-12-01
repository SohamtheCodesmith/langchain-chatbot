from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

context = ""

llm = ChatOllama(model="gemma3:4b")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Be funny and nice."),
    ("human", 
     "Conversation so far:\n{context}\n\n"
     "User message:\n{question}")
])

chain = prompt | llm

print("Chatbot ready! Type 'end' to quit.\n")

try:
    while True:
        user_message = input("User: ").strip()
        if user_message.lower() == "end":
            break

        ai_response = ""

        for chunk in chain.stream({"context": context, "question": user_message}):
            print(chunk.content, end='', flush=True)
            ai_response += chunk.content

        print("\n")  # newline

        context += f"User: {user_message}\nAI: {ai_response}\n"

except (KeyboardInterrupt, EOFError):
    print("\nExiting.")