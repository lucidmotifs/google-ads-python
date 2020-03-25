# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/errors/media_upload_error.proto

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
  name='google/ads/googleads_v3/proto/errors/media_upload_error.proto',
  package='google.ads.googleads.v3.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v3.errorsB\025MediaUploadErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v3/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V3.Errors\312\002\036Google\\Ads\\GoogleAds\\V3\\Errors\352\002\"Google::Ads::GoogleAds::V3::Errors'),
  serialized_pb=_b('\n=google/ads/googleads_v3/proto/errors/media_upload_error.proto\x12\x1egoogle.ads.googleads.v3.errors\x1a\x1cgoogle/api/annotations.proto\"\x8b\x02\n\x14MediaUploadErrorEnum\"\xf2\x01\n\x10MediaUploadError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x10\n\x0c\x46ILE_TOO_BIG\x10\x02\x12\x15\n\x11UNPARSEABLE_IMAGE\x10\x03\x12\x1e\n\x1a\x41NIMATED_IMAGE_NOT_ALLOWED\x10\x04\x12\x16\n\x12\x46ORMAT_NOT_ALLOWED\x10\x05\x12\x1c\n\x18\x45XTERNAL_URL_NOT_ALLOWED\x10\x06\x12\x19\n\x15INVALID_URL_REFERENCE\x10\x07\x12&\n\"MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY\x10\x08\x42\xf0\x01\n\"com.google.ads.googleads.v3.errorsB\x15MediaUploadErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v3/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V3.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V3\\Errors\xea\x02\"Google::Ads::GoogleAds::V3::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_MEDIAUPLOADERRORENUM_MEDIAUPLOADERROR = _descriptor.EnumDescriptor(
  name='MediaUploadError',
  full_name='google.ads.googleads.v3.errors.MediaUploadErrorEnum.MediaUploadError',
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
      name='FILE_TOO_BIG', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNPARSEABLE_IMAGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANIMATED_IMAGE_NOT_ALLOWED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORMAT_NOT_ALLOWED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL_URL_NOT_ALLOWED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_URL_REFERENCE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=153,
  serialized_end=395,
)
_sym_db.RegisterEnumDescriptor(_MEDIAUPLOADERRORENUM_MEDIAUPLOADERROR)


_MEDIAUPLOADERRORENUM = _descriptor.Descriptor(
  name='MediaUploadErrorEnum',
  full_name='google.ads.googleads.v3.errors.MediaUploadErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MEDIAUPLOADERRORENUM_MEDIAUPLOADERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=395,
)

_MEDIAUPLOADERRORENUM_MEDIAUPLOADERROR.containing_type = _MEDIAUPLOADERRORENUM
DESCRIPTOR.message_types_by_name['MediaUploadErrorEnum'] = _MEDIAUPLOADERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MediaUploadErrorEnum = _reflection.GeneratedProtocolMessageType('MediaUploadErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _MEDIAUPLOADERRORENUM,
  __module__ = 'google.ads.googleads_v3.proto.errors.media_upload_error_pb2'
  ,
  __doc__ = """Container for enum describing possible media uploading errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.errors.MediaUploadErrorEnum)
  ))
_sym_db.RegisterMessage(MediaUploadErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
