import grpc
from concurrent import futures
import time
import factorial_pb2
import factorial_pb2_grpc
import os


class FactorialServicer(factorial_pb2_grpc.FactorialServiceServicer):  # Usar el nombre correcto de la clase
    def Compute(self, request, context):
        number = request.number
        result = 1
        for i in range(1, number + 1):
            result *= i
        return factorial_pb2.FactorialResponse(result=result)


def serve():
    port = os.getenv('PORT', '50051')  # Usar el puerto de la variable de entorno
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Cambiado para usar el nombre correcto de la función
    factorial_pb2_grpc.add_FactorialServiceServicer_to_server(FactorialServicer(), server)

    server.add_insecure_port(f'0.0.0.0:{port}')
    server.start()
    print(f"Server is running on port {port}...")
    try:
        while True:
            time.sleep(86400)  # Sleep for a day
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
