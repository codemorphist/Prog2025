from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import render

from tree.models import *


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'tree/home.html')


class TreeListView(ListView):
    model = Tree
    paginate_by = 10
    template_name = 'tree/treelist.html'
    context_object_name = 'trees'


class TreeFamilyView(DetailView):
    model = TreeFamily
    template_name = 'tree/treefamily.html'
    context_object_name = 'family'


class TreeSortView(DetailView):
    model = TreeSort
    template_name = 'tree/treesort.html'
    context_object_name = 'sort'


class PlaceView(DetailView):
    model = Place
    template_name = 'tree/place.html'
    context_object_name = 'place'


class TreeView(DetailView):
    model = Tree
    template_name = 'tree/tree.html'
    context_object_name = 'tree'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tree = super().get_object()
        context['harvest'] = Harvest.objects.filter(tree=tree)
        return context


class TreeAddView(CreateView):
    model = Tree
    template_name = 'tree/add_tree.html'
    fields = '__all__'


class TreeFamilyAddView(CreateView):
    model = TreeFamily
    template_name = 'tree/add_treefamily.html'
    fields = '__all__'


class TreeSortAddView(CreateView):
    model = TreeSort
    template_name = 'tree/add_treesort.html'
    fields = '__all__'


class PlaceAddView(CreateView):
    model = Place
    template_name = 'tree/add_place.html'
    fields = '__all__'


class HarverAddView(CreateView):
    model = Harvest
    template_name = 'tree/add_harvest.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('tree:tree', args=(self.object.tree.pk,))
