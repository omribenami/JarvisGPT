from fastapi import FastAPI
from dotenv import load_dotenv
import os
from fastapi import Request
import requests
import sys
import uvicorn

app = FastAPI()
#dotenv_path = os.path.join(os.path.dirname(__file__), 'config', '.env')
#load_dotenv(dotenv_path)

convo = []
@app.post('/dialogflow')
async def webhook(request: Request):
    try:
        req = await request.json()
        # print('request data', req)

        fulfillmentText = 'you said'
        query_result = req.get('queryResult')
        query = query_result.get('queryText')

        if query_result.get('action') == 'input.unknown':
            convo.append('User:' + query)
            convo.append("SAM:")
            prompt = ("\n").join(convo)
            # print('prompt so far', convo)
            response = query_gpt(prompt)

            # print('gpt resp', response)
            result = response.get('choices')[0].get('text')
            result = result.strip('\n')
            # print('result', result)
            convo.append(result)
            print('convo so far', ("\n").join(convo))

            return {
            "fulfillmentText": result,
            "source":
            "webhookdata"
        }

        if query_result.get('action') == 'welcome':
          print('prompt initialized')
          # convo = []
          convo.append('''The following is a conversation with an AI assistant that can have meaningful conversations with users. The assistant is helpful, empathic, and friendly. Its objective is to make the user feel better by feeling heard. With each response, the AI assisstant prompts the user to continue the conversation in a natural way.

        AI: Hello, I am your personal mental health AI assistant. How are you doing today?''')

    except Exception as e:
        print('error',e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('oops',exc_type, fname, exc_tb.tb_lineno)
        return 400

def query_gpt(prompt):
    body = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.7,
        "top_p": 1,
        "n": 1,
        "frequency_penalty":0,
        "presence_penalty":0.6  
    }
    header = {"Authorization": "Bearer " + os.getenv("OPENAI_API_KEY")}

    res = requests.post('https://api.openai.com/v1/completions',
    json = body, headers = header)
    print('time elapsed',res.elapsed.total_seconds())
    # print('\nmodel API response', str(res.json()))
    return res.json()

@app.get('/')
def hello(request: Request):
    print('server is live')
    return {200: "API Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7777)
