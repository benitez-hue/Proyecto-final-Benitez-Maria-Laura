from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm
from django.contrib import messages

# Vista para listar los blogs
def lista_blogs(request):
    blogs = Blog.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/lista_blogs.html', {'blogs': blogs})

# Vista para el detalle de un blog
def detalle_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog/detalle_blog.html', {'blog': blog})

# Vista para crear un nuevo blog
def nuevo_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El blog se ha creado correctamente.')
            return redirect('blog:lista_blogs')
    else:
        form = BlogForm()
    return render(request, 'blog/nuevo_blog.html', {'form': form})
