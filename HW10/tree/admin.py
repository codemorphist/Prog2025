from django.contrib import admin

from tree.models import TreeFamily, TreeSort, Place, Tree, Harvest


admin.site.register(TreeFamily)
admin.site.register(TreeSort)
admin.site.register(Place)
admin.site.register(Tree)
admin.site.register(Harvest)
