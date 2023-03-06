# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto_aiservice_pb2 as proto__aiservice__pb2


class AiServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Predict = channel.unary_unary(
                '/AiService/Predict',
                request_serializer=proto__aiservice__pb2.PredictRequest.SerializeToString,
                response_deserializer=proto__aiservice__pb2.PredictResponse.FromString,
                )


class AiServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Predict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AiServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Predict': grpc.unary_unary_rpc_method_handler(
                    servicer.Predict,
                    request_deserializer=proto__aiservice__pb2.PredictRequest.FromString,
                    response_serializer=proto__aiservice__pb2.PredictResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AiService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AiService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Predict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AiService/Predict',
            proto__aiservice__pb2.PredictRequest.SerializeToString,
            proto__aiservice__pb2.PredictResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class GateServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Report = channel.unary_unary(
                '/GateService/Report',
                request_serializer=proto__aiservice__pb2.ReportRequest.SerializeToString,
                response_deserializer=proto__aiservice__pb2.ReportResponse.FromString,
                )


class GateServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Report(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Report': grpc.unary_unary_rpc_method_handler(
                    servicer.Report,
                    request_deserializer=proto__aiservice__pb2.ReportRequest.FromString,
                    response_serializer=proto__aiservice__pb2.ReportResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GateService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Report(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GateService/Report',
            proto__aiservice__pb2.ReportRequest.SerializeToString,
            proto__aiservice__pb2.ReportResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
