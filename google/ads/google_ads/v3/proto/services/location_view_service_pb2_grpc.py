# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v3.proto.resources import location_view_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_location__view__pb2
from google.ads.google_ads.v3.proto.services import location_view_service_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_location__view__service__pb2


class LocationViewServiceStub(object):
  """Proto file describing the Location View service.

  Service to fetch location views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetLocationView = channel.unary_unary(
        '/google.ads.googleads.v3.services.LocationViewService/GetLocationView',
        request_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_location__view__service__pb2.GetLocationViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_location__view__pb2.LocationView.FromString,
        )


class LocationViewServiceServicer(object):
  """Proto file describing the Location View service.

  Service to fetch location views.
  """

  def GetLocationView(self, request, context):
    """Returns the requested location view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LocationViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetLocationView': grpc.unary_unary_rpc_method_handler(
          servicer.GetLocationView,
          request_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_location__view__service__pb2.GetLocationViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_location__view__pb2.LocationView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v3.services.LocationViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
