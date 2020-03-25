# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/enums/media_type.proto

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
  name='google/ads/googleads_v2/proto/enums/media_type.proto',
  package='google.ads.googleads.v2.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v2.enumsB\016MediaTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V2.Enums\312\002\035Google\\Ads\\GoogleAds\\V2\\Enums\352\002!Google::Ads::GoogleAds::V2::Enums'),
  serialized_pb=_b('\n4google/ads/googleads_v2/proto/enums/media_type.proto\x12\x1dgoogle.ads.googleads.v2.enums\x1a\x1cgoogle/api/annotations.proto\"\x8a\x01\n\rMediaTypeEnum\"y\n\tMediaType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\t\n\x05IMAGE\x10\x02\x12\x08\n\x04ICON\x10\x03\x12\x10\n\x0cMEDIA_BUNDLE\x10\x04\x12\t\n\x05\x41UDIO\x10\x05\x12\t\n\x05VIDEO\x10\x06\x12\x11\n\rDYNAMIC_IMAGE\x10\x07\x42\xe3\x01\n!com.google.ads.googleads.v2.enumsB\x0eMediaTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V2.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V2\\Enums\xea\x02!Google::Ads::GoogleAds::V2::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_MEDIATYPEENUM_MEDIATYPE = _descriptor.EnumDescriptor(
  name='MediaType',
  full_name='google.ads.googleads.v2.enums.MediaTypeEnum.MediaType',
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
      name='IMAGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICON', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIA_BUNDLE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIO', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DYNAMIC_IMAGE', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=135,
  serialized_end=256,
)
_sym_db.RegisterEnumDescriptor(_MEDIATYPEENUM_MEDIATYPE)


_MEDIATYPEENUM = _descriptor.Descriptor(
  name='MediaTypeEnum',
  full_name='google.ads.googleads.v2.enums.MediaTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MEDIATYPEENUM_MEDIATYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=256,
)

_MEDIATYPEENUM_MEDIATYPE.containing_type = _MEDIATYPEENUM
DESCRIPTOR.message_types_by_name['MediaTypeEnum'] = _MEDIATYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MediaTypeEnum = _reflection.GeneratedProtocolMessageType('MediaTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _MEDIATYPEENUM,
  __module__ = 'google.ads.googleads_v2.proto.enums.media_type_pb2'
  ,
  __doc__ = """Container for enum describing the types of media.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.enums.MediaTypeEnum)
  ))
_sym_db.RegisterMessage(MediaTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
