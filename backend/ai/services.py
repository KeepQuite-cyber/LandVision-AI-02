import json
from groq import Groq
from django.conf import settings
from .prompts import SYSTEM_PROMPT
from .response_prompt import RESPONSE_PROMPT
class AIService:
    client = Groq(api_key=settings.GROQ_API_KEY)
    @classmethod
    def detect_intent( cls, message, memory):
        prompt = f"""
Conversation Memory

{json.dumps(memory, indent=2)}

User Request

{message}
"""

        completion = cls.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0,
            response_format={
                "type": "json_object"
            },
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return json.loads(
            completion.choices[0].message.content
        )

    @classmethod
    def generate_response(cls,tool_outputs):
        completion = cls.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": RESPONSE_PROMPT
                },
                {
                    "role": "user",
                    "content": "\n".join(tool_outputs)
                }
            ]

        )

        return completion.choices[0].message.content.strip()