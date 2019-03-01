from concurrent import futures
import time

import grpc

from proto import my_if_pb2
from proto import my_if_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


# my_if_pb2_grpcのMyGrpcServicerを実装
class MyGrpc(my_if_pb2_grpc.MyGrpcServicer):

    def GetSomething(self, request, context):

        # いろんな処理
        print("Someone requested something!")
        print(f'int_param: {request.int_param}')
        print(f'str_param: {request.str_param}')

        response = my_if_pb2.MyResp(status=200, message="Great message.")
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # MyGrpc()を使うよ！と登録している
    my_if_pb2_grpc.add_MyGrpcServicer_to_server(MyGrpc(), server)
    # portの設定
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
