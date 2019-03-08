import grpc

from proto import my_if_pb2
from proto import my_if_pb2_grpc


def run():
    # SSL/TLS認証を利用する場合は`secure_channel`を使用する
    # 通信先を設定する（server.pyでポートを50051に設定したのでそれを指定）
    # リトライ設定等はoptionで指定できる
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = my_if_pb2_grpc.MyGrpcStub(channel)
        # ここでデータを送信している
        resp = stub.GetSomething(my_if_pb2.MyReq(int_param=99, str_param='me'))
    # 受け取ったデータはxx.yyで受け取れる
    print(f'client received: status={resp.status}, message={resp.message}')


if __name__ == '__main__':
    print("run")
    run()
