from groq import Groq

client = Groq(api_key="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")

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Give one motivational quote for students"}
    ],
    model="llama-3.1-8b-instant"
)

print(chat_completion.choices[0].message.content)