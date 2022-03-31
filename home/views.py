from django.shortcuts import render

from utils.utils.shell import get_output
# Create your views here.

def main_page(request):
    kv = get_output('uname -r')
    return render(request, 'home/index.html', {'kv': kv})
