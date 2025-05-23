from rest_framework.views import APIView

from permissions.decorator import permission_required
from utils.base_authentication import JWTAuthentication
from .api_serializer import ProductSerializer,OrderSerializer,OrderDetailSerializer
from rest_framework.response import Response
from utils.reusable_fuunction import get_first_error



class ProductView(APIView):
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]



    @permission_required(['create_product'])
    
    def post (self , request):
        try:
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                obj = serialized_data.save()
                resp = self.serializer_class(obj).data
                return Response({"message":"successful","data":resp},status=200)
            else:
                return Response({"message":get_first_error(serialized_data.error)},status=400)
        except Exception as e :
            return Response({"message": str(e)}, status=500)
    @permission_required(['read_product'])
        
    def get(self , request):
        try:
            instances =self.serializer_class.Meta.model.objects.filter()
            resp = self.serializer_class(instances , many=True).data
            return Response({"message":"successful","data":resp},status=200)
        except Exception as e :
            return Response({"message": str(e)}, status=500)
    @permission_required(['update_product'])
        
    def patch(self, request):
        try:
            if request.query_params.get('id'):
                instance = self.serializer_class.Meta.model.objects.filter(id=request.query_params.get('id')).first()
                if instance:
                    serialized_data = self.serializer_class(instance, data=request.data, partial=True)
                    if serialized_data.is_valid():
                        obj = serialized_data.save()
                        resp = self.serializer_class(obj).data
                        return Response({"message": "SUccessful", "data": resp}, status=200)
                    else:
                        return Response({"message": get_first_error(serialized_data.errors)}, status=400)
                else:
                    return Response({"message": "Not Found"}, status=404)
            else:
                return Response({"message": "ID not provided"}, status=400)

        except Exception as e:
            return Response({"message": str(e)}, status=500)
        
    @permission_required(['delete_product'])
    
    def delete(self, request):
        try :
            if request.query_params.get('id'):
                instance =self.serializer_class.Meta.model.objects.filter(id=request.query_params.get('id')).first()
                if instance:
                    instance.delete()
                    return Response({"message": "SUccessful"}, status=200)
                else:
                    return Response({"message": "not found"}, status=404)
                

            else:
                    return Response({"message": "id not provided"}, status=400)

        except Exception as e:
            return Response({"message": str(e)}, status=500)






class OrderView(APIView):
    serializer_class = OrderSerializer



    def post (self , request):
        try:
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                obj = serialized_data.save()
                resp = self.serializer_class(obj).data
                return Response({"message":"successful","data":resp},status=200)
            else:
                return Response({"message":get_first_error(serialized_data.error)},status=400)
        except Exception as e :
            return Response({"message": str(e)}, status=500)
        
    def get(self , request):
        try:
            instances =self.serializer_class.Meta.model.objects.filter()
            resp = self.serializer_class(instances , many=True).data
            return Response({"message":"successful","data":resp},status=200)
        except Exception as e :
            return Response({"message": str(e)}, status=500)
        
    def patch(self, request):
        try:
            if request.query_params.get('id'):
                instance = self.serializer_class.Meta.model.objects.filter(id=request.query_params.get('id')).first()
                if instance:
                    serialized_data = self.serializer_class(instance, data=request.data, partial=True)
                    if serialized_data.is_valid():
                        obj = serialized_data.save()
                        resp = self.serializer_class(obj).data
                        return Response({"message": "SUccessful", "data": resp}, status=200)
                    else:
                        return Response({"message": get_first_error(serialized_data.errors)}, status=400)
                else:
                    return Response({"message": "Not Found"}, status=404)
            else:
                return Response({"message": "ID not provided"}, status=400)

        except Exception as e:
            return Response({"message": str(e)}, status=500)
        

    def delete(self, request):
        try :
            if request.query_params.get('id'):
                instance =self.serializer_class.Meta.model.objects.filter(id=request.query_params.get('id')).first()
                if instance:
                    instance.delete()
                    return Response({"message": "SUccessful"}, status=200)
                else:
                    return Response({"message": "not found"}, status=404)
                

            else:
                    return Response({"message": "id not provided"}, status=400)

        except Exception as e:
            return Response({"message": str(e)}, status=500)




class OrderDetailView(APIView):
    serializer_class = OrderDetailSerializer



    def post (self , request):
        try:
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                obj = serialized_data.save()
                resp = self.serializer_class(obj).data
                return Response({"message":"successful","data":resp},status=200)
            else:
                return Response({"message":get_first_error(serialized_data.error)},status=400)
        except Exception as e :
            return Response({"message": str(e)}, status=500)
        
    def get(self , request):
        try:
            instances =self.serializer_class.Meta.model.objects.filter()
            resp = self.serializer_class(instances , many=True).data
            return Response({"message":"successful","data":resp},status=200)
        except Exception as e :
            return Response({"message": str(e)}, status=500)
        
    def patch(self, request):
        try:
            if request.query_params.get('id'):
                instance = self.serializer_class.Meta.model.objects.filter(id=request.query_params.get('id')).first()
                if instance:
                    serialized_data = self.serializer_class(instance, data=request.data, partial=True)
                    if serialized_data.is_valid():
                        obj = serialized_data.save()
                        resp = self.serializer_class(obj).data
                        return Response({"message": "SUccessful", "data": resp}, status=200)
                    else:
                        return Response({"message": get_first_error(serialized_data.errors)}, status=400)
                else:
                    return Response({"message": "Not Found"}, status=404)
            else:
                return Response({"message": "ID not provided"}, status=400)

        except Exception as e:
            return Response({"message": str(e)}, status=500)
        

    def delete(self, request):
        try :
            if request.query_params.get('id'):
                instance =self.serializer_class.Meta.model.objects.filter(id=request.query_params.get('id')).first()
                if instance:
                    instance.delete()
                    return Response({"message": "SUccessful"}, status=200)
                else:
                    return Response({"message": "not found"}, status=404)
                

            else:
                    return Response({"message": "id not provided"}, status=400)

        except Exception as e:
            return Response({"message": str(e)}, status=500)




