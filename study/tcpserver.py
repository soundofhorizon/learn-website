import socket


class TCPServer:
    """
    TCP通信を行うサーバーを表すクラス
    """

    def serve(self):
        """
        サーバーを起動する
        :return:
        state
        """
        print("サーバーを起動します")

        try:
            # socketを生成
            server_socket = socket.socket()
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # socketをlocalhostの8080portに割り当て
            server_socket.bind(("localhost", 8080))
            server_socket.listen(10)

            # 外部接続を待ち、接続があったらコネクション確立
            print("クライアントからの接続を待ちます")
            (client_socket, address) = server_socket.accept()
            print(f"クライアントとの接続を確立しました, remote_address: {address}")

            request = client_socket.recv(4096)

            # 送られたデータをファイルに出す
            with open("server_recv.txt", "wb") as f:
                f.write(request)

            # 通信終了
            client_socket.close()

        finally:
            print("サーバーを停止します")


if __name__ == "__main__":
    server = TCPServer()
    server.serve()
