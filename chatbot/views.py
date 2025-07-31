from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from openai import OpenAI
import os
from datetime import datetime
from .models import User

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Global variable to store the uploaded file ID
uploaded_file_id = None

def upload_pdf_file():
    """Upload the PDF file to OpenAI and return the file ID"""
    global uploaded_file_id
    
    # If file is already uploaded, return the existing ID
    if uploaded_file_id:
        return uploaded_file_id
    
    try:
        # Upload the PDF file
        file = client.files.create(
            file=open("./PDF/LectureNotes.pdf", "rb"),
            purpose="user_data"
        )
        uploaded_file_id = file.id
        return uploaded_file_id
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None

def read_prompt():
    with open('./prompt/Prompt1.txt', 'r') as file:
        return file.read().strip()

def count_tokens(text):
    """Count tokens based on character count: 1 token = 4 characters"""
    # Count total characters in the text
    char_count = len(text)
    # Calculate tokens: 1 token = 4 characters
    tokens = char_count / 4
    # Round up to the nearest whole token
    return int(tokens) + (1 if tokens % 1 > 0 else 0)

def log_token_request(username, message, token_count):
    """Log token request to token log file and update user's token count in database"""
    # Update user's token count in database
    try:
        user = User.objects.get(username=username)
        user.tokens += token_count
        user.save()
    except User.DoesNotExist:
        pass 
    
    # Log to token log file
    logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'log')
    os.makedirs(logs_dir, exist_ok=True)
    token_log_path = os.path.join(logs_dir, 'token_log.txt')
    
    with open(token_log_path, 'a', encoding='utf-8') as f:
        now = datetime.now()
        formatted_now = now.strftime('%Y-%m-%d %H:%M:%S')
        # Shorten message if too long
        truncated_message = message[:100] + "..." if len(message) > 100 else message
        f.write(f"{formatted_now} - User {username} sent message: '{truncated_message}' (Token count: {token_count})\n")





@csrf_exempt
def chat_api(request):
    def log_message(sender, message, username):
        # Sanitize username
        safe_username = "".join([c for c in username if c.isalnum() or c in ('.', '_', '-')]).strip()
        if not safe_username: 
            safe_username = "invalid_username"
            
        log_file_name = f"{safe_username}.txt"
        logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'chat_history')
        os.makedirs(logs_dir, exist_ok=True)
        log_path = os.path.join(logs_dir, log_file_name)
        with open(log_path, 'a', encoding='utf-8') as f:
            now = datetime.now()
            formatted_now = now.strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"{formatted_now} - {sender}: {message}\n\n")

    if request.method == 'POST':
        try:
            # Get username from request
            data = json.loads(request.body)
            messages = data.get('messages', [])
            username = data.get('username', 'unknown_user')  
            
            # Log user message(s) and count tokens
            for msg in messages:
                if msg.get('role') == 'user':
                    content = msg.get('content', '')
                    log_message('User', content, username)
                    # Count tokens and log token request
                    token_count = count_tokens(content)
                    log_token_request(username, content, token_count)

            # Make sure there's a system message
            if not any(msg.get('role') == 'system' for msg in messages):
                system_prompt = read_prompt() 
                messages.insert(0, {
                    'role': 'system',
                    'content': system_prompt
                })

            # Upload PDF file and get file ID
            file_id = upload_pdf_file()
            
            # Modify the last user message to include the file
            if messages and messages[-1].get('role') == 'user':
                original_content = messages[-1]['content']
                messages[-1]['content'] = [
                    {
                        "type": "file",
                        "file": {
                            "file_id": file_id,
                        }
                    },
                    {
                        "type": "text",
                        "text": original_content,
                    },
                ]

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )

            chatbot_reply = response.choices[0].message.content
            # Log chatbot response
            log_message('Chatbot', chatbot_reply, username)
            return JsonResponse({
                'message': chatbot_reply,
                'role': 'assistant'
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def authenticate_user(request):
    if request.method == 'POST':
        try:
            # Check if has content
            if not request.body:
                return JsonResponse({'error': 'Request body is empty'}, status=400)
            
            # Parse JSON
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError as e:
                return JsonResponse({'error': 'Invalid JSON format'}, status=400)
            
            username = data.get('username', '')
            password = data.get('password', '')
            
            if not username or not password:
                return JsonResponse({'error': 'Username and password are required'}, status=400)
            
            # Check if user exists
            try:
                user = User.objects.get(username=username)
                
                # Check if password matches
                if user.password == password:
                    # Logging
                    logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'log')
                    os.makedirs(logs_dir, exist_ok=True)
                    login_log_path = os.path.join(logs_dir, 'login_log.txt')

                    with open(login_log_path, 'a', encoding='utf-8') as f:
                        now = datetime.now()
                        formatted_now = now.strftime('%Y-%m-%d %H:%M:%S')
                        f.write(f"{formatted_now} - User {username} logged in successfully.\n")
                    
                    return JsonResponse({'status': 'success', 'message': 'Login successful'})
                else:
                    return JsonResponse({'error': 'Invalid credentials!'}, status=401)
            except User.DoesNotExist:
                return JsonResponse({'error': 'Invalid credentials!'}, status=401)
                
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)



@csrf_exempt
def get_token_count(request):
    """Endpoint to get a user's token count"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            
            if not username:
                return JsonResponse({'error': 'Username is required'}, status=400)
            
            try:
                user = User.objects.get(username=username)
                return JsonResponse({
                    'username': username,
                    'tokens': user.tokens
                })
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
                
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def test_view(request):
    """Simple test endpoint to verify the server is running"""
    return JsonResponse({
        'status': 'success',
        'message': 'Server is running!',
        'timestamp': datetime.now().isoformat()
    })