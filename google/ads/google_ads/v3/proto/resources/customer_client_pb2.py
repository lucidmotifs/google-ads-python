# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/resources/customer_client.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/resources/customer_client.proto',
  package='google.ads.googleads.v3.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v3.resourcesB\023CustomerClientProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V3.Resources\312\002!Google\\Ads\\GoogleAds\\V3\\Resources\352\002%Google::Ads::GoogleAds::V3::Resources'),
  serialized_pb=_b('\n=google/ads/googleads_v3/proto/resources/customer_client.proto\x12!google.ads.googleads.v3.resources\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xc2\x04\n\x0e\x43ustomerClient\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x35\n\x0f\x63lient_customer\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x06hidden\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x05level\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12/\n\ttime_zone\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\x0ctest_account\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12+\n\x07manager\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x10\x64\x65scriptive_name\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rcurrency_code\x18\n \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\'\n\x02id\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int64Value:d\xea\x41\x61\n\'googleads.googleapis.com/CustomerClient\x12\x36\x63ustomers/{customer}/customerClients/{customer_client}B\x80\x02\n%com.google.ads.googleads.v3.resourcesB\x13\x43ustomerClientProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V3.Resources\xca\x02!Google\\Ads\\GoogleAds\\V3\\Resources\xea\x02%Google::Ads::GoogleAds::V3::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CUSTOMERCLIENT = _descriptor.Descriptor(
  name='CustomerClient',
  full_name='google.ads.googleads.v3.resources.CustomerClient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.resources.CustomerClient.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_customer', full_name='google.ads.googleads.v3.resources.CustomerClient.client_customer', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hidden', full_name='google.ads.googleads.v3.resources.CustomerClient.hidden', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='google.ads.googleads.v3.resources.CustomerClient.level', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_zone', full_name='google.ads.googleads.v3.resources.CustomerClient.time_zone', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_account', full_name='google.ads.googleads.v3.resources.CustomerClient.test_account', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manager', full_name='google.ads.googleads.v3.resources.CustomerClient.manager', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descriptive_name', full_name='google.ads.googleads.v3.resources.CustomerClient.descriptive_name', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency_code', full_name='google.ads.googleads.v3.resources.CustomerClient.currency_code', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v3.resources.CustomerClient.id', index=9,
      number=11, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('\352Aa\n\'googleads.googleapis.com/CustomerClient\0226customers/{customer}/customerClients/{customer_client}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=768,
)

_CUSTOMERCLIENT.fields_by_name['client_customer'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMERCLIENT.fields_by_name['hidden'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CUSTOMERCLIENT.fields_by_name['level'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CUSTOMERCLIENT.fields_by_name['time_zone'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMERCLIENT.fields_by_name['test_account'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CUSTOMERCLIENT.fields_by_name['manager'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CUSTOMERCLIENT.fields_by_name['descriptive_name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMERCLIENT.fields_by_name['currency_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMERCLIENT.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['CustomerClient'] = _CUSTOMERCLIENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomerClient = _reflection.GeneratedProtocolMessageType('CustomerClient', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMERCLIENT,
  __module__ = 'google.ads.googleads_v3.proto.resources.customer_client_pb2'
  ,
  __doc__ = """A link between the given customer and a client customer. CustomerClients
  only exist for manager customers. All direct and indirect client
  customers are included, as well as the manager itself.
  
  
  Attributes:
      resource_name:
          The resource name of the customer client. CustomerClient
          resource names have the form: ``customers/{customer_id}/custom
          erClients/{client_customer_id}``
      client_customer:
          The resource name of the client-customer which is linked to
          the given customer. Read only.
      hidden:
          Specifies whether this is a `hidden account
          <https://support.google.com/google-ads/answer/7519830>`__.
          Read only.
      level:
          Distance between given customer and client. For self link, the
          level value will be 0. Read only.
      time_zone:
          Common Locale Data Repository (CLDR) string representation of
          the time zone of the client, e.g. America/Los\_Angeles. Read
          only.
      test_account:
          Identifies if the client is a test account. Read only.
      manager:
          Identifies if the client is a manager. Read only.
      descriptive_name:
          Descriptive name for the client. Read only.
      currency_code:
          Currency code (e.g. 'USD', 'EUR') for the client. Read only.
      id:
          The ID of the client customer. Read only.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.CustomerClient)
  ))
_sym_db.RegisterMessage(CustomerClient)


DESCRIPTOR._options = None
_CUSTOMERCLIENT._options = None
# @@protoc_insertion_point(module_scope)
