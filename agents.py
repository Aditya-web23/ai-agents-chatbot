from groq import Groq

client = Groq(api_key="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")


# Study AI Agent
def study_agent(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": "Explain this topic simply for students: " + prompt}
        ],
        model="llama-3.1-8b-instant"
    )
    return response.choices[0].message.content


# Coding AI Agent
def coding_agent(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": "Help with programming problem: " + prompt}
        ],
        model="llama-3.1-8b-instant"
    )
    return response.choices[0].message.content


# Motivation AI Agent
def motivation_agent(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": "Give motivation about: " + prompt}
        ],
        model="llama-3.1-8b-instant"
    )
    return response.choices[0].message.content


# Summarizer AI Agent
def summarizer_agent(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": "Summarize this text: " + prompt}
        ],
        model="llama-3.1-8b-instant"
    )
    return response.choices[0].message.content


# Fun AI Agent
def fun_agent(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": "Tell something fun or interesting about: " + prompt}
        ],
        model="llama-3.1-8b-instant"
    )
    return response.choices[0].message.content