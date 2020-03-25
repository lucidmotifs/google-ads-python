# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/services/feed_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.resources import feed_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_feed__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/services/feed_service.proto',
  package='google.ads.googleads.v3.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v3.servicesB\020FeedServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V3.Services\312\002 Google\\Ads\\GoogleAds\\V3\\Services\352\002$Google::Ads::GoogleAds::V3::Services'),
  serialized_pb=_b('\n9google/ads/googleads_v3/proto/services/feed_service.proto\x12 google.ads.googleads.v3.services\x1a\x32google/ads/googleads_v3/proto/resources/feed.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\",\n\x0eGetFeedRequest\x12\x1a\n\rresource_name\x18\x01 \x01(\tB\x03\xe0\x41\x02\"\xa8\x01\n\x12MutateFeedsRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12H\n\noperations\x18\x02 \x03(\x0b\x32/.google.ads.googleads.v3.services.FeedOperationB\x03\xe0\x41\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\xd5\x01\n\rFeedOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x39\n\x06\x63reate\x18\x01 \x01(\x0b\x32\'.google.ads.googleads.v3.resources.FeedH\x00\x12\x39\n\x06update\x18\x02 \x01(\x0b\x32\'.google.ads.googleads.v3.resources.FeedH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\x8d\x01\n\x13MutateFeedsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12\x43\n\x07results\x18\x02 \x03(\x0b\x32\x32.google.ads.googleads.v3.services.MutateFeedResult\")\n\x10MutateFeedResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\x9f\x03\n\x0b\x46\x65\x65\x64Service\x12\xa5\x01\n\x07GetFeed\x12\x30.google.ads.googleads.v3.services.GetFeedRequest\x1a\'.google.ads.googleads.v3.resources.Feed\"?\x82\xd3\xe4\x93\x02)\x12\'/v3/{resource_name=customers/*/feeds/*}\xda\x41\rresource_name\x12\xca\x01\n\x0bMutateFeeds\x12\x34.google.ads.googleads.v3.services.MutateFeedsRequest\x1a\x35.google.ads.googleads.v3.services.MutateFeedsResponse\"N\x82\xd3\xe4\x93\x02/\"*/v3/customers/{customer_id=*}/feeds:mutate:\x01*\xda\x41\x16\x63ustomer_id,operations\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xf7\x01\n$com.google.ads.googleads.v3.servicesB\x10\x46\x65\x65\x64ServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V3.Services\xca\x02 Google\\Ads\\GoogleAds\\V3\\Services\xea\x02$Google::Ads::GoogleAds::V3::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_feed__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETFEEDREQUEST = _descriptor.Descriptor(
  name='GetFeedRequest',
  full_name='google.ads.googleads.v3.services.GetFeedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.services.GetFeedRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
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
  serialized_start=294,
  serialized_end=338,
)


_MUTATEFEEDSREQUEST = _descriptor.Descriptor(
  name='MutateFeedsRequest',
  full_name='google.ads.googleads.v3.services.MutateFeedsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v3.services.MutateFeedsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v3.services.MutateFeedsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v3.services.MutateFeedsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v3.services.MutateFeedsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=341,
  serialized_end=509,
)


_FEEDOPERATION = _descriptor.Descriptor(
  name='FeedOperation',
  full_name='google.ads.googleads.v3.services.FeedOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v3.services.FeedOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v3.services.FeedOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v3.services.FeedOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v3.services.FeedOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v3.services.FeedOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=512,
  serialized_end=725,
)


_MUTATEFEEDSRESPONSE = _descriptor.Descriptor(
  name='MutateFeedsResponse',
  full_name='google.ads.googleads.v3.services.MutateFeedsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v3.services.MutateFeedsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v3.services.MutateFeedsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=728,
  serialized_end=869,
)


_MUTATEFEEDRESULT = _descriptor.Descriptor(
  name='MutateFeedResult',
  full_name='google.ads.googleads.v3.services.MutateFeedResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.services.MutateFeedResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=871,
  serialized_end=912,
)

_MUTATEFEEDSREQUEST.fields_by_name['operations'].message_type = _FEEDOPERATION
_FEEDOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_FEEDOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_feed__pb2._FEED
_FEEDOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_feed__pb2._FEED
_FEEDOPERATION.oneofs_by_name['operation'].fields.append(
  _FEEDOPERATION.fields_by_name['create'])
_FEEDOPERATION.fields_by_name['create'].containing_oneof = _FEEDOPERATION.oneofs_by_name['operation']
_FEEDOPERATION.oneofs_by_name['operation'].fields.append(
  _FEEDOPERATION.fields_by_name['update'])
_FEEDOPERATION.fields_by_name['update'].containing_oneof = _FEEDOPERATION.oneofs_by_name['operation']
_FEEDOPERATION.oneofs_by_name['operation'].fields.append(
  _FEEDOPERATION.fields_by_name['remove'])
_FEEDOPERATION.fields_by_name['remove'].containing_oneof = _FEEDOPERATION.oneofs_by_name['operation']
_MUTATEFEEDSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATEFEEDSRESPONSE.fields_by_name['results'].message_type = _MUTATEFEEDRESULT
DESCRIPTOR.message_types_by_name['GetFeedRequest'] = _GETFEEDREQUEST
DESCRIPTOR.message_types_by_name['MutateFeedsRequest'] = _MUTATEFEEDSREQUEST
DESCRIPTOR.message_types_by_name['FeedOperation'] = _FEEDOPERATION
DESCRIPTOR.message_types_by_name['MutateFeedsResponse'] = _MUTATEFEEDSRESPONSE
DESCRIPTOR.message_types_by_name['MutateFeedResult'] = _MUTATEFEEDRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFeedRequest = _reflection.GeneratedProtocolMessageType('GetFeedRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFEEDREQUEST,
  __module__ = 'google.ads.googleads_v3.proto.services.feed_service_pb2'
  ,
  __doc__ = """Request message for
  [FeedService.GetFeed][google.ads.googleads.v3.services.FeedService.GetFeed].
  
  
  Attributes:
      resource_name:
          Required. The resource name of the feed to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.GetFeedRequest)
  ))
_sym_db.RegisterMessage(GetFeedRequest)

MutateFeedsRequest = _reflection.GeneratedProtocolMessageType('MutateFeedsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEFEEDSREQUEST,
  __module__ = 'google.ads.googleads_v3.proto.services.feed_service_pb2'
  ,
  __doc__ = """Request message for
  [FeedService.MutateFeeds][google.ads.googleads.v3.services.FeedService.MutateFeeds].
  
  
  Attributes:
      customer_id:
          Required. The ID of the customer whose feeds are being
          modified.
      operations:
          Required. The list of operations to perform on individual
          feeds.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.MutateFeedsRequest)
  ))
_sym_db.RegisterMessage(MutateFeedsRequest)

FeedOperation = _reflection.GeneratedProtocolMessageType('FeedOperation', (_message.Message,), dict(
  DESCRIPTOR = _FEEDOPERATION,
  __module__ = 'google.ads.googleads_v3.proto.services.feed_service_pb2'
  ,
  __doc__ = """A single operation (create, update, remove) on an feed.
  
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          feed.
      update:
          Update operation: The feed is expected to have a valid
          resource name.
      remove:
          Remove operation: A resource name for the removed feed is
          expected, in this format:
          ``customers/{customer_id}/feeds/{feed_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.FeedOperation)
  ))
_sym_db.RegisterMessage(FeedOperation)

MutateFeedsResponse = _reflection.GeneratedProtocolMessageType('MutateFeedsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEFEEDSRESPONSE,
  __module__ = 'google.ads.googleads_v3.proto.services.feed_service_pb2'
  ,
  __doc__ = """Response message for an feed mutate.
  
  
  Attributes:
      partial_failure_error:
          Errors that pertain to operation failures in the partial
          failure mode. Returned only when partial\_failure = true and
          all errors occur inside the operations. If any errors occur
          outside the operations (e.g. auth errors), we return an RPC
          level error.
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.MutateFeedsResponse)
  ))
_sym_db.RegisterMessage(MutateFeedsResponse)

MutateFeedResult = _reflection.GeneratedProtocolMessageType('MutateFeedResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEFEEDRESULT,
  __module__ = 'google.ads.googleads_v3.proto.services.feed_service_pb2'
  ,
  __doc__ = """The result for the feed mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.MutateFeedResult)
  ))
_sym_db.RegisterMessage(MutateFeedResult)


DESCRIPTOR._options = None
_GETFEEDREQUEST.fields_by_name['resource_name']._options = None
_MUTATEFEEDSREQUEST.fields_by_name['customer_id']._options = None
_MUTATEFEEDSREQUEST.fields_by_name['operations']._options = None

_FEEDSERVICE = _descriptor.ServiceDescriptor(
  name='FeedService',
  full_name='google.ads.googleads.v3.services.FeedService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=915,
  serialized_end=1330,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeed',
    full_name='google.ads.googleads.v3.services.FeedService.GetFeed',
    index=0,
    containing_service=None,
    input_type=_GETFEEDREQUEST,
    output_type=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_feed__pb2._FEED,
    serialized_options=_b('\202\323\344\223\002)\022\'/v3/{resource_name=customers/*/feeds/*}\332A\rresource_name'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateFeeds',
    full_name='google.ads.googleads.v3.services.FeedService.MutateFeeds',
    index=1,
    containing_service=None,
    input_type=_MUTATEFEEDSREQUEST,
    output_type=_MUTATEFEEDSRESPONSE,
    serialized_options=_b('\202\323\344\223\002/\"*/v3/customers/{customer_id=*}/feeds:mutate:\001*\332A\026customer_id,operations'),
  ),
])
_sym_db.RegisterServiceDescriptor(_FEEDSERVICE)

DESCRIPTOR.services_by_name['FeedService'] = _FEEDSERVICE

# @@protoc_insertion_point(module_scope)
