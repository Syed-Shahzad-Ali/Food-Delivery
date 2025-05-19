from django.shortcuts import render
from . models import Role,Permission
from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
#from .blog_serializer import BlogSerializer
from utils.base_authentication import JWTAuthentication
from .permission_controller import RoleController, PermissionController
from .decorator import permission_required
from rest_framework.permissions import IsAdminUser
# Create your views here.


role_controller = RoleController()
permission_controller = PermissionController()
# rolepermission_controller = RolepermissionController()



class RoleViews(ModelViewSet):

    authentication_classes = [JWTAuthentication]
    @permission_required(['create_role'])


    def post_role(self, request):
        return role_controller.create(request)
    

    @permission_required(['read_role'])

    
    def get_role(self, request):
        return role_controller.get_role(request)
    
    @permission_required(['update_role'])

    
    def update_role(self, request):
        return role_controller.update_role(request)
    
    @permission_required(['delete_role'])

    
    def delete_role(self, request):
        return role_controller.delete_role(request)
    
class PermissionViews(ModelViewSet):

    authentication_classes = [JWTAuthentication]
    
    def post_permission(self, request):
        return permission_controller.create(request)
    
    def get_permission(self, request):
        return permission_controller.get_permission(request)
    
    def update_permission(self, request):
        return permission_controller.update_permission(request)
    
    def delete_permission(self, request):
        return permission_controller.delete_permission(request)