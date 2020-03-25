# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v1.proto.resources import paid_organic_search_term_view_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_paid__organic__search__term__view__pb2
from google.ads.google_ads.v1.proto.services import paid_organic_search_term_view_service_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_paid__organic__search__term__view__service__pb2


class PaidOrganicSearchTermViewServiceStub(object):
  """Proto file describing the Paid Organic Search Term View service.

  Service to fetch paid organic search term views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetPaidOrganicSearchTermView = channel.unary_unary(
        '/google.ads.googleads.v1.services.PaidOrganicSearchTermViewService/GetPaidOrganicSearchTermView',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_paid__organic__search__term__view__service__pb2.GetPaidOrganicSearchTermViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_paid__organic__search__term__view__pb2.PaidOrganicSearchTermView.FromString,
        )


class PaidOrganicSearchTermViewServiceServicer(object):
  """Proto file describing the Paid Organic Search Term View service.

  Service to fetch paid organic search term views.
  """

  def GetPaidOrganicSearchTermView(self, request, context):
    """Returns the requested paid organic search term view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PaidOrganicSearchTermViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetPaidOrganicSearchTermView': grpc.unary_unary_rpc_method_handler(
          servicer.GetPaidOrganicSearchTermView,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_paid__organic__search__term__view__service__pb2.GetPaidOrganicSearchTermViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_paid__organic__search__term__view__pb2.PaidOrganicSearchTermView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.PaidOrganicSearchTermViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
