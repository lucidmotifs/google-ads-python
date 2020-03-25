# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v2.proto.resources import customer_feed_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_customer__feed__pb2
from google.ads.google_ads.v2.proto.services import customer_feed_service_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_customer__feed__service__pb2


class CustomerFeedServiceStub(object):
  """Proto file describing the CustomerFeed service.

  Service to manage customer feeds.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCustomerFeed = channel.unary_unary(
        '/google.ads.googleads.v2.services.CustomerFeedService/GetCustomerFeed',
        request_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_customer__feed__service__pb2.GetCustomerFeedRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_customer__feed__pb2.CustomerFeed.FromString,
        )
    self.MutateCustomerFeeds = channel.unary_unary(
        '/google.ads.googleads.v2.services.CustomerFeedService/MutateCustomerFeeds',
        request_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_customer__feed__service__pb2.MutateCustomerFeedsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_customer__feed__service__pb2.MutateCustomerFeedsResponse.FromString,
        )


class CustomerFeedServiceServicer(object):
  """Proto file describing the CustomerFeed service.

  Service to manage customer feeds.
  """

  def GetCustomerFeed(self, request, context):
    """Returns the requested customer feed in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateCustomerFeeds(self, request, context):
    """Creates, updates, or removes customer feeds. Operation statuses are
    returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CustomerFeedServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCustomerFeed': grpc.unary_unary_rpc_method_handler(
          servicer.GetCustomerFeed,
          request_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_customer__feed__service__pb2.GetCustomerFeedRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_customer__feed__pb2.CustomerFeed.SerializeToString,
      ),
      'MutateCustomerFeeds': grpc.unary_unary_rpc_method_handler(
          servicer.MutateCustomerFeeds,
          request_deserializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_customer__feed__service__pb2.MutateCustomerFeedsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_customer__feed__service__pb2.MutateCustomerFeedsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v2.services.CustomerFeedService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
