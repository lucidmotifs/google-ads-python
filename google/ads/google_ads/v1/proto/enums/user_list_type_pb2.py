# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/user_list_type.proto

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
  name='google/ads/googleads_v1/proto/enums/user_list_type.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\021UserListTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\n8google/ads/googleads_v1/proto/enums/user_list_type.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\xa5\x01\n\x10UserListTypeEnum\"\x90\x01\n\x0cUserListType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0f\n\x0bREMARKETING\x10\x02\x12\x0b\n\x07LOGICAL\x10\x03\x12\x18\n\x14\x45XTERNAL_REMARKETING\x10\x04\x12\x0e\n\nRULE_BASED\x10\x05\x12\x0b\n\x07SIMILAR\x10\x06\x12\r\n\tCRM_BASED\x10\x07\x42\xe6\x01\n!com.google.ads.googleads.v1.enumsB\x11UserListTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_USERLISTTYPEENUM_USERLISTTYPE = _descriptor.EnumDescriptor(
  name='UserListType',
  full_name='google.ads.googleads.v1.enums.UserListTypeEnum.UserListType',
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
      name='REMARKETING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGICAL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL_REMARKETING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RULE_BASED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIMILAR', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRM_BASED', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=143,
  serialized_end=287,
)
_sym_db.RegisterEnumDescriptor(_USERLISTTYPEENUM_USERLISTTYPE)


_USERLISTTYPEENUM = _descriptor.Descriptor(
  name='UserListTypeEnum',
  full_name='google.ads.googleads.v1.enums.UserListTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USERLISTTYPEENUM_USERLISTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=287,
)

_USERLISTTYPEENUM_USERLISTTYPE.containing_type = _USERLISTTYPEENUM
DESCRIPTOR.message_types_by_name['UserListTypeEnum'] = _USERLISTTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserListTypeEnum = _reflection.GeneratedProtocolMessageType('UserListTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _USERLISTTYPEENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.user_list_type_pb2'
  ,
  __doc__ = """The user list types.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.UserListTypeEnum)
  ))
_sym_db.RegisterMessage(UserListTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
