# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kikimr.public.api.protos import ydb_scheme_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2


class SchemeServiceStub(object):
  """Every YDB Database Instance has set of objects organized a tree.
  SchemeService provides some functionality to browse and modify
  this tree.
  SchemeService provides a generic tree functionality, to create specific
  objects like YDB Table or Persistent Queue use corresponding services.

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.MakeDirectory = channel.unary_unary(
        '/Ydb.Scheme.V1.SchemeService/MakeDirectory',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.MakeDirectoryRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.MakeDirectoryResponse.FromString,
        )
    self.RemoveDirectory = channel.unary_unary(
        '/Ydb.Scheme.V1.SchemeService/RemoveDirectory',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.RemoveDirectoryRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.RemoveDirectoryResponse.FromString,
        )
    self.ListDirectory = channel.unary_unary(
        '/Ydb.Scheme.V1.SchemeService/ListDirectory',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.ListDirectoryRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.ListDirectoryResponse.FromString,
        )
    self.DescribePath = channel.unary_unary(
        '/Ydb.Scheme.V1.SchemeService/DescribePath',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.DescribePathRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.DescribePathResponse.FromString,
        )
    self.ModifyPermissions = channel.unary_unary(
        '/Ydb.Scheme.V1.SchemeService/ModifyPermissions',
        request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.ModifyPermissionsRequest.SerializeToString,
        response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.ModifyPermissionsResponse.FromString,
        )


class SchemeServiceServicer(object):
  """Every YDB Database Instance has set of objects organized a tree.
  SchemeService provides some functionality to browse and modify
  this tree.
  SchemeService provides a generic tree functionality, to create specific
  objects like YDB Table or Persistent Queue use corresponding services.

  """

  def MakeDirectory(self, request, context):
    """Make Directory.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveDirectory(self, request, context):
    """Remove Directory.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListDirectory(self, request, context):
    """Returns information about given directory and objects inside it.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DescribePath(self, request, context):
    """Returns information about object with given path.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModifyPermissions(self, request, context):
    """Modify permissions.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SchemeServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'MakeDirectory': grpc.unary_unary_rpc_method_handler(
          servicer.MakeDirectory,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.MakeDirectoryRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.MakeDirectoryResponse.SerializeToString,
      ),
      'RemoveDirectory': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveDirectory,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.RemoveDirectoryRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.RemoveDirectoryResponse.SerializeToString,
      ),
      'ListDirectory': grpc.unary_unary_rpc_method_handler(
          servicer.ListDirectory,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.ListDirectoryRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.ListDirectoryResponse.SerializeToString,
      ),
      'DescribePath': grpc.unary_unary_rpc_method_handler(
          servicer.DescribePath,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.DescribePathRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.DescribePathResponse.SerializeToString,
      ),
      'ModifyPermissions': grpc.unary_unary_rpc_method_handler(
          servicer.ModifyPermissions,
          request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.ModifyPermissionsRequest.FromString,
          response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_ydb__scheme__pb2.ModifyPermissionsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Ydb.Scheme.V1.SchemeService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
