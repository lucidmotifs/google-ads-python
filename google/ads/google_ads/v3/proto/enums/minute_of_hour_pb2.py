# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/enums/minute_of_hour.proto

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
  name='google/ads/googleads_v3/proto/enums/minute_of_hour.proto',
  package='google.ads.googleads.v3.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v3.enumsB\021MinuteOfHourProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V3.Enums\312\002\035Google\\Ads\\GoogleAds\\V3\\Enums\352\002!Google::Ads::GoogleAds::V3::Enums'),
  serialized_pb=_b('\n8google/ads/googleads_v3/proto/enums/minute_of_hour.proto\x12\x1dgoogle.ads.googleads.v3.enums\x1a\x1cgoogle/api/annotations.proto\"s\n\x10MinuteOfHourEnum\"_\n\x0cMinuteOfHour\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x08\n\x04ZERO\x10\x02\x12\x0b\n\x07\x46IFTEEN\x10\x03\x12\n\n\x06THIRTY\x10\x04\x12\x0e\n\nFORTY_FIVE\x10\x05\x42\xe6\x01\n!com.google.ads.googleads.v3.enumsB\x11MinuteOfHourProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V3.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V3\\Enums\xea\x02!Google::Ads::GoogleAds::V3::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_MINUTEOFHOURENUM_MINUTEOFHOUR = _descriptor.EnumDescriptor(
  name='MinuteOfHour',
  full_name='google.ads.googleads.v3.enums.MinuteOfHourEnum.MinuteOfHour',
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
      name='ZERO', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIFTEEN', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THIRTY', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORTY_FIVE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=141,
  serialized_end=236,
)
_sym_db.RegisterEnumDescriptor(_MINUTEOFHOURENUM_MINUTEOFHOUR)


_MINUTEOFHOURENUM = _descriptor.Descriptor(
  name='MinuteOfHourEnum',
  full_name='google.ads.googleads.v3.enums.MinuteOfHourEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MINUTEOFHOURENUM_MINUTEOFHOUR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=236,
)

_MINUTEOFHOURENUM_MINUTEOFHOUR.containing_type = _MINUTEOFHOURENUM
DESCRIPTOR.message_types_by_name['MinuteOfHourEnum'] = _MINUTEOFHOURENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MinuteOfHourEnum = _reflection.GeneratedProtocolMessageType('MinuteOfHourEnum', (_message.Message,), dict(
  DESCRIPTOR = _MINUTEOFHOURENUM,
  __module__ = 'google.ads.googleads_v3.proto.enums.minute_of_hour_pb2'
  ,
  __doc__ = """Container for enumeration of quarter-hours.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.enums.MinuteOfHourEnum)
  ))
_sym_db.RegisterMessage(MinuteOfHourEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
