import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .ai_assistant import get_ai_response

def home(request):
    return render(request, "index.html")

@csrf_exempt
@require_POST
def chat_api(request):
    """API endpoint for visitor AI queries."""
    try:
        data = json.loads(request.body.decode('utf-8'))
        user_message = data.get('message', '').strip()
        if not user_message:
            return JsonResponse({
                'status': 'error',
                'reply': 'Please enter a question.'
            }, status=400)
            
        reply = get_ai_response(user_message)
        return JsonResponse({
            'status': 'success',
            'reply': reply
        })
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'reply': 'Invalid JSON request format.'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'reply': 'An unexpected error occurred while processing your request.'
        }, status=500)
