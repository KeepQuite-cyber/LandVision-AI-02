import json

class AILogger:
    @staticmethod
    def log(title , data):
        print("\n" + "=" * 70)
        print(title)
        print("-"*70)

        if isinstance(data,dict):
            print(json.dumps(data,indent=4))
        else:
            print(data)
        
        print("=" * 70)