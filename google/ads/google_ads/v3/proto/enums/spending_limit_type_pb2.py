# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/enums/spending_limit_type.proto

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
  name='google/ads/googleads_v3/proto/enums/spending_limit_type.proto',
  package='google.ads.googleads.v3.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v3.enumsB\026SpendingLimitTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V3.Enums\312\002\035Google\\Ads\\GoogleAds\\V3\\Enums\352\002!Google::Ads::GoogleAds::V3::Enums'),
  serialized_pb=_b('\n=google/ads/googleads_v3/proto/enums/spending_limit_type.proto\x12\x1dgoogle.ads.googleads.v3.enums\x1a\x1cgoogle/api/annotations.proto\"X\n\x15SpendingLimitTypeEnum\"?\n\x11SpendingLimitType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0c\n\x08INFINITE\x10\x02\x42\xeb\x01\n!com.google.ads.googleads.v3.enumsB\x16SpendingLimitTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V3.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V3\\Enums\xea\x02!Google::Ads::GoogleAds::V3::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_SPENDINGLIMITTYPEENUM_SPENDINGLIMITTYPE = _descriptor.EnumDescriptor(
  name='SpendingLimitType',
  full_name='google.ads.googleads.v3.enums.SpendingLimitTypeEnum.SpendingLimitType',
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
      name='INFINITE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=151,
  serialized_end=214,
)
_sym_db.RegisterEnumDescriptor(_SPENDINGLIMITTYPEENUM_SPENDINGLIMITTYPE)


_SPENDINGLIMITTYPEENUM = _descriptor.Descriptor(
  name='SpendingLimitTypeEnum',
  full_name='google.ads.googleads.v3.enums.SpendingLimitTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SPENDINGLIMITTYPEENUM_SPENDINGLIMITTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=214,
)

_SPENDINGLIMITTYPEENUM_SPENDINGLIMITTYPE.containing_type = _SPENDINGLIMITTYPEENUM
DESCRIPTOR.message_types_by_name['SpendingLimitTypeEnum'] = _SPENDINGLIMITTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpendingLimitTypeEnum = _reflection.GeneratedProtocolMessageType('SpendingLimitTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _SPENDINGLIMITTYPEENUM,
  __module__ = 'google.ads.googleads_v3.proto.enums.spending_limit_type_pb2'
  ,
  __doc__ = """Message describing spending limit types.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.enums.SpendingLimitTypeEnum)
  ))
_sym_db.RegisterMessage(SpendingLimitTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
