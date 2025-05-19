from rest_framework.exceptions import PermissionDenied
from .models import Role

def permission_required(permissions):
    def decorator(drf_custom_method):
        def _decorator(self, *args, **kwargs):
            user = self.request.user

            if not user.is_authenticated:
                raise PermissionDenied("User is not authenticated")

            if user.is_superuser:
                return drf_custom_method(self, *args, **kwargs)

            if not hasattr(user, 'role') or user.role is None:
                raise PermissionDenied("User has no role assigned")

            if Role.objects.filter(id=user.role.id, permissions__code__in=permissions).exists():
                return drf_custom_method(self, *args, **kwargs)
            else:
                raise PermissionDenied("User does not have the required permissions")

        return _decorator
    return decorator
