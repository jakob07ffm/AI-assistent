import openai
import os


openai.api_key = os.getenv('OPENAI_API_KEY', 'kex')

def format_response(response):
    
    return response.replace('\n', '\n> ')

def ask_question(question):
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        answer = response['choices'][0]['message']['content'].strip()
        return format_response(answer)
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    
    print("Welcome to the ChatGPT Q&A assistant. Type 'exit' or 'quit' to end the session.")
    while True:
        question = input("\nAsk a question: ")
        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        answer = ask_question(question)
        print("\nAnswer:\n> " + answer)

if __name__ == "__main__":
    main()
