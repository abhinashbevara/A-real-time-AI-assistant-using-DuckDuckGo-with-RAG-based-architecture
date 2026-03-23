from langchain_ollama import OllamaLLM
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


# ✅ Initialize LLM (NEW VERSION)
llm = OllamaLLM(model="llama3:2b")

# ✅ Search tool
search = DuckDuckGoSearchRun()

# ✅ Prompt
prompt = ChatPromptTemplate.from_template(
    """You are a helpful AI assistant. You must answer the user's question 
    based *only* on the following search results. If the search results 
    are empty or do not contain the answer, say 'I could not find 
    any information on that.'

    Search Results:
    {context}

    Question:
    {question}
    """
)

# ✅ Chain (RAG-style)
chain = (
    RunnablePassthrough.assign(
        context=lambda x: search.run(x["question"])
    )
    | prompt
    | llm
)


print("🤖 Hello! I'm a real-time AI assistant. What's new?")

while True:
    try:
        user_query = input("You: ")

        if user_query.lower() in ["exit", "quit"]:
            print("🤖 Goodbye!")
            break

        print("🤖 Thinking...")

        response = chain.invoke({"question": user_query})

        print(f"🤖: {response}")

    except Exception as e:
        print(f"❌ Error: {e}")