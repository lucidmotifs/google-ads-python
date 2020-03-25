# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v3.proto.resources import ad_group_ad_label_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_ad__group__ad__label__pb2
from google.ads.google_ads.v3.proto.services import ad_group_ad_label_service_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_ad__group__ad__label__service__pb2


class AdGroupAdLabelServiceStub(object):
  """Proto file describing the Ad Group Ad Label service.

  Service to manage labels on ad group ads.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAdGroupAdLabel = channel.unary_unary(
        '/google.ads.googleads.v3.services.AdGroupAdLabelService/GetAdGroupAdLabel',
        request_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_ad__group__ad__label__service__pb2.GetAdGroupAdLabelRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_ad__group__ad__label__pb2.AdGroupAdLabel.FromString,
        )
    self.MutateAdGroupAdLabels = channel.unary_unary(
        '/google.ads.googleads.v3.services.AdGroupAdLabelService/MutateAdGroupAdLabels',
        request_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_ad__group__ad__label__service__pb2.MutateAdGroupAdLabelsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_ad__group__ad__label__service__pb2.MutateAdGroupAdLabelsResponse.FromString,
        )


class AdGroupAdLabelServiceServicer(object):
  """Proto file describing the Ad Group Ad Label service.

  Service to manage labels on ad group ads.
  """

  def GetAdGroupAdLabel(self, request, context):
    """Returns the requested ad group ad label in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateAdGroupAdLabels(self, request, context):
    """Creates and removes ad group ad labels.
    Operation statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdGroupAdLabelServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAdGroupAdLabel': grpc.unary_unary_rpc_method_handler(
          servicer.GetAdGroupAdLabel,
          request_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_ad__group__ad__label__service__pb2.GetAdGroupAdLabelRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_ad__group__ad__label__pb2.AdGroupAdLabel.SerializeToString,
      ),
      'MutateAdGroupAdLabels': grpc.unary_unary_rpc_method_handler(
          servicer.MutateAdGroupAdLabels,
          request_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_ad__group__ad__label__service__pb2.MutateAdGroupAdLabelsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_ad__group__ad__label__service__pb2.MutateAdGroupAdLabelsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v3.services.AdGroupAdLabelService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
