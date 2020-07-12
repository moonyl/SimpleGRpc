from concurrent import futures
import grpc
import simple_proto_pb2
import simple_proto_pb2_grpc

import logging


class SimpleGRpcServicer(simple_proto_pb2_grpc.SimpleGRpcServicer):
    def Echo(self, request, context):
        return simple_proto_pb2.SimpleData(data=request.data)

    def Add(self, request, context):
        result = request.input1 + request.input2
        return simple_proto_pb2.SimpleResult(result=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    simple_proto_pb2_grpc.add_SimpleGRpcServicer_to_server(
        SimpleGRpcServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
