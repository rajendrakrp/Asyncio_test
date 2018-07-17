from django.shortcuts import render_to_response, render

# Create your views here.

from django.views.generic import TemplateView
import asyncio

class TestAsync(TemplateView):
    template_name = 'test.html'

    def get(self, request, *args, **kwargs):
        print ("Testing async functions using asyncio")
        from async_app.utils import get_results, func1, func2
        response = get_results(func1, func2)
        print ("response:", response)
        return render(request, 'test.html')

class TestAsyncFromSync(TemplateView):
    template_name = 'test.html'

    def get(self, request, *args, **kwargs):
        print ("Testing sync functions using asyncio")
        from async_app.sync_utils import get_results, func1, func2
        response = get_results(func1, func2)
        print ("response:", response)
        return render(request, 'test.html')

class TestDbCall(TemplateView):
    template_name = 'test.html'

    def get(self, request, *args, **kwargs):
        print ("Testing db calls")
        from async_app.db_utils import get_results, order_details, member_details
        response = get_results(order_details, member_details)
        print ("response:", response)
        return render(request, 'test.html')

class TestAsyncDbCall(TemplateView):
    template_name = 'test.html'

    def get(self, request, *args, **kwargs):
        print ("Testing db calls")
        from async_app.async_db_utils import get_results, func1, func2
        response = get_results(func1, func2)
        print ("response:", response)
        return render(request, 'test.html')

