from django.shortcuts import render
from .forms import CSVUploadForm
from .models import UploadedCSV
import openai

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_csv = form.save()
            result = process_csv_with_chatgpt(uploaded_csv.file.path)
            return render(request, 'result.html', {'result': result})
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})

def process_csv_with_chatgpt(csv_file_path):
    # Add code to process the CSV file using ChatGPT
    # For example, using OpenAI's GPT-3 API
    openai.api_key = 'your-own-api-key' # You should generate api key to test this project
    with open(csv_file_path, 'r') as file:
        content = file.read()
    response = openai.Completion.create(
        engine="davinci",
        prompt=content,
        max_tokens=100,
        n=1,
        stop=None
    )
    return response.choices[0].text
