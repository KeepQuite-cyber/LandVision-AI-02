from .tools import AITools

class AIExecutor:
    @staticmethod
    def execute(plan):
        
        steps = plan.get("steps", [])
        if not steps:
            return {
                "reply": "Sorry, I couldn't understand your request.",
                "actions": []
            }
        responses = []
        actions = []
        for step in steps:
            try:
                result = AITools.execute(step)
            except Exception as e:
                result = {"reply" : str(e)}
            if not result:
                continue
            responses.append(
                result.get("reply", "")
            )
            if result.get("action"):
                actions.append(result)
        from .services import AIService
        reply = AIService.generate_response(responses)
        return {
            "reply": reply,
            "actions" : actions
        }