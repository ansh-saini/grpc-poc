from concurrent import futures
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

from database import session, Users


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        first_user_email = session.query(Users).first().email
        message = f"Hello, World! From GRPC service: {first_user_email}"
        return helloworld_pb2.HelloReply(message=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()