from agents import study_agent, coding_agent, motivation_agent, summarizer_agent, fun_agent

def ai_pipeline(prompt):

    prompt = prompt.lower()

    if "code" in prompt or "program" in prompt or "python" in prompt:
        return coding_agent(prompt)

    elif "study" in prompt or "explain" in prompt or "learn" in prompt:
        return study_agent(prompt)

    elif "motivate" in prompt or "sad" in prompt or "inspire" in prompt:
        return motivation_agent(prompt)

    elif "summary" in prompt or "summarize" in prompt:
        return summarizer_agent(prompt)

    else:
        return fun_agent(prompt)