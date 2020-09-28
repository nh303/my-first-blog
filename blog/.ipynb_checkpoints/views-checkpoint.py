from django.shortcuts import render

# Create your views here.
def post_list(request):
    print('hello world')
    return render(request, 'blog/post_list.html', {})

def ola_blog(request):
    print("Ola's blog")
    return render(request, 'blog/ola_blog.html', {})

def class(request):
    print('django')
    return render(request, 'blog/class.html', {})

def object(request):
    print('Hi there!!')
    return render(request, 'blog/object.html', {})
