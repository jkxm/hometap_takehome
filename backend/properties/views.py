from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from properties.adapters import *

def property_view(request):
    address = request.GET.get('address')

    if not address:
        return JsonResponse({"error": "Address is required"}, status=400)
    
    provider_one = ProviderOneAdapter(address=address)
    provider_two = ProviderTwoAdapter(address=address)

    providers = {
        "Provider 1": ProviderOneAdapter,
        "Provider 2": ProviderTwoAdapter
    }

    data = {}

    for provider, adapter in providers.items():
        provider_adapter = adapter(address=address)
        data[provider] = provider_adapter.get_data()

    return JsonResponse(data)

# Create your views here.
