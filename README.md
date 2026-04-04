# 🌱 Agentic Farm AI System

## 🚀 Overview

This project is a *multi-agent, autonomous AI system* designed to generate intelligent farm action plans using real-time data, tool-based reasoning, and local large language models (LLMs).

Unlike traditional machine learning models or static scripts, this system follows a *true Agentic AI architecture*, where multiple specialized agents collaborate to make decisions.

---

## 🧠 What Makes This “Agentic AI”?

This system is not just a model—it is an *intelligent decision-making ecosystem*.

It includes:

* ✅ Planning agent (decides what actions to take)
* ✅ Execution agent (runs domain-specific tools)
* ✅ Orchestrator (controls full workflow)
* ✅ Memory system (stores past decisions)
* ✅ Real-world data integration (weather API)
* ✅ Autonomous loop (continuous operation)

---

## 🏗️ Architecture


User / Sensor Input
        ↓
Orchestrator Agent (Brain)
        ↓
 ┌───────────────┬───────────────┬───────────────┐
 ↓               ↓               ↓
Planner Agent   Executor Agent   Memory Agent
 ↓               ↓               ↓
Decision        Tools           Past Data
 ↓
Final LLM Reasoning (Ollama)
 ↓
Farm Action Plan


---

## ⚙️ Tech Stack

### 🧠 AI / LLM

* *Ollama (Local LLM)*
* Model: llama3
* Runs locally with GPU acceleration

### 🧩 Backend / Logic

* Python 3.10+
* Modular architecture (agents + tools)

### 🌐 External APIs

* *Open-Meteo API* (real-time weather data)

### 💾 Memory

* JSON-based persistent storage (memory.json)

### 🧪 Environment

* Virtual Environment (venv)
* VS Code

---

## 📁 Project Structure


agentic-farm-ai/
│
├── agents/
│   ├── planner_agent.py
│   ├── executor_agent.py
│   ├── orchestrator.py
│   ├── memory.py
│   └── __init__.py
│
├── tools/
│   ├── irrigation.py
│   ├── fertilizer.py
│   ├── pest.py
│   ├── environment.py
│   ├── weather.py
│   └── __init__.py
│
├── main.py
├── memory.json
└── README.md


---

## 🔍 System Capabilities

### 🌾 1. Smart Farm Planning

Generates structured plans including:

* Irrigation strategy
* Fertilization recommendations
* Pest control measures
* Environmental adjustments

---

### 🧠 2. Multi-Agent Decision Making

* Planner decides required actions
* Executor runs tools
* Orchestrator combines everything

---

### 🔧 3. Tool-Based Reasoning

Custom tools for:

* Irrigation logic
* Soil nutrient analysis
* Pest risk detection
* Temperature stress handling

---

### 🌐 4. Real-Time Data Integration

* Fetches live weather data
* Combines with simulated sensor data

---

### 💾 5. Memory System

* Stores past decisions
* Enables context-aware reasoning

---

### 🔄 6. Autonomous Operation

* Runs continuously
* Adapts decisions every cycle
* Simulates real IoT farming system

---

## ▶️ How to Run

### 1. Activate environment

bash
venv\Scripts\activate


### 2. Install dependencies

bash
pip install requests


### 3. Start Ollama

bash
ollama run llama3


### 4. Run system

bash
python main.py


---

## 📊 Example Output


📡 INPUT: {sensor data}

🧠 Planner: ['irrigation', 'fertilizer']

🔧 Tools: {tool outputs}

🌱 FINAL DECISION:
Structured farm plan with recommendations...


---

## 🧠 Intelligence Level

This system demonstrates:

| Capability             | Status |
| ---------------------- | ------ |
| Static ML Model        | ❌      |
| Prompt-based AI        | ❌      |
| Tool-using Agent       | ✅      |
| Multi-Agent System     | ✅      |
| Autonomous AI          | ✅      |
| Real-world integration | ✅      |

---

## 🚀 Real-World Potential

This system can evolve into:

* Smart agriculture platforms
* IoT farm monitoring systems
* Precision agriculture tools
* Autonomous decision engines
* AI-based advisory systems

---

## 🔮 Future Improvements

* 🌐 FastAPI backend (serve as API)
* 📊 Dashboard UI (React)
* 🧠 Vector memory (long-term learning)
* 🤖 Multi-agent communication
* ☁️ Cloud deployment

---

## 🏆 Summary

This project is a:

> *Multi-agent autonomous AI system with orchestration, memory, tool usage, and real-time data integration using local LLMs.*

It represents a transition from:

* ❌ traditional ML
* ❌ simple AI scripts

to:

> 💥 *Agentic AI Systems Engineering*

---

## 👨‍💻 Author

Built as an advanced AI systems project demonstrating real-world agentic architecture.

---

## ⭐ If you like this project

Give it a star ⭐ and explore further improvements!
