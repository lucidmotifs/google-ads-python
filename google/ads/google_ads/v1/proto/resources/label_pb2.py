# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/resources/label.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.common import text_label_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_text__label__pb2
from google.ads.google_ads.v1.proto.enums import label_status_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_label__status__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/resources/label.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v1.resourcesB\nLabelProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources'),
  serialized_pb=_b('\n3google/ads/googleads_v1/proto/resources/label.proto\x12!google.ads.googleads.v1.resources\x1a\x35google/ads/googleads_v1/proto/common/text_label.proto\x1a\x36google/ads/googleads_v1/proto/enums/label_status.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xfe\x01\n\x05Label\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x04name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12J\n\x06status\x18\x04 \x01(\x0e\x32:.google.ads.googleads.v1.enums.LabelStatusEnum.LabelStatus\x12=\n\ntext_label\x18\x05 \x01(\x0b\x32).google.ads.googleads.v1.common.TextLabelB\xf7\x01\n%com.google.ads.googleads.v1.resourcesB\nLabelProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_text__label__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_label__status__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='google.ads.googleads.v1.resources.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.Label.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v1.resources.Label.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v1.resources.Label.name', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v1.resources.Label.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_label', full_name='google.ads.googleads.v1.resources.Label.text_label', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=518,
)

_LABEL.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_LABEL.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_LABEL.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_label__status__pb2._LABELSTATUSENUM_LABELSTATUS
_LABEL.fields_by_name['text_label'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_text__label__pb2._TEXTLABEL
DESCRIPTOR.message_types_by_name['Label'] = _LABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), dict(
  DESCRIPTOR = _LABEL,
  __module__ = 'google.ads.googleads_v1.proto.resources.label_pb2'
  ,
  __doc__ = """A label.
  
  
  Attributes:
      resource_name:
          Name of the resource. Label resource names have the form:
          ``customers/{customer_id}/labels/{label_id}``
      id:
          Id of the label. Read only.
      name:
          The name of the label.  This field is required and should not
          be empty when creating a new label.  The length of this string
          should be between 1 and 80, inclusive.
      status:
          Status of the label. Read only.
      text_label:
          A type of label displaying text on a colored background.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.Label)
  ))
_sym_db.RegisterMessage(Label)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
