from django.shortcuts import render
from .models import Page
from .forms import PageForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "diary/index.html")

def info(request):
    return render(request, 'diary/info.html')

class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    template_name = "diary/page_form.html"

    def get_success_url(self):
        return reverse('page-detail', kwargs={'pk':self.object.id})

class PageListView(ListView):
    model = Page
    template_name = "diary/page_list.html"
    ordering = ["-dt_created"]
    paginate_by = 8
    page_kwarg = 'page'

class PageDetailView(DetailView):
    model = Page
    template_name = "diary/page_detail.html"
    # pk_url_kwarg = "pk"

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name = "diary/page_form.html"
    # pk_url_kwarg= "pk"

    def get_success_url(self):
        return reverse('page-detail', kwargs={"pk":self.object.id})

class PageDeleteView(DeleteView):
    model = Page
    template_name = "diary/page_confirm_delete.html"
    # pk_url_kwarg = "pk"

    def get_success_url(self):
        return reverse('page-list')

# def page_create(request):
#     if request.method == 'POST':
#         new_page = Page(
#             title = request.POST['title'],
#             content = request.POST['content'],
#             feeling = request.POST['feeling'],
#             score = request.POST['score'],
#             dt_created = request.POST['dt_created'],
#         )
#         new_page.save()
#         return redirect('page-detail', page_id=new_page.id)
#     else :
#         form = PageForm()
#         return render(request, 'diary/page_form.html', {'form': form})

# def page_create(request):
#     if request.method == "POST":
#         form = PageForm(request.POST)
#         if form.is_valid():
#             new_page = form.save()
#             return redirect('page-detail', page_id=new_page.id)
#     else : 
#         form = PageForm()
#     return render(request, 'diary/page_form.html', {'form': form})      

# def page_list(request):
#     object_list = Page.objects.all()
#     paginator = Paginator(object_list, 8)
#     curr_page_num = request.GET.get('page')
#     if curr_page_num == None:
#         curr_page_num = 1
#     page = paginator.page(curr_page_num)
#     return render(request, "diary/page_list.html", {'page': page})  

# def page_detail(request, page_id):
#     object = Page.objects.get(id=page_id)
#     return render(request, "diary/page_detail.html", {'object': object})

# def page_update(request, page_id):
#     object = Page.objects.get(id=page_id)
#     if request.method == "POST":
#         form = PageForm(request.POST, instance=object)
#         if form.is_valid():
#             form.save()
#             return redirect('page-detail', page_id=object.id)
#     else:
#         form = PageForm(instance=object)
#     return render(request, 'diary/page_form.html', {'form': form})

# def page_delete(request, page_id):
#     object = Page.objects.get(id=page_id)
#     if request.method == 'POST':
#         object.delete()
#         return redirect('page-list')
#     else:
#         return render(request, 'diary/page_confirm_delete.html', {'object': object})