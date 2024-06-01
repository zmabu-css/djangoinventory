from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category

def index(request):
    return render(request, 'inventory/index.html')

class ProductListView(ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'inventory/product_detail.html'
    context_object_name = 'product'

class CategoryListView(ListView):
    model = Category
    template_name = 'inventory/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(ListView):
    model = Product
    template_name = 'inventory/category_detail.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
