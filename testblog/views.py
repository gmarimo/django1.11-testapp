from django.shortcuts import render

def post_list(request):
    return render(request, 'testblog/post_list.html', {})
