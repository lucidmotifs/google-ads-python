# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/enums/frequency_cap_time_unit.proto

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
  name='google/ads/googleads_v3/proto/enums/frequency_cap_time_unit.proto',
  package='google.ads.googleads.v3.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v3.enumsB\031FrequencyCapTimeUnitProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V3.Enums\312\002\035Google\\Ads\\GoogleAds\\V3\\Enums\352\002!Google::Ads::GoogleAds::V3::Enums'),
  serialized_pb=_b('\nAgoogle/ads/googleads_v3/proto/enums/frequency_cap_time_unit.proto\x12\x1dgoogle.ads.googleads.v3.enums\x1a\x1cgoogle/api/annotations.proto\"n\n\x18\x46requencyCapTimeUnitEnum\"R\n\x14\x46requencyCapTimeUnit\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x07\n\x03\x44\x41Y\x10\x02\x12\x08\n\x04WEEK\x10\x03\x12\t\n\x05MONTH\x10\x04\x42\xee\x01\n!com.google.ads.googleads.v3.enumsB\x19\x46requencyCapTimeUnitProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V3.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V3\\Enums\xea\x02!Google::Ads::GoogleAds::V3::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FREQUENCYCAPTIMEUNITENUM_FREQUENCYCAPTIMEUNIT = _descriptor.EnumDescriptor(
  name='FrequencyCapTimeUnit',
  full_name='google.ads.googleads.v3.enums.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit',
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
      name='DAY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEEK', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONTH', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=158,
  serialized_end=240,
)
_sym_db.RegisterEnumDescriptor(_FREQUENCYCAPTIMEUNITENUM_FREQUENCYCAPTIMEUNIT)


_FREQUENCYCAPTIMEUNITENUM = _descriptor.Descriptor(
  name='FrequencyCapTimeUnitEnum',
  full_name='google.ads.googleads.v3.enums.FrequencyCapTimeUnitEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FREQUENCYCAPTIMEUNITENUM_FREQUENCYCAPTIMEUNIT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=240,
)

_FREQUENCYCAPTIMEUNITENUM_FREQUENCYCAPTIMEUNIT.containing_type = _FREQUENCYCAPTIMEUNITENUM
DESCRIPTOR.message_types_by_name['FrequencyCapTimeUnitEnum'] = _FREQUENCYCAPTIMEUNITENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FrequencyCapTimeUnitEnum = _reflection.GeneratedProtocolMessageType('FrequencyCapTimeUnitEnum', (_message.Message,), dict(
  DESCRIPTOR = _FREQUENCYCAPTIMEUNITENUM,
  __module__ = 'google.ads.googleads_v3.proto.enums.frequency_cap_time_unit_pb2'
  ,
  __doc__ = """Container for enum describing the unit of time the cap is defined at.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.enums.FrequencyCapTimeUnitEnum)
  ))
_sym_db.RegisterMessage(FrequencyCapTimeUnitEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
