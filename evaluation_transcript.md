# Evaluation Transcript - Sahayak Voice Agent

This document records the evaluation of the Sahayak Agent, featuring successful flows, handled failures, and edge cases.

## 1. Successful Interaction (Happy Path)
**Scenario**: User asks for farmer schemes and checks eligibility.

> **Agent**: నమస్కారం! నేను సహాయక్. నేను మీకు ప్రభుత్వ పథకాల గురించి సహాయం చేయగలను...
>
> **User (Audio)**: "రైతులకు ఏమైనా పథకాలు ఉన్నాయా?" (Are there any schemes for farmers?)
>
> **Agent (Thought)**: User asking for 'Farmers'. Calling `search_schemes('farmer')`.
> **Tool Output**: Found 'Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)'.
>
> **Agent (Voice)**: "అవును, రైతుల కోసం 'ప్రధాన మంత్రి కిసాన్ సమ్మాన్ నిధి' (PM-KISAN) పథకం ఉంది. దీని ద్వారా రైతులకు ఏడాదికి 6000 రూపాయల ఆర్థిక సహాయం అందుతుంది."
>
> **User (Audio)**: "నేను దీనికి అర్హుడినా?" (Am I eligible for this?)
>
> **Agent (Voice)**: "మీ అర్హతను పరిశీలించడానికి, దయచేసి మీ వయస్సు మరియు వార్షిక ఆదాయం చెప్పండి."
>
> **User (Audio)**: "నా వయస్సు 45 సంవత్సరాలు, ఆదాయం లక్ష రూపాయలు."
>
> **Agent (Thought)**: Calling `check_eligibility('pm_kisan', age=45, income=100000, occupation='farmer')`.
> **Tool Output**: `{"eligible": True, "reason": "You meet all the criteria!"}`
>
> **Agent (Voice)**: "అభినందనలు! మీరు PM-KISAN పథకానికి అర్హులు."

## 2. Failed Interaction Caused by Language Barrier (Fixed)
**Scenario**: User uses a Telugu specific term ("Rythu") which the English database didn't understand initially.

> **User (Audio)**: "Rythu bandhu pathakam gurinchi cheppandi."
>
> **Agent (Thought)**: User said "Rythu". Calling `search_schemes('Rythu')`.
> **Tool Output**: `[]` (No results found).
>
> **Agent (Voice)**: "క్షమించండి, 'Rythu' పేరుతో నాకు ఏ పథకాలు దొరకలేదు."
>
> **Correction Applied**: System Prompt updated to force translation.
>
> **Retest (Success)**:
> **Agent (Thought)**: User said "Rythu". Translating to "Farmer". Calling `search_schemes('farmer')`.
> **Tool Output**: Found PM-KISAN etc. accepted.

## 3. System Failure & Recovery (Edge Case)
**Scenario**: Microphone driver (PyAudio) crashes due to incompatibility.

> **System**: `AttributeError: Could not find PyAudio; check installation`
>
> **Agent Handling**: Exception caught in `audio.py`.
>
> **System Output**: `[System]: Audio Error. Switching to Text Input.`
>
> **User (Text Input)**: "Tell me about student schemes."
>
> **Agent (Text Output)**: "For students, we have scholarships..."
>
> **Result**: The system degraded gracefully from Voice -> Text instead of crashing completely.

## 4. Edge Case: Ambiguous Query
**Scenario**: User accepts but doesn't provide details.

> **User (Audio)**: "నాకు డబ్బులు కావాలి." (I want money.)
>
> **Agent (Thought)**: Query is too vague. `search_schemes('money')` might return too many or irrelevant results.
>
> **Agent (Voice)**: "ప్రభుత్వ పథకాల ద్వారా ఆర్థిక సహాయం పొందవచ్చు. కానీ, మీరు విద్యార్థా, రైతా, లేక వృద్ధులా? దయచేసి మీ వివరాలు చెబితే సరైన పథకాన్ని సూచించగలను."
>
> **Result**: Agent correctly asks clarifying questions instead of hallucinating a response.
