import grpc
import classifier_pb2
import classifier_pb2_grpc


def classify(text: str) -> classifier_pb2.Classification:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = classifier_pb2_grpc.MBertClassifierStub(channel)
        return stub.Classify(classifier_pb2.ClassificationRequest(text=text))


# if __name__ == "__main__":
#     import sys

#     text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter text: ")
#     result = classify(text)
#     print(f"Label:      {result.label}")
#     print(f"Confidence: {result.confidence:.1%}")
