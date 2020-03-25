# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/enums/reach_plan_network.proto

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
  name='google/ads/googleads_v3/proto/enums/reach_plan_network.proto',
  package='google.ads.googleads.v3.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v3.enumsB\025ReachPlanNetworkProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V3.Enums\312\002\035Google\\Ads\\GoogleAds\\V3\\Enums\352\002!Google::Ads::GoogleAds::V3::Enums'),
  serialized_pb=_b('\n<google/ads/googleads_v3/proto/enums/reach_plan_network.proto\x12\x1dgoogle.ads.googleads.v3.enums\x1a\x1cgoogle/api/annotations.proto\"\x97\x01\n\x14ReachPlanNetworkEnum\"\x7f\n\x10ReachPlanNetwork\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07YOUTUBE\x10\x02\x12\x19\n\x15GOOGLE_VIDEO_PARTNERS\x10\x03\x12%\n!YOUTUBE_AND_GOOGLE_VIDEO_PARTNERS\x10\x04\x42\xea\x01\n!com.google.ads.googleads.v3.enumsB\x15ReachPlanNetworkProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V3.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V3\\Enums\xea\x02!Google::Ads::GoogleAds::V3::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_REACHPLANNETWORKENUM_REACHPLANNETWORK = _descriptor.EnumDescriptor(
  name='ReachPlanNetwork',
  full_name='google.ads.googleads.v3.enums.ReachPlanNetworkEnum.ReachPlanNetwork',
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
      name='YOUTUBE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_VIDEO_PARTNERS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE_AND_GOOGLE_VIDEO_PARTNERS', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=150,
  serialized_end=277,
)
_sym_db.RegisterEnumDescriptor(_REACHPLANNETWORKENUM_REACHPLANNETWORK)


_REACHPLANNETWORKENUM = _descriptor.Descriptor(
  name='ReachPlanNetworkEnum',
  full_name='google.ads.googleads.v3.enums.ReachPlanNetworkEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REACHPLANNETWORKENUM_REACHPLANNETWORK,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=277,
)

_REACHPLANNETWORKENUM_REACHPLANNETWORK.containing_type = _REACHPLANNETWORKENUM
DESCRIPTOR.message_types_by_name['ReachPlanNetworkEnum'] = _REACHPLANNETWORKENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReachPlanNetworkEnum = _reflection.GeneratedProtocolMessageType('ReachPlanNetworkEnum', (_message.Message,), dict(
  DESCRIPTOR = _REACHPLANNETWORKENUM,
  __module__ = 'google.ads.googleads_v3.proto.enums.reach_plan_network_pb2'
  ,
  __doc__ = """Container for enum describing plannable networks.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.enums.ReachPlanNetworkEnum)
  ))
_sym_db.RegisterMessage(ReachPlanNetworkEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
