import time
import random
from agents.orchestrator import orchestrator
from tools.weather import get_weather


def get_sensor_data():

    weather = get_weather()

    return {
        "crop": "Wheat",
        "soil_moisture": random.randint(20, 60),
        "soil_temp": random.randint(20, 35),
        "air_temp": weather["air_temp"],
        "humidity": random.randint(30, 90),
        "soil_ph": round(random.uniform(5.5, 7.5), 1),
        "nitrogen": random.randint(30, 80),
        "phosphorus": random.randint(20, 50),
        "potassium": random.randint(20, 50)
    }


if __name__ == "__main__":

    while True:

        print("\n==============================")

        data = get_sensor_data()
        print("📡 INPUT:", data)

        result = orchestrator(data)

        print("\n🌱 FINAL DECISION:\n")
        print(result)

        time.sleep(10)