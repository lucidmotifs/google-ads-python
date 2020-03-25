# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/enums/click_type.proto

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
  name='google/ads/googleads_v3/proto/enums/click_type.proto',
  package='google.ads.googleads.v3.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v3.enumsB\016ClickTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V3.Enums\312\002\035Google\\Ads\\GoogleAds\\V3\\Enums\352\002!Google::Ads::GoogleAds::V3::Enums'),
  serialized_pb=_b('\n4google/ads/googleads_v3/proto/enums/click_type.proto\x12\x1dgoogle.ads.googleads.v3.enums\x1a\x1cgoogle/api/annotations.proto\"\xa6\x0c\n\rClickTypeEnum\"\x94\x0c\n\tClickType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x10\n\x0c\x41PP_DEEPLINK\x10\x02\x12\x0f\n\x0b\x42READCRUMBS\x10\x03\x12\x12\n\x0e\x42ROADBAND_PLAN\x10\x04\x12\x11\n\rCALL_TRACKING\x10\x05\x12\t\n\x05\x43\x41LLS\x10\x06\x12\x1a\n\x16\x43LICK_ON_ENGAGEMENT_AD\x10\x07\x12\x12\n\x0eGET_DIRECTIONS\x10\x08\x12\x16\n\x12LOCATION_EXPANSION\x10\t\x12\x18\n\x14LOCATION_FORMAT_CALL\x10\n\x12\x1e\n\x1aLOCATION_FORMAT_DIRECTIONS\x10\x0b\x12\x19\n\x15LOCATION_FORMAT_IMAGE\x10\x0c\x12 \n\x1cLOCATION_FORMAT_LANDING_PAGE\x10\r\x12\x17\n\x13LOCATION_FORMAT_MAP\x10\x0e\x12\x1e\n\x1aLOCATION_FORMAT_STORE_INFO\x10\x0f\x12\x18\n\x14LOCATION_FORMAT_TEXT\x10\x10\x12\x18\n\x14MOBILE_CALL_TRACKING\x10\x11\x12\x10\n\x0cOFFER_PRINTS\x10\x12\x12\t\n\x05OTHER\x10\x13\x12\x1c\n\x18PRODUCT_EXTENSION_CLICKS\x10\x14\x12\x1d\n\x19PRODUCT_LISTING_AD_CLICKS\x10\x15\x12\r\n\tSITELINKS\x10\x16\x12\x11\n\rSTORE_LOCATOR\x10\x17\x12\x0e\n\nURL_CLICKS\x10\x19\x12\x1a\n\x16VIDEO_APP_STORE_CLICKS\x10\x1a\x12\x1f\n\x1bVIDEO_CALL_TO_ACTION_CLICKS\x10\x1b\x12%\n!VIDEO_CARD_ACTION_HEADLINE_CLICKS\x10\x1c\x12\x18\n\x14VIDEO_END_CAP_CLICKS\x10\x1d\x12\x18\n\x14VIDEO_WEBSITE_CLICKS\x10\x1e\x12\x14\n\x10VISUAL_SITELINKS\x10\x1f\x12\x11\n\rWIRELESS_PLAN\x10 \x12\x1c\n\x18PRODUCT_LISTING_AD_LOCAL\x10!\x12)\n%PRODUCT_LISTING_AD_MULTICHANNEL_LOCAL\x10\"\x12*\n&PRODUCT_LISTING_AD_MULTICHANNEL_ONLINE\x10#\x12\x1e\n\x1aPRODUCT_LISTING_ADS_COUPON\x10$\x12#\n\x1fPRODUCT_LISTING_AD_TRANSACTABLE\x10%\x12\x1b\n\x17PRODUCT_AD_APP_DEEPLINK\x10&\x12\x1d\n\x19SHOWCASE_AD_CATEGORY_LINK\x10\'\x12%\n!SHOWCASE_AD_LOCAL_STOREFRONT_LINK\x10(\x12#\n\x1fSHOWCASE_AD_ONLINE_PRODUCT_LINK\x10*\x12\"\n\x1eSHOWCASE_AD_LOCAL_PRODUCT_LINK\x10+\x12\x17\n\x13PROMOTION_EXTENSION\x10,\x12!\n\x1dSWIPEABLE_GALLERY_AD_HEADLINE\x10-\x12\x1f\n\x1bSWIPEABLE_GALLERY_AD_SWIPES\x10.\x12!\n\x1dSWIPEABLE_GALLERY_AD_SEE_MORE\x10/\x12%\n!SWIPEABLE_GALLERY_AD_SITELINK_ONE\x10\x30\x12%\n!SWIPEABLE_GALLERY_AD_SITELINK_TWO\x10\x31\x12\'\n#SWIPEABLE_GALLERY_AD_SITELINK_THREE\x10\x32\x12&\n\"SWIPEABLE_GALLERY_AD_SITELINK_FOUR\x10\x33\x12&\n\"SWIPEABLE_GALLERY_AD_SITELINK_FIVE\x10\x34\x12\x0f\n\x0bHOTEL_PRICE\x10\x35\x12\x13\n\x0fPRICE_EXTENSION\x10\x36\x12\'\n#HOTEL_BOOK_ON_GOOGLE_ROOM_SELECTION\x10\x37\x12\x1f\n\x1bSHOPPING_COMPARISON_LISTING\x10\x38\x42\xe3\x01\n!com.google.ads.googleads.v3.enumsB\x0e\x43lickTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V3.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V3\\Enums\xea\x02!Google::Ads::GoogleAds::V3::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CLICKTYPEENUM_CLICKTYPE = _descriptor.EnumDescriptor(
  name='ClickType',
  full_name='google.ads.googleads.v3.enums.ClickTypeEnum.ClickType',
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
      name='APP_DEEPLINK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BREADCRUMBS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROADBAND_PLAN', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_TRACKING', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALLS', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLICK_ON_ENGAGEMENT_AD', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_DIRECTIONS', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_EXPANSION', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_FORMAT_CALL', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_FORMAT_DIRECTIONS', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_FORMAT_IMAGE', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_FORMAT_LANDING_PAGE', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_FORMAT_MAP', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_FORMAT_STORE_INFO', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_FORMAT_TEXT', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOBILE_CALL_TRACKING', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFFER_PRINTS', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_EXTENSION_CLICKS', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_LISTING_AD_CLICKS', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SITELINKS', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORE_LOCATOR', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_CLICKS', index=24, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_APP_STORE_CLICKS', index=25, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_CALL_TO_ACTION_CLICKS', index=26, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_CARD_ACTION_HEADLINE_CLICKS', index=27, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_END_CAP_CLICKS', index=28, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_WEBSITE_CLICKS', index=29, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VISUAL_SITELINKS', index=30, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIRELESS_PLAN', index=31, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_LISTING_AD_LOCAL', index=32, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_LISTING_AD_MULTICHANNEL_LOCAL', index=33, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_LISTING_AD_MULTICHANNEL_ONLINE', index=34, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_LISTING_ADS_COUPON', index=35, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_LISTING_AD_TRANSACTABLE', index=36, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_AD_APP_DEEPLINK', index=37, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOWCASE_AD_CATEGORY_LINK', index=38, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOWCASE_AD_LOCAL_STOREFRONT_LINK', index=39, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOWCASE_AD_ONLINE_PRODUCT_LINK', index=40, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOWCASE_AD_LOCAL_PRODUCT_LINK', index=41, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTION_EXTENSION', index=42, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SWIPEABLE_GALLERY_AD_HEADLINE', index=43, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SWIPEABLE_GALLERY_AD_SWIPES', index=44, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SWIPEABLE_GALLERY_AD_SEE_MORE', index=45, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SWIPEABLE_GALLERY_AD_SITELINK_ONE', index=46, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SWIPEABLE_GALLERY_AD_SITELINK_TWO', index=47, number=49,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SWIPEABLE_GALLERY_AD_SITELINK_THREE', index=48, number=50,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SWIPEABLE_GALLERY_AD_SITELINK_FOUR', index=49, number=51,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SWIPEABLE_GALLERY_AD_SITELINK_FIVE', index=50, number=52,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOTEL_PRICE', index=51, number=53,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE_EXTENSION', index=52, number=54,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOTEL_BOOK_ON_GOOGLE_ROOM_SELECTION', index=53, number=55,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOPPING_COMPARISON_LISTING', index=54, number=56,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=136,
  serialized_end=1692,
)
_sym_db.RegisterEnumDescriptor(_CLICKTYPEENUM_CLICKTYPE)


_CLICKTYPEENUM = _descriptor.Descriptor(
  name='ClickTypeEnum',
  full_name='google.ads.googleads.v3.enums.ClickTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLICKTYPEENUM_CLICKTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=1692,
)

_CLICKTYPEENUM_CLICKTYPE.containing_type = _CLICKTYPEENUM
DESCRIPTOR.message_types_by_name['ClickTypeEnum'] = _CLICKTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClickTypeEnum = _reflection.GeneratedProtocolMessageType('ClickTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _CLICKTYPEENUM,
  __module__ = 'google.ads.googleads_v3.proto.enums.click_type_pb2'
  ,
  __doc__ = """Container for enumeration of Google Ads click types.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.enums.ClickTypeEnum)
  ))
_sym_db.RegisterMessage(ClickTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
