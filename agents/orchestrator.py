from agents.planner_agent import planner_agent
from agents.executor_agent import executor_agent
from agents.memory import save_memory, load_memory
import ollama


def orchestrator(data):

    # Load memory
    memory = load_memory()

    # Step 1: Planning
    plan = planner_agent(data)

    # Step 2: Execution
    tool_results = executor_agent(plan, data)

    # Step 3: Final reasoning
    prompt = f"""
    You are a master farm AI orchestrator.

    Current Data:
    {data}

    Plan:
    {plan}

    Tool Results:
    {tool_results}

    Memory:
    {memory[-5:]}

    Generate final optimized farm strategy.
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    final_output = response["message"]["content"]

    # Save memory
    save_memory({
        "data": data,
        "plan": plan,
        "result": tool_results
    })

    return final_output