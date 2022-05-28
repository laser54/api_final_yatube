from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Изменять контент может только автор"""

    message = 'Изменять или удалять чужой контент запрещено'

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class IsFollowerOrReadOnly(permissions.BasePermission):
    """Редактировать свои подписки может только пользователь"""

    message = 'Управлять чужими подписками запрещено'

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
