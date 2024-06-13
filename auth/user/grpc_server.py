from concurrent import futures
import grpc
from . import token_pb2_grpc
from . import token_pb2
from rest_framework_simplejwt.authentication import JWTAuthentication

class TokenServiceServicer(token_pb2_grpc.TokenServiceServicer):
    def ExchangeToken(self, request, context):
        decoded = JWTAuthentication().get_validated_token(raw_token=request.token)
        print('payload is', decoded)
        return token_pb2.TokenResponse(data=str(decoded['user_id']))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    token_pb2_grpc.add_TokenServiceServicer_to_server(TokenServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()