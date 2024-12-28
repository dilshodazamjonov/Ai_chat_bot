import openai
from django.db.models.expressions import result
from django.http import JsonResponse
from django.shortcuts import render
from pyexpat.errors import messages
from transformers import pipeline

openai_api_key = ''
openai.api_key = openai_api_key

def generate_response(prompt):
    generator = pipeline('text-generation', model='gpt2')
    result = generator(prompt, max_length=200)
    return result[0]['generated_text']
    print(result)
    # answer = response.choice[0].text.strip()
    # return answer

# Create your views here.
def chatbot_views(request):
    if request.method == 'POST':
        messages = request.POST.get('message')
        response = generate_response(messages)
        return JsonResponse({
            'message': messages,
            'response': response
        })
    return render(request, 'chatbot.html')