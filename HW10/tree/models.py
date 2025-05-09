from django.db import models
from django.urls import reverse
import datetime


class TreeFamily(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self) -> str:
        return reverse('tree:family', args=[self.pk])


class TreeSort(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    family = models.ForeignKey(TreeFamily, on_delete=models.CASCADE, related_name='sorts')

    class Meta:
        ordering = ['name', 'family']

    def __str__(self) -> str:
        return f'({self.family}) {self.name}'

    def get_absolute_url(self) -> str:
        return reverse('tree:sort', args=[self.pk])


class Place(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return str(self.name)
    
    def get_absolute_url(self) -> str:
        return reverse('tree:place', args=[self.pk])


class Tree(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    sort = models.ForeignKey(TreeSort, on_delete=models.CASCADE, related_name='trees')
    planting_date = models.DateField(auto_now_add=True)
    planting_place = models.ForeignKey(Place, on_delete=models.CASCADE) 

    class Meta:
        ordering = ['name', 'sort__family', 'sort']

    def __str__(self) -> str:
        return f'({self.pk}) {self.name}'

    def get_absolute_url(self) -> str:
        return reverse('tree:tree', args=[self.pk])


def year_choices() -> list:
    return [(r,r) for r in range(2000, datetime.date.today().year+1)]


def current_year() -> int:
    return datetime.date.today().year


class Harvest(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    weight = models.IntegerField(blank=False)
    year = models.IntegerField(choices=year_choices, default=current_year)
