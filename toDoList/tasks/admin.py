from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Vista de administración para el modelo Task."""
    list_display = ('title', 'status', 'created_at', 'user')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description')

    def get_queryset(self, request):
        """Limita las tareas mostradas al usuario actual."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        """Asigna el usuario actual como propietario de la tarea."""
        obj.user = request.user
        super().save_model(request, obj, form, change)