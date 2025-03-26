import asyncio
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import logging
from .bot import bot_tele

logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        data = request.body
        res = json.loads(data.decode('utf-8'))
        print(res)
        asyncio.run(bot_tele(res))
        return HttpResponse("ok")
    else:
        return HttpResponse("hello world!")

@csrf_exempt
@require_http_methods(["POST"])
def webhook(request):
    """Handle incoming webhook requests from Telegram."""
    try:
        # Get the update from the request
        update = request.body.decode('utf-8')
        
        # Log the incoming request
        logger.info(f"Received update: {update}")
        
        # Process the update
        bot_tele(update)
        
        return HttpResponse("OK")
        
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        return HttpResponse(status=500)