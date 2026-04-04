from tools.irrigation import irrigation_tool
from tools.fertilizer import fertilizer_tool
from tools.pest import pest_control_tool
from tools.environment import temperature_tool


def executor_agent(actions, data):

    results = {}

    if "irrigation" in actions:
        results["irrigation"] = irrigation_tool(
            data["soil_moisture"], data["air_temp"]
        )

    if "fertilizer" in actions:
        results["fertilizer"] = fertilizer_tool(
            data["nitrogen"], data["phosphorus"], data["potassium"], data["soil_ph"]
        )

    if "pest_control" in actions:
        results["pest_control"] = pest_control_tool(data["humidity"])

    if "temperature" in actions:
        results["temperature"] = temperature_tool(data["air_temp"])

    return results