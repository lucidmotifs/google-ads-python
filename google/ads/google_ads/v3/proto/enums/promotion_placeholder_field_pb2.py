# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/enums/promotion_placeholder_field.proto

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
  name='google/ads/googleads_v3/proto/enums/promotion_placeholder_field.proto',
  package='google.ads.googleads.v3.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v3.enumsB\036PromotionPlaceholderFieldProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V3.Enums\312\002\035Google\\Ads\\GoogleAds\\V3\\Enums\352\002!Google::Ads::GoogleAds::V3::Enums'),
  serialized_pb=_b('\nEgoogle/ads/googleads_v3/proto/enums/promotion_placeholder_field.proto\x12\x1dgoogle.ads.googleads.v3.enums\x1a\x1cgoogle/api/annotations.proto\"\xee\x02\n\x1dPromotionPlaceholderFieldEnum\"\xcc\x02\n\x19PromotionPlaceholderField\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x14\n\x10PROMOTION_TARGET\x10\x02\x12\x15\n\x11\x44ISCOUNT_MODIFIER\x10\x03\x12\x0f\n\x0bPERCENT_OFF\x10\x04\x12\x14\n\x10MONEY_AMOUNT_OFF\x10\x05\x12\x12\n\x0ePROMOTION_CODE\x10\x06\x12\x16\n\x12ORDERS_OVER_AMOUNT\x10\x07\x12\x13\n\x0fPROMOTION_START\x10\x08\x12\x11\n\rPROMOTION_END\x10\t\x12\x0c\n\x08OCCASION\x10\n\x12\x0e\n\nFINAL_URLS\x10\x0b\x12\x15\n\x11\x46INAL_MOBILE_URLS\x10\x0c\x12\x10\n\x0cTRACKING_URL\x10\r\x12\x0c\n\x08LANGUAGE\x10\x0e\x12\x14\n\x10\x46INAL_URL_SUFFIX\x10\x0f\x42\xf3\x01\n!com.google.ads.googleads.v3.enumsB\x1ePromotionPlaceholderFieldProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V3.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V3\\Enums\xea\x02!Google::Ads::GoogleAds::V3::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_PROMOTIONPLACEHOLDERFIELDENUM_PROMOTIONPLACEHOLDERFIELD = _descriptor.EnumDescriptor(
  name='PromotionPlaceholderField',
  full_name='google.ads.googleads.v3.enums.PromotionPlaceholderFieldEnum.PromotionPlaceholderField',
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
      name='PROMOTION_TARGET', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCOUNT_MODIFIER', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERCENT_OFF', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONEY_AMOUNT_OFF', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTION_CODE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDERS_OVER_AMOUNT', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTION_START', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTION_END', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OCCASION', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINAL_URLS', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINAL_MOBILE_URLS', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRACKING_URL', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LANGUAGE', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINAL_URL_SUFFIX', index=15, number=15,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=169,
  serialized_end=501,
)
_sym_db.RegisterEnumDescriptor(_PROMOTIONPLACEHOLDERFIELDENUM_PROMOTIONPLACEHOLDERFIELD)


_PROMOTIONPLACEHOLDERFIELDENUM = _descriptor.Descriptor(
  name='PromotionPlaceholderFieldEnum',
  full_name='google.ads.googleads.v3.enums.PromotionPlaceholderFieldEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROMOTIONPLACEHOLDERFIELDENUM_PROMOTIONPLACEHOLDERFIELD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=501,
)

_PROMOTIONPLACEHOLDERFIELDENUM_PROMOTIONPLACEHOLDERFIELD.containing_type = _PROMOTIONPLACEHOLDERFIELDENUM
DESCRIPTOR.message_types_by_name['PromotionPlaceholderFieldEnum'] = _PROMOTIONPLACEHOLDERFIELDENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PromotionPlaceholderFieldEnum = _reflection.GeneratedProtocolMessageType('PromotionPlaceholderFieldEnum', (_message.Message,), dict(
  DESCRIPTOR = _PROMOTIONPLACEHOLDERFIELDENUM,
  __module__ = 'google.ads.googleads_v3.proto.enums.promotion_placeholder_field_pb2'
  ,
  __doc__ = """Values for Promotion placeholder fields.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.enums.PromotionPlaceholderFieldEnum)
  ))
_sym_db.RegisterMessage(PromotionPlaceholderFieldEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
