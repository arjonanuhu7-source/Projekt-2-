from django.shortcuts import render, get_object_or_404
from .models import Animal, Category, ContactMessage, BlogPost


def home(request):
    categories = Category.objects.all()

    featured_animals = []

    for category in categories:
        animal = Animal.objects.filter(category=category).first()

        if animal:
            featured_animals.append(animal)

    return render(request, 'index.html', {
        'categories': categories,
        'featured_animals': featured_animals
    })


def animal_list(request):
    animals = Animal.objects.all()
    categories = Category.objects.all()

    search_query = request.GET.get('q')
    category_id = request.GET.get('category')

    if search_query:
        animals = animals.filter(name__icontains=search_query)

    if category_id:
        animals = animals.filter(category_id=category_id)

    return render(request, 'animal_list.html', {
        'animals': animals,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id
    })


def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    return render(request, 'animal_detail.html', {
        'animal': animal
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    success = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        success = True

    return render(request, 'contact.html', {
        'success': success
    })


def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')

    return render(request, 'blog_list.html', {
        'posts': posts
    })


def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    return render(request, 'blog_detail.html', {
        'post': post
    })