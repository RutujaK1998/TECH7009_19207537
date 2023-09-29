# views.py
from django.shortcuts import render, redirect
import openai

def display(request):
    return render(request, 'main/display.html', {'display': display})
def commonattractions(request):
    return render(request, 'main/commonattractions.html', {'commonattractions': commonattractions})
# Homepage code
def home(request):
    generated_itinerary = None
    if request.method == "POST":
        destination = request.POST.get("destination")
        duration = request.POST.get("duration")
        budget = request.POST.get("budget")
        # Extract other form fields here
        openai.api_key = "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"
        prompt = f"Generate an itinerary for a trip to {destination} for a duration of {duration} days with a budget of {budget}"
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            temperature=0.5
        )
        generated_itinerary = response.choices[0].text.strip()
        return redirect("itinerary_result", generated_itinerary=generated_itinerary)
    return render(request, "main/home.html")

# Itenery result
def itinerary_result(request, generated_itinerary):
    context = {
        "generated_itinerary": generated_itinerary
    }
    return render(request, "main/itinerary_result.html", context)
