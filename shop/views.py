from django.shortcuts import render, redirect
from django.views.generic import DetailView

from main.models import TodoList
from shop.forms import ReviewForm
from shop.models import Product, Review


# Create your views here.
def shop_index(request):
    progress = TodoList.objects.filter(status=True).count()
    context = {
        'progress': progress,

    }
    return render(request, 'shop_index.html', context)

def shop_catalog(request):
    progress = TodoList.objects.filter(status=True).count()
    products_item = Product.objects.order_by('-pk')

    context = {
        'product_list': products_item,

    }
    return render(request, 'shop_catalog.html', context)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop_product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        reviews = product.reviews.all().order_by('-pk')
        context['reviews'] = reviews

        if self.request.user.is_authenticated:
            context['review_form'] = ReviewForm()

        return context

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        form = ReviewForm(request.POST)

        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']

            review = Review.objects.create(
                user=self.request.user,
                rating=rating,
                comment=comment
            )
            product.reviews.add(review)

        return redirect('product-detail', pk=product.pk)