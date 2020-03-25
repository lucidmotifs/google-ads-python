# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v1.proto.resources import group_placement_view_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_group__placement__view__pb2
from google.ads.google_ads.v1.proto.services import group_placement_view_service_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_group__placement__view__service__pb2


class GroupPlacementViewServiceStub(object):
  """Proto file describing the Group Placement View service.

  Service to fetch Group Placement views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetGroupPlacementView = channel.unary_unary(
        '/google.ads.googleads.v1.services.GroupPlacementViewService/GetGroupPlacementView',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_group__placement__view__service__pb2.GetGroupPlacementViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_group__placement__view__pb2.GroupPlacementView.FromString,
        )


class GroupPlacementViewServiceServicer(object):
  """Proto file describing the Group Placement View service.

  Service to fetch Group Placement views.
  """

  def GetGroupPlacementView(self, request, context):
    """Returns the requested Group Placement view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GroupPlacementViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetGroupPlacementView': grpc.unary_unary_rpc_method_handler(
          servicer.GetGroupPlacementView,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_group__placement__view__service__pb2.GetGroupPlacementViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_group__placement__view__pb2.GroupPlacementView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.GroupPlacementViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
