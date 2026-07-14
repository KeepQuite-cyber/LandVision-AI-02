class AIMemory:
    _memory = {}
    @classmethod
    def get(cls, session_id="default"):
        return cls._memory.setdefault(session_id,{})
    @classmethod
    def update(cls,session_id="default",**kwargs):
        memory = cls.get(session_id)
        memory.update(kwargs)
    @classmethod
    def clear(cls,session_id="default"
    ):
        cls._memory[session_id] = {}