from random import choice, randint
from chatbot import chat
import subprocess
import io
import sys
import traceback

def runCode(code):
    try:
        result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, timeout=10)
        return ("```" + result.decode("utf-8") + "```")
    except subprocess.CalledProcessError as e:
        return ("Error: " + e.output.decode("utf-8"))
    except subprocess.TimeoutExpired:
        return ("Error: Execution timed out.")
    except Exception as e:
        return ("Error: " + str(e))
def runCode2(code):
    sys.stdout = io.StringIO()

    try:
        exec(code, globals(), locals())
        output = sys.stdout.getvalue()
        if output:
            return("```" + output + "```")
    # except Exception:
    #     error_message = traceback.format_exc()
    #     return("Error: " + error_message)
    except subprocess.CalledProcessError as e:
        return ("Error: " + e.output.decode("utf-8"))
    except subprocess.TimeoutExpired:
        return ("Error: Execution timed out.")
    except Exception as e:
        return ("Error: " + str(e))

    # Reset standard output
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