from random import choice, randint
from chatbot import chat
#test
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'ai' in lowered:
        return chat(lowered[2:])
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'roll' in lowered:

        parts = lowered.split(" ")
        d = parts[1].split("d")

        return "You rolled: " + ", ".join(([str(randint(1,int(d[1]))) for i in range(int(d[0])) ]))



    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'bruh what u saying cuh'])