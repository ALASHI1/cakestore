from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product,ProductImage,Contact
from .forms import ContactCreateForm,Adminpage,Adminmage
from cart.forms import CartAddProductForm
from django.forms import modelformset_factory
def home(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
 
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category) 
	return render(request, 'index.html',{'category': category,'categories': categories, 'products': products})



def product_list(request, category_slug=None): 
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True) 
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category) 
	return render(request,'product/list.html', {'category': category,'categories': categories, 'products': products})



def product_detail(request, id, slug): 
	product = get_object_or_404(Product,id=id, slug=slug, available=True)
	images = ProductImage.objects.filter(product=product)
	cart_product_form = CartAddProductForm()
	return render(request, 'product/detail.html',{'product': product,'cart_product_form': cart_product_form,'images':images})	

def contact(request):
	if request.method == 'POST':
		form = ContactCreateForm(data=request.POST)
		if form.is_valid():
			form.save()
	else:
		form = ContactCreateForm()
	return render(request,'contact.html',{'form':form})

def about(request):
	return render(request,'about.html',{})


def adminpage(request):
	if request.method == 'POST':
		form = Adminpage(data=request.POST)
		if form.is_valid():
			form.save()
			return render(request,'adminpage01.html',{})
	else:
		form = Adminpage()

	return render(request,'adminpage.html',{'form':form})

def adminpage01(request):
	return render(request,'adminpage01.html',{})


def adminpage2(request):
	if request.method == 'POST':
		form = Adminmage(data=request.POST)
		if form.is_valid():
			form.save()
			return render(request,'adminpage01.html',{})
	else:
		form = Adminmage()

	return render(request,'adminpage2.html',{'adminmage':form})






