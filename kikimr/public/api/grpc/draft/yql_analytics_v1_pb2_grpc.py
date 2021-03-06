# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kikimr.public.api.protos.draft import yql_analytics_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2


class AnalyticsServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ExecuteQuery = channel.unary_unary(
        '/Yql.Analytics.V1.AnalyticsService/ExecuteQuery',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2.ExecuteQueryRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2.ExecuteQueryResponse.FromString,
        )
    self.GetResultInfo = channel.unary_unary(
        '/Yql.Analytics.V1.AnalyticsService/GetResultInfo',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2.GetResultInfoRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2.GetResultInfoResponse.FromString,
        )
    self.GetResultData = channel.unary_unary(
        '/Yql.Analytics.V1.AnalyticsService/GetResultData',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2.GetResultDataRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2.GetResultDataResponse.FromString,
        )


class AnalyticsServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ExecuteQuery(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetResultInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetResultData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AnalyticsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ExecuteQuery': grpc.unary_unary_rpc_method_handler(
          servicer.ExecuteQuery,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2.ExecuteQueryRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2.ExecuteQueryResponse.SerializeToString,
      ),
      'GetResultInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetResultInfo,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2.GetResultInfoRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2.GetResultInfoResponse.SerializeToString,
      ),
      'GetResultData': grpc.unary_unary_rpc_method_handler(
          servicer.GetResultData,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2.GetResultDataRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yql__analytics__pb2.GetResultDataResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Yql.Analytics.V1.AnalyticsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
