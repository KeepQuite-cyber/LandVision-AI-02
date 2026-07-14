from .memory import AIMemory
from .services import AIService
from .executor import AIExecutor


class AIAgent:

    @classmethod
    def chat( cls, session_id, message):
        memory = AIMemory.get(session_id)
        plan = AIService.detect_intent(message,memory)
        try:
            response = AIExecutor.execute(plan)
        except Exception:
            return{
                "reply" : "Something went wrong while executing your request",
                 "actions": []
            }
            
        cls.update_memory(session_id,plan,response)
        return response
    
    @staticmethod
    def update_memory( session_id, plan, response ):
        memory = {}
        for step in plan.get("steps", []):
            action = step.get("action")
            if action == "search_plot":
                memory["current_plot"] = step.get("plot_number")
            elif action == "owner_details":
                memory["current_plot"] = step.get("plot_number")
            elif action == "village_summary":
                memory["current_village"] = step.get("village")
            elif action == "filter_land_use":
                memory["current_land_use"] = step.get("land_use")
        memory["last_action"] = action

        AIMemory.update(session_id, **memory)