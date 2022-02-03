# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import history_pb2 as history__pb2


class HistoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
            "/HistoryService/Get",
            request_serializer=history__pb2.HistoryRequest.SerializeToString,
            response_deserializer=history__pb2.HistoryResponse.FromString,
        )


class HistoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_HistoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Get": grpc.unary_unary_rpc_method_handler(
            servicer.Get,
            request_deserializer=history__pb2.HistoryRequest.FromString,
            response_serializer=history__pb2.HistoryResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "HistoryService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class HistoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/HistoryService/Get",
            history__pb2.HistoryRequest.SerializeToString,
            history__pb2.HistoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
