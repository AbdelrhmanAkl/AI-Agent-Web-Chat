import os
from typing import Dict, List

from groq import Groq


class AIChatAgent:
    """Conversational AI agent with per-conversation memory."""

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GROQ_API_KEY is missing. Add it to the .env file."
            )

        self.client = Groq(api_key=api_key)

        self.model = os.getenv(
            "GROQ_MODEL",
            "llama-3.3-70b-versatile",
        )

        self.system_prompt = """
You are a helpful AI assistant inside a web chat application.

Your responsibilities:
- Answer the user's questions clearly and accurately.
- Use previous conversation context when relevant.
- Be concise but useful.
- If you are unsure, say so instead of inventing facts.
"""

        self.histories: Dict[str, List[dict]] = {}

    def _get_history(self, conversation_id: str) -> List[dict]:
        if conversation_id not in self.histories:
            self.histories[conversation_id] = [
                {
                    "role": "system",
                    "content": self.system_prompt,
                }
            ]

        return self.histories[conversation_id]

    def chat(self, message: str, conversation_id: str) -> str:
        history = self._get_history(conversation_id)

        history.append(
            {
                "role": "user",
                "content": message,
            }
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=history,
            temperature=0.3,
            max_tokens=1024,
        )

        answer = response.choices[0].message.content.strip()

        history.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        return answer

    def clear_history(self, conversation_id: str):
        self.histories.pop(conversation_id, None)