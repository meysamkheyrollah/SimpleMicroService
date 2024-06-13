import grpc
from . import token_pb2
from . import token_pb2_grpc

def run(payload):
    with grpc.insecure_channel('auth:50051') as channel:
        try:
            stub = token_pb2_grpc.TokenServiceStub(channel)
            data = stub.ExchangeToken(token_pb2.TokenRequest(token=payload))
        except Exception as e:
            data = None
    return data