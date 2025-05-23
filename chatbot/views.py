from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from openai import OpenAI
import os
from datetime import datetime

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def read_prompt():
    print("Current working directory:", os.getcwd())
    with open('./Prompt.txt', 'r') as file:
        return file.read().strip()

def chat_view(request):
    return render(request, 'chatbot/chat.html')

@csrf_exempt
def chat_api(request):
    def log_message(sender, message):
        log_path = os.path.join(os.path.dirname(__file__), 'Log.txt')
        with open('./Log.txt', 'a', encoding='utf-8') as f:
            now = datetime.now()
            formatted_now = now.strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"{formatted_now} - {sender}: {message}\n\n")

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            messages = data.get('messages', [])
            
            # Log user message(s)
            for msg in messages:
                if msg.get('role') == 'user':
                    log_message('User', msg.get('content', ''))

            # Ensure there's a system message
            if not any(msg.get('role') == 'system' for msg in messages):
                system_prompt = read_prompt()  # Read prompt from the file
                messages.insert(0, {
                    'role': 'system',
                    'content': system_prompt
                })

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            chatbot_reply = response.choices[0].message.content
            # Log chatbot response
            log_message('Chatbot', chatbot_reply)
            return JsonResponse({
                'message': chatbot_reply,
                'role': 'assistant'
            })
        except Exception as e:
            print("Error in chat_api:", str(e))  # Add logging
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)