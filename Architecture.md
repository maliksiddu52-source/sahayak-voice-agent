# Architecture Document - Sahayak Voice Agent (Telugu Edition)

## 1. System Overview
"Sahayak" is a voice-first, agentic AI system designed to help users identify and apply for government schemes in **Telugu**. It uses a "Listen-Think-Act" loop to process voice commands, query a structured database, and respond naturally.

## 2. Agent Lifecycle & Decision Flow

The agent operates on an autonomous state loop (`src/agent/workflow.py`).
![Agent Lifecycle](/agent_lifecycle.png)

## 3. Core Components

### A. Voice Interface (`src/voice/`)
- **Input (STT)**: Uses `speech_recognition` configured for `te-IN` (Telugu India). Handles ambient noise and connection timeouts.
- **Output (TTS)**: Uses `gTTS` (Google Text-to-Speech) to generate MP3s on the fly, played via `playsound`.
- **Fallback**: Includes a `try-except` block to switch to Text Mode if PyAudio drivers are missing (common on modern Python versions).

### B. Cognitive Layer (`src/agent/brain.py`)
- **Model**: **Google Gemini Pro** (via `google-genai` SDK).
- **Role**: Parses user intent, translates entities (e.g., "Rythu" -> "Farmer"), and decides which tool to call.
- **Reasoning**: Uses a ReAct-like loop (Reason + Act). It can perform up to 5 turns of thinking/tool-calling before answering.

### C. Memory (`src/agent/state.py`)
- **Structure**: A sliding window of conversation history.
- **Format**:
  ```json
  [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "Rythu bandhu schemas?"},
    {"role": "tool", "content": "{...}"},
    {"role": "assistant", "content": "..."}
  ]
  ```
- **Persistence**: Short-term memory is maintained for the session duration.

### D. System Prompts
The **System Prompt** (`src/agent/workflow.py`) governs the agent's behavior. Key directives include:

1.  **Persona**: "You are Sahayak, a helpful Indian government assistant."
2.  **Language Enforcer**: "If user speaks Telugu, reply in Telugu (Script). Do not use English characters."
3.  **Translation Logic**: "The database is in English. You MUST translate user queries (e.g. 'Rythu') to English (e.g. 'Farmer') when callings tools."
4.  **Voice Optimization**: "Keep responses concise."

## 4. Tools & Data (`src/tools/`)
The agent does not hallucinate schemes; it retrieves them from a mock database.

- **`search_schemes(query)`**: Fuzzy search on Scheme Name/Description.
- **`check_eligibility(scheme_id, age, ...)`**: Rule-based engine to validate criteria.
- **`get_scheme_details(id)`**: Fetches full metadata.

## 5. Failure Handling
1.  **STT Failures**: If speech is unclear, it prompts: "Could not understand audio, please try again."
2.  **Search Failures**: If `search_schemes` returns empty, the agent asks for clarifications instead of inventing a scheme.
3.  **Driver Failures**: Automatic degradation to Text Mode ensures the agent remains usable even without audio hardware.
