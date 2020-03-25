# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/errors/campaign_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/errors/campaign_error.proto',
  package='google.ads.googleads.v1.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v1.errorsB\022CampaignErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Errors\312\002\036Google\\Ads\\GoogleAds\\V1\\Errors\352\002\"Google::Ads::GoogleAds::V1::Errors'),
  serialized_pb=_b('\n9google/ads/googleads_v1/proto/errors/campaign_error.proto\x12\x1egoogle.ads.googleads.v1.errors\x1a\x1cgoogle/api/annotations.proto\"\x99\r\n\x11\x43\x61mpaignErrorEnum\"\x83\r\n\rCampaignError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12!\n\x1d\x43\x41NNOT_TARGET_CONTENT_NETWORK\x10\x03\x12 \n\x1c\x43\x41NNOT_TARGET_SEARCH_NETWORK\x10\x04\x12\x36\n2CANNOT_TARGET_SEARCH_NETWORK_WITHOUT_GOOGLE_SEARCH\x10\x05\x12\x30\n,CANNOT_TARGET_GOOGLE_SEARCH_FOR_CPM_CAMPAIGN\x10\x06\x12-\n)CAMPAIGN_MUST_TARGET_AT_LEAST_ONE_NETWORK\x10\x07\x12(\n$CANNOT_TARGET_PARTNER_SEARCH_NETWORK\x10\x08\x12K\nGCANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CRITERIA_LEVEL_BIDDING_STRATEGY\x10\t\x12\x36\n2CAMPAIGN_DURATION_MUST_CONTAIN_ALL_RUNNABLE_TRIALS\x10\n\x12$\n CANNOT_MODIFY_FOR_TRIAL_CAMPAIGN\x10\x0b\x12\x1b\n\x17\x44UPLICATE_CAMPAIGN_NAME\x10\x0c\x12\x1f\n\x1bINCOMPATIBLE_CAMPAIGN_FIELD\x10\r\x12\x19\n\x15INVALID_CAMPAIGN_NAME\x10\x0e\x12*\n&INVALID_AD_SERVING_OPTIMIZATION_STATUS\x10\x0f\x12\x18\n\x14INVALID_TRACKING_URL\x10\x10\x12>\n:CANNOT_SET_BOTH_TRACKING_URL_TEMPLATE_AND_TRACKING_SETTING\x10\x11\x12 \n\x1cMAX_IMPRESSIONS_NOT_IN_RANGE\x10\x12\x12\x1b\n\x17TIME_UNIT_NOT_SUPPORTED\x10\x13\x12\x31\n-INVALID_OPERATION_IF_SERVING_STATUS_HAS_ENDED\x10\x14\x12\x1b\n\x17\x42UDGET_CANNOT_BE_SHARED\x10\x15\x12%\n!CAMPAIGN_CANNOT_USE_SHARED_BUDGET\x10\x16\x12\x30\n,CANNOT_CHANGE_BUDGET_ON_CAMPAIGN_WITH_TRIALS\x10\x17\x12!\n\x1d\x43\x41MPAIGN_LABEL_DOES_NOT_EXIST\x10\x18\x12!\n\x1d\x43\x41MPAIGN_LABEL_ALREADY_EXISTS\x10\x19\x12\x1c\n\x18MISSING_SHOPPING_SETTING\x10\x1a\x12\"\n\x1eINVALID_SHOPPING_SALES_COUNTRY\x10\x1b\x12*\n&MISSING_UNIVERSAL_APP_CAMPAIGN_SETTING\x10\x1e\x12;\n7ADVERTISING_CHANNEL_TYPE_NOT_AVAILABLE_FOR_ACCOUNT_TYPE\x10\x1f\x12(\n$INVALID_ADVERTISING_CHANNEL_SUB_TYPE\x10 \x12,\n(AT_LEAST_ONE_CONVERSION_MUST_BE_SELECTED\x10!\x12\x1f\n\x1b\x43\x41NNOT_SET_AD_ROTATION_MODE\x10\"\x12/\n+CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED\x10#\x12\x1b\n\x17\x43\x41NNOT_SET_DATE_TO_PAST\x10$\x12\x1f\n\x1bMISSING_HOTEL_CUSTOMER_LINK\x10%\x12\x1f\n\x1bINVALID_HOTEL_CUSTOMER_LINK\x10&\x12\x19\n\x15MISSING_HOTEL_SETTING\x10\'\x12\x42\n>CANNOT_USE_SHARED_CAMPAIGN_BUDGET_WHILE_PART_OF_CAMPAIGN_GROUP\x10(\x12\x11\n\rAPP_NOT_FOUND\x10)\x12\x39\n5SHOPPING_ENABLE_LOCAL_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE\x10*\x12\x33\n/MERCHANT_NOT_ALLOWED_FOR_COMPARISON_LISTING_ADS\x10+B\xed\x01\n\"com.google.ads.googleads.v1.errorsB\x12\x43\x61mpaignErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Errors\xea\x02\"Google::Ads::GoogleAds::V1::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CAMPAIGNERRORENUM_CAMPAIGNERROR = _descriptor.EnumDescriptor(
  name='CampaignError',
  full_name='google.ads.googleads.v1.errors.CampaignErrorEnum.CampaignError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_TARGET_CONTENT_NETWORK', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_TARGET_SEARCH_NETWORK', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_TARGET_SEARCH_NETWORK_WITHOUT_GOOGLE_SEARCH', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_TARGET_GOOGLE_SEARCH_FOR_CPM_CAMPAIGN', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_MUST_TARGET_AT_LEAST_ONE_NETWORK', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_TARGET_PARTNER_SEARCH_NETWORK', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CRITERIA_LEVEL_BIDDING_STRATEGY', index=8, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_DURATION_MUST_CONTAIN_ALL_RUNNABLE_TRIALS', index=9, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_MODIFY_FOR_TRIAL_CAMPAIGN', index=10, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_CAMPAIGN_NAME', index=11, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOMPATIBLE_CAMPAIGN_FIELD', index=12, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CAMPAIGN_NAME', index=13, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_AD_SERVING_OPTIMIZATION_STATUS', index=14, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_TRACKING_URL', index=15, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_BOTH_TRACKING_URL_TEMPLATE_AND_TRACKING_SETTING', index=16, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_IMPRESSIONS_NOT_IN_RANGE', index=17, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIME_UNIT_NOT_SUPPORTED', index=18, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_OPERATION_IF_SERVING_STATUS_HAS_ENDED', index=19, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDGET_CANNOT_BE_SHARED', index=20, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_CANNOT_USE_SHARED_BUDGET', index=21, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CHANGE_BUDGET_ON_CAMPAIGN_WITH_TRIALS', index=22, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_LABEL_DOES_NOT_EXIST', index=23, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_LABEL_ALREADY_EXISTS', index=24, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_SHOPPING_SETTING', index=25, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SHOPPING_SALES_COUNTRY', index=26, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_UNIVERSAL_APP_CAMPAIGN_SETTING', index=27, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADVERTISING_CHANNEL_TYPE_NOT_AVAILABLE_FOR_ACCOUNT_TYPE', index=28, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ADVERTISING_CHANNEL_SUB_TYPE', index=29, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AT_LEAST_ONE_CONVERSION_MUST_BE_SELECTED', index=30, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_AD_ROTATION_MODE', index=31, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED', index=32, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_DATE_TO_PAST', index=33, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_HOTEL_CUSTOMER_LINK', index=34, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_HOTEL_CUSTOMER_LINK', index=35, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_HOTEL_SETTING', index=36, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_USE_SHARED_CAMPAIGN_BUDGET_WHILE_PART_OF_CAMPAIGN_GROUP', index=37, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APP_NOT_FOUND', index=38, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOPPING_ENABLE_LOCAL_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE', index=39, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MERCHANT_NOT_ALLOWED_FOR_COMPARISON_LISTING_ADS', index=40, number=43,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=146,
  serialized_end=1813,
)
_sym_db.RegisterEnumDescriptor(_CAMPAIGNERRORENUM_CAMPAIGNERROR)


_CAMPAIGNERRORENUM = _descriptor.Descriptor(
  name='CampaignErrorEnum',
  full_name='google.ads.googleads.v1.errors.CampaignErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CAMPAIGNERRORENUM_CAMPAIGNERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=1813,
)

_CAMPAIGNERRORENUM_CAMPAIGNERROR.containing_type = _CAMPAIGNERRORENUM
DESCRIPTOR.message_types_by_name['CampaignErrorEnum'] = _CAMPAIGNERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignErrorEnum = _reflection.GeneratedProtocolMessageType('CampaignErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNERRORENUM,
  __module__ = 'google.ads.googleads_v1.proto.errors.campaign_error_pb2'
  ,
  __doc__ = """Container for enum describing possible campaign errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.errors.CampaignErrorEnum)
  ))
_sym_db.RegisterMessage(CampaignErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
