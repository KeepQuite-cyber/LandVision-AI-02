import json
from groq import Groq
from django.conf import settings
from .prompts import SYSTEM_PROMPT
from .tools import AITools

class AIService:
    client = Groq(api_key=settings.GROQ_API_KEY)
    @classmethod
    def detect_intent(cls, message):
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
                    "content": message
                }
            ]

        )
        return json.loads(
            completion.choices[0].message.content
        )

    @classmethod
    def chat(cls, message):
        try:
            intent = cls.detect_intent(message)
            result = AITools.execute(intent)
            return result
        except Exception as e:
            return {
                "reply": "Sorry, something went wrong while processing your request.",
                "error": str(e)
            }