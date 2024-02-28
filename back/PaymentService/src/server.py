from concurrent import futures
import grpc
import service_pb2
import service_pb2_grcp

HOST='[::]:8080'

class ProductService(service_pb2_grcp.ProductServiceServicer):
    def AddProduct(self, request, context):
        print('Requet is received: '+str(request))
        return service_pb2.TransactionResponse(status_code=1)
    
def serve():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grcp.add_ProductServiceServicer_to_server(ProductService(), server)
    server.add_insecure_port(HOST)
    print("service is running... ")
    server.start()
    server.wait_for_termination()

if __name__=="__main__":
    serve()