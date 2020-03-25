# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v3.proto.resources import topic_constant_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_topic__constant__pb2
from google.ads.google_ads.v3.proto.services import topic_constant_service_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_topic__constant__service__pb2


class TopicConstantServiceStub(object):
  """Proto file describing the Topic constant service

  Service to fetch topic constants.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetTopicConstant = channel.unary_unary(
        '/google.ads.googleads.v3.services.TopicConstantService/GetTopicConstant',
        request_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_topic__constant__service__pb2.GetTopicConstantRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_topic__constant__pb2.TopicConstant.FromString,
        )


class TopicConstantServiceServicer(object):
  """Proto file describing the Topic constant service

  Service to fetch topic constants.
  """

  def GetTopicConstant(self, request, context):
    """Returns the requested topic constant in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TopicConstantServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetTopicConstant': grpc.unary_unary_rpc_method_handler(
          servicer.GetTopicConstant,
          request_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_topic__constant__service__pb2.GetTopicConstantRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_topic__constant__pb2.TopicConstant.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v3.services.TopicConstantService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
