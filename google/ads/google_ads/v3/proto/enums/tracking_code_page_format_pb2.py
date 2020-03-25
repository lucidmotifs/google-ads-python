# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/enums/tracking_code_page_format.proto

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
  name='google/ads/googleads_v3/proto/enums/tracking_code_page_format.proto',
  package='google.ads.googleads.v3.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v3.enumsB\033TrackingCodePageFormatProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V3.Enums\312\002\035Google\\Ads\\GoogleAds\\V3\\Enums\352\002!Google::Ads::GoogleAds::V3::Enums'),
  serialized_pb=_b('\nCgoogle/ads/googleads_v3/proto/enums/tracking_code_page_format.proto\x12\x1dgoogle.ads.googleads.v3.enums\x1a\x1cgoogle/api/annotations.proto\"g\n\x1aTrackingCodePageFormatEnum\"I\n\x16TrackingCodePageFormat\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x08\n\x04HTML\x10\x02\x12\x07\n\x03\x41MP\x10\x03\x42\xf0\x01\n!com.google.ads.googleads.v3.enumsB\x1bTrackingCodePageFormatProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V3.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V3\\Enums\xea\x02!Google::Ads::GoogleAds::V3::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_TRACKINGCODEPAGEFORMATENUM_TRACKINGCODEPAGEFORMAT = _descriptor.EnumDescriptor(
  name='TrackingCodePageFormat',
  full_name='google.ads.googleads.v3.enums.TrackingCodePageFormatEnum.TrackingCodePageFormat',
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
      name='HTML', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AMP', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=162,
  serialized_end=235,
)
_sym_db.RegisterEnumDescriptor(_TRACKINGCODEPAGEFORMATENUM_TRACKINGCODEPAGEFORMAT)


_TRACKINGCODEPAGEFORMATENUM = _descriptor.Descriptor(
  name='TrackingCodePageFormatEnum',
  full_name='google.ads.googleads.v3.enums.TrackingCodePageFormatEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRACKINGCODEPAGEFORMATENUM_TRACKINGCODEPAGEFORMAT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=235,
)

_TRACKINGCODEPAGEFORMATENUM_TRACKINGCODEPAGEFORMAT.containing_type = _TRACKINGCODEPAGEFORMATENUM
DESCRIPTOR.message_types_by_name['TrackingCodePageFormatEnum'] = _TRACKINGCODEPAGEFORMATENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrackingCodePageFormatEnum = _reflection.GeneratedProtocolMessageType('TrackingCodePageFormatEnum', (_message.Message,), dict(
  DESCRIPTOR = _TRACKINGCODEPAGEFORMATENUM,
  __module__ = 'google.ads.googleads_v3.proto.enums.tracking_code_page_format_pb2'
  ,
  __doc__ = """Container for enum describing the format of the web page where the
  tracking tag and snippet will be installed.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.enums.TrackingCodePageFormatEnum)
  ))
_sym_db.RegisterMessage(TrackingCodePageFormatEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
