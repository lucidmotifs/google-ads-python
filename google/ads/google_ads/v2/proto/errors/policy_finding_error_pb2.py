# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/errors/policy_finding_error.proto

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
  name='google/ads/googleads_v2/proto/errors/policy_finding_error.proto',
  package='google.ads.googleads.v2.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v2.errorsB\027PolicyFindingErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V2.Errors\312\002\036Google\\Ads\\GoogleAds\\V2\\Errors\352\002\"Google::Ads::GoogleAds::V2::Errors'),
  serialized_pb=_b('\n?google/ads/googleads_v2/proto/errors/policy_finding_error.proto\x12\x1egoogle.ads.googleads.v2.errors\x1a\x1cgoogle/api/annotations.proto\"|\n\x16PolicyFindingErrorEnum\"b\n\x12PolicyFindingError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x12\n\x0ePOLICY_FINDING\x10\x02\x12\x1a\n\x16POLICY_TOPIC_NOT_FOUND\x10\x03\x42\xf2\x01\n\"com.google.ads.googleads.v2.errorsB\x17PolicyFindingErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V2.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V2\\Errors\xea\x02\"Google::Ads::GoogleAds::V2::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_POLICYFINDINGERRORENUM_POLICYFINDINGERROR = _descriptor.EnumDescriptor(
  name='PolicyFindingError',
  full_name='google.ads.googleads.v2.errors.PolicyFindingErrorEnum.PolicyFindingError',
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
      name='POLICY_FINDING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POLICY_TOPIC_NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=155,
  serialized_end=253,
)
_sym_db.RegisterEnumDescriptor(_POLICYFINDINGERRORENUM_POLICYFINDINGERROR)


_POLICYFINDINGERRORENUM = _descriptor.Descriptor(
  name='PolicyFindingErrorEnum',
  full_name='google.ads.googleads.v2.errors.PolicyFindingErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POLICYFINDINGERRORENUM_POLICYFINDINGERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=253,
)

_POLICYFINDINGERRORENUM_POLICYFINDINGERROR.containing_type = _POLICYFINDINGERRORENUM
DESCRIPTOR.message_types_by_name['PolicyFindingErrorEnum'] = _POLICYFINDINGERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PolicyFindingErrorEnum = _reflection.GeneratedProtocolMessageType('PolicyFindingErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _POLICYFINDINGERRORENUM,
  __module__ = 'google.ads.googleads_v2.proto.errors.policy_finding_error_pb2'
  ,
  __doc__ = """Container for enum describing possible policy finding errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.errors.PolicyFindingErrorEnum)
  ))
_sym_db.RegisterMessage(PolicyFindingErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
