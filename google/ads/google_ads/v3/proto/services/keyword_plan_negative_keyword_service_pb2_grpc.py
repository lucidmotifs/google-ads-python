# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v3.proto.resources import keyword_plan_negative_keyword_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_keyword__plan__negative__keyword__pb2
from google.ads.google_ads.v3.proto.services import keyword_plan_negative_keyword_service_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_keyword__plan__negative__keyword__service__pb2


class KeywordPlanNegativeKeywordServiceStub(object):
  """Proto file describing the keyword plan negative keyword service.

  Service to manage Keyword Plan negative keywords.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetKeywordPlanNegativeKeyword = channel.unary_unary(
        '/google.ads.googleads.v3.services.KeywordPlanNegativeKeywordService/GetKeywordPlanNegativeKeyword',
        request_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_keyword__plan__negative__keyword__service__pb2.GetKeywordPlanNegativeKeywordRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_keyword__plan__negative__keyword__pb2.KeywordPlanNegativeKeyword.FromString,
        )
    self.MutateKeywordPlanNegativeKeywords = channel.unary_unary(
        '/google.ads.googleads.v3.services.KeywordPlanNegativeKeywordService/MutateKeywordPlanNegativeKeywords',
        request_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_keyword__plan__negative__keyword__service__pb2.MutateKeywordPlanNegativeKeywordsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_keyword__plan__negative__keyword__service__pb2.MutateKeywordPlanNegativeKeywordsResponse.FromString,
        )


class KeywordPlanNegativeKeywordServiceServicer(object):
  """Proto file describing the keyword plan negative keyword service.

  Service to manage Keyword Plan negative keywords.
  """

  def GetKeywordPlanNegativeKeyword(self, request, context):
    """Returns the requested plan in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateKeywordPlanNegativeKeywords(self, request, context):
    """Creates, updates, or removes Keyword Plan negative keywords. Operation
    statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_KeywordPlanNegativeKeywordServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetKeywordPlanNegativeKeyword': grpc.unary_unary_rpc_method_handler(
          servicer.GetKeywordPlanNegativeKeyword,
          request_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_keyword__plan__negative__keyword__service__pb2.GetKeywordPlanNegativeKeywordRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_keyword__plan__negative__keyword__pb2.KeywordPlanNegativeKeyword.SerializeToString,
      ),
      'MutateKeywordPlanNegativeKeywords': grpc.unary_unary_rpc_method_handler(
          servicer.MutateKeywordPlanNegativeKeywords,
          request_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_keyword__plan__negative__keyword__service__pb2.MutateKeywordPlanNegativeKeywordsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_keyword__plan__negative__keyword__service__pb2.MutateKeywordPlanNegativeKeywordsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v3.services.KeywordPlanNegativeKeywordService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
