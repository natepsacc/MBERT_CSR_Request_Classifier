from concurrent import futures
import grpc
import classifier_pb2
import classifier_pb2_grpc
from infer import predict


class ClassifierServicer(classifier_pb2_grpc.MBertClassifierServicer):
    def Classify(self, request, context):
        result = predict(request.text)
        return classifier_pb2.Classification(
            label=result["label"],
            confidence=result["confidence"],
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    classifier_pb2_grpc.add_MBertClassifierServicer_to_server(ClassifierServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server listening on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
