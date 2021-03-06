# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import service_pb2 as service__pb2


class WorkerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ForwardMode = channel.unary_unary(
                '/Worker/ForwardMode',
                request_serializer=service__pb2.ForwardRequest.SerializeToString,
                response_deserializer=service__pb2.ForwardReply.FromString,
                )
        self.BackwardMode = channel.unary_unary(
                '/Worker/BackwardMode',
                request_serializer=service__pb2.BackwardRequest.SerializeToString,
                response_deserializer=service__pb2.BackwardReply.FromString,
                )
        self.ResetState = channel.unary_unary(
                '/Worker/ResetState',
                request_serializer=service__pb2.EmptyMessage.SerializeToString,
                response_deserializer=service__pb2.EmptyMessage.FromString,
                )


class WorkerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ForwardMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BackwardMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ForwardMode': grpc.unary_unary_rpc_method_handler(
                    servicer.ForwardMode,
                    request_deserializer=service__pb2.ForwardRequest.FromString,
                    response_serializer=service__pb2.ForwardReply.SerializeToString,
            ),
            'BackwardMode': grpc.unary_unary_rpc_method_handler(
                    servicer.BackwardMode,
                    request_deserializer=service__pb2.BackwardRequest.FromString,
                    response_serializer=service__pb2.BackwardReply.SerializeToString,
            ),
            'ResetState': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetState,
                    request_deserializer=service__pb2.EmptyMessage.FromString,
                    response_serializer=service__pb2.EmptyMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Worker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Worker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ForwardMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Worker/ForwardMode',
            service__pb2.ForwardRequest.SerializeToString,
            service__pb2.ForwardReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BackwardMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Worker/BackwardMode',
            service__pb2.BackwardRequest.SerializeToString,
            service__pb2.BackwardReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Worker/ResetState',
            service__pb2.EmptyMessage.SerializeToString,
            service__pb2.EmptyMessage.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
