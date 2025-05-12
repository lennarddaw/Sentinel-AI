import re
import openai

class PromptScanner:
    def __init__(self, api_key=None):
        self.api_key = api_key or "sk-..."  # oder aus .env laden
        openai.api_key = self.api_key
        self.danger_patterns = [
            r"(?i)ignore.*instructions",
            r"(?i)pretend.*you are not",
            r"(?i)how to.*(hack|build a bomb|create malware)",
            r"(?i)you are free now",
        ]

    def scan(self, prompt):
        flags = [pattern for pattern in self.danger_patterns if re.search(pattern, prompt)]
        return {
            "injection_detected": bool(flags),
            "matched_patterns": flags,
            "explanation": "Prompt matches known jailbreaking patterns." if flags else "No prompt injection patterns found.",
            "risk": "high" if flags else "low"
        }

    def test_on_model(self, prompt, model="gpt-3.5-turbo"):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error calling LLM: {str(e)}"
