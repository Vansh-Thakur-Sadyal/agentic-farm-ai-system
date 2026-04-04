import ollama


def planner_agent(data):

    prompt = f"""
    You are a planning agent.

    Based on the following farm data:
    {data}

    Decide what actions are needed.

    Choose from:
    - irrigation
    - fertilizer
    - pest_control
    - temperature

    Return ONLY a Python list.

    Example:
    ["irrigation", "fertilizer"]
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]