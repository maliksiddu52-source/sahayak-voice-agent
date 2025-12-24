# Sahayak - Government Scheme Agent (Telugu Edition)

A voice-first AI agent that helps Indian citizens discover and apply for government schemes in **Telugu**.

## Features
- **Voice-First Interaction (Telugu)**: Speak to the agent in Telugu (`te-IN`). The agent responds in Telugu.
- **Agentic Workflow**: The agent plans, calls tools, and reasons about eligibility using the **Google Gemini Pro** model.
- **Mock Database**: Includes PM Kisan, Ayushman Bharat, and more.
- **Robust Error Handling**:
    - Automatic **Text Mode Fallback** if microphone/audio drivers fail.
    - Handles voice timeouts.

## Prerequisites
- Python 3.9+ (Python 3.14 users may experience PyAudio issues, forcing Text Mode).
- **Google Gemini API Key**.

## setup (Detailed)

### 1. Create Virtual Environment (Recommended)
You should use a clean virtual environment (Python 3.10 is stable for audio drivers).

**Windows (PowerShell):**
```powershell
# Create venv
python 3.10 -m venv venv

# Activate venv
.\venv\Scripts\activate
```

### 2. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## Usage

Run the main script:
```bash
python main.py
```

### Modes of Operation
1.  **Voice Mode (Default)**:
    - Agent greets: *"నమస్కారం! నేను సహాయక్..."* (in Telugu script).
    - You speak: *"Rythu bandhu pathakam gurinchi cheppandi"* (Tell me about farmer schemes).
    - Agent speaks back.

2.  **Text Fallback Mode**:
    - If your audio drivers fail, the system prints: `[System]: Audio Error. Switching to Text Input.`
    - You can type your query in English or Telugu characters.
    - The agent will print the response.

## Evaluation Transcript

For a detailed record of successful interactions, failure handling, and edge cases, please refer to the [Evaluation Transcript](evaluation_transcript.md).

## Project Structure
- `src/agent/`: Core logic (Brain uses `google-genai`).
- `src/tools/`: Mock database (English) and API functions.
- `src/voice/`: STT and TTS handling (configured for `te-IN`).
- `main.py`: Entry point.
