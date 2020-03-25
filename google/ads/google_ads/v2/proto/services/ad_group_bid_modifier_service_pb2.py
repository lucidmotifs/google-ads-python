# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/services/ad_group_bid_modifier_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v2.proto.resources import ad_group_bid_modifier_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_ad__group__bid__modifier__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v2/proto/services/ad_group_bid_modifier_service.proto',
  package='google.ads.googleads.v2.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v2.servicesB\036AdGroupBidModifierServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V2.Services\312\002 Google\\Ads\\GoogleAds\\V2\\Services\352\002$Google::Ads::GoogleAds::V2::Services'),
  serialized_pb=_b('\nJgoogle/ads/googleads_v2/proto/services/ad_group_bid_modifier_service.proto\x12 google.ads.googleads.v2.services\x1a\x43google/ads/googleads_v2/proto/resources/ad_group_bid_modifier.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\x1a\x17google/api/client.proto\"5\n\x1cGetAdGroupBidModifierRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\xba\x01\n MutateAdGroupBidModifiersRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12Q\n\noperations\x18\x02 \x03(\x0b\x32=.google.ads.googleads.v2.services.AdGroupBidModifierOperation\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\xff\x01\n\x1b\x41\x64GroupBidModifierOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12G\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x35.google.ads.googleads.v2.resources.AdGroupBidModifierH\x00\x12G\n\x06update\x18\x02 \x01(\x0b\x32\x35.google.ads.googleads.v2.resources.AdGroupBidModifierH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\xa9\x01\n!MutateAdGroupBidModifiersResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12Q\n\x07results\x18\x02 \x03(\x0b\x32@.google.ads.googleads.v2.services.MutateAdGroupBidModifierResult\"7\n\x1eMutateAdGroupBidModifierResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xf4\x03\n\x19\x41\x64GroupBidModifierService\x12\xcd\x01\n\x15GetAdGroupBidModifier\x12>.google.ads.googleads.v2.services.GetAdGroupBidModifierRequest\x1a\x35.google.ads.googleads.v2.resources.AdGroupBidModifier\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/v2/{resource_name=customers/*/adGroupBidModifiers/*}\x12\xe9\x01\n\x19MutateAdGroupBidModifiers\x12\x42.google.ads.googleads.v2.services.MutateAdGroupBidModifiersRequest\x1a\x43.google.ads.googleads.v2.services.MutateAdGroupBidModifiersResponse\"C\x82\xd3\xe4\x93\x02=\"8/v2/customers/{customer_id=*}/adGroupBidModifiers:mutate:\x01*\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x85\x02\n$com.google.ads.googleads.v2.servicesB\x1e\x41\x64GroupBidModifierServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V2.Services\xca\x02 Google\\Ads\\GoogleAds\\V2\\Services\xea\x02$Google::Ads::GoogleAds::V2::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_ad__group__bid__modifier__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_GETADGROUPBIDMODIFIERREQUEST = _descriptor.Descriptor(
  name='GetAdGroupBidModifierRequest',
  full_name='google.ads.googleads.v2.services.GetAdGroupBidModifierRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.GetAdGroupBidModifierRequest.resource_name', index=0,
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
  serialized_start=295,
  serialized_end=348,
)


_MUTATEADGROUPBIDMODIFIERSREQUEST = _descriptor.Descriptor(
  name='MutateAdGroupBidModifiersRequest',
  full_name='google.ads.googleads.v2.services.MutateAdGroupBidModifiersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v2.services.MutateAdGroupBidModifiersRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v2.services.MutateAdGroupBidModifiersRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v2.services.MutateAdGroupBidModifiersRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v2.services.MutateAdGroupBidModifiersRequest.validate_only', index=3,
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
  serialized_start=351,
  serialized_end=537,
)


_ADGROUPBIDMODIFIEROPERATION = _descriptor.Descriptor(
  name='AdGroupBidModifierOperation',
  full_name='google.ads.googleads.v2.services.AdGroupBidModifierOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v2.services.AdGroupBidModifierOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v2.services.AdGroupBidModifierOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v2.services.AdGroupBidModifierOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v2.services.AdGroupBidModifierOperation.remove', index=3,
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
      name='operation', full_name='google.ads.googleads.v2.services.AdGroupBidModifierOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=540,
  serialized_end=795,
)


_MUTATEADGROUPBIDMODIFIERSRESPONSE = _descriptor.Descriptor(
  name='MutateAdGroupBidModifiersResponse',
  full_name='google.ads.googleads.v2.services.MutateAdGroupBidModifiersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v2.services.MutateAdGroupBidModifiersResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v2.services.MutateAdGroupBidModifiersResponse.results', index=1,
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
  serialized_start=798,
  serialized_end=967,
)


_MUTATEADGROUPBIDMODIFIERRESULT = _descriptor.Descriptor(
  name='MutateAdGroupBidModifierResult',
  full_name='google.ads.googleads.v2.services.MutateAdGroupBidModifierResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.MutateAdGroupBidModifierResult.resource_name', index=0,
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
  serialized_start=969,
  serialized_end=1024,
)

_MUTATEADGROUPBIDMODIFIERSREQUEST.fields_by_name['operations'].message_type = _ADGROUPBIDMODIFIEROPERATION
_ADGROUPBIDMODIFIEROPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_ADGROUPBIDMODIFIEROPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_ad__group__bid__modifier__pb2._ADGROUPBIDMODIFIER
_ADGROUPBIDMODIFIEROPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_ad__group__bid__modifier__pb2._ADGROUPBIDMODIFIER
_ADGROUPBIDMODIFIEROPERATION.oneofs_by_name['operation'].fields.append(
  _ADGROUPBIDMODIFIEROPERATION.fields_by_name['create'])
_ADGROUPBIDMODIFIEROPERATION.fields_by_name['create'].containing_oneof = _ADGROUPBIDMODIFIEROPERATION.oneofs_by_name['operation']
_ADGROUPBIDMODIFIEROPERATION.oneofs_by_name['operation'].fields.append(
  _ADGROUPBIDMODIFIEROPERATION.fields_by_name['update'])
_ADGROUPBIDMODIFIEROPERATION.fields_by_name['update'].containing_oneof = _ADGROUPBIDMODIFIEROPERATION.oneofs_by_name['operation']
_ADGROUPBIDMODIFIEROPERATION.oneofs_by_name['operation'].fields.append(
  _ADGROUPBIDMODIFIEROPERATION.fields_by_name['remove'])
_ADGROUPBIDMODIFIEROPERATION.fields_by_name['remove'].containing_oneof = _ADGROUPBIDMODIFIEROPERATION.oneofs_by_name['operation']
_MUTATEADGROUPBIDMODIFIERSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATEADGROUPBIDMODIFIERSRESPONSE.fields_by_name['results'].message_type = _MUTATEADGROUPBIDMODIFIERRESULT
DESCRIPTOR.message_types_by_name['GetAdGroupBidModifierRequest'] = _GETADGROUPBIDMODIFIERREQUEST
DESCRIPTOR.message_types_by_name['MutateAdGroupBidModifiersRequest'] = _MUTATEADGROUPBIDMODIFIERSREQUEST
DESCRIPTOR.message_types_by_name['AdGroupBidModifierOperation'] = _ADGROUPBIDMODIFIEROPERATION
DESCRIPTOR.message_types_by_name['MutateAdGroupBidModifiersResponse'] = _MUTATEADGROUPBIDMODIFIERSRESPONSE
DESCRIPTOR.message_types_by_name['MutateAdGroupBidModifierResult'] = _MUTATEADGROUPBIDMODIFIERRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAdGroupBidModifierRequest = _reflection.GeneratedProtocolMessageType('GetAdGroupBidModifierRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETADGROUPBIDMODIFIERREQUEST,
  __module__ = 'google.ads.googleads_v2.proto.services.ad_group_bid_modifier_service_pb2'
  ,
  __doc__ = """Request message for
  [AdGroupBidModifierService.GetAdGroupBidModifier][google.ads.googleads.v2.services.AdGroupBidModifierService.GetAdGroupBidModifier].
  
  
  Attributes:
      resource_name:
          The resource name of the ad group bid modifier to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.GetAdGroupBidModifierRequest)
  ))
_sym_db.RegisterMessage(GetAdGroupBidModifierRequest)

MutateAdGroupBidModifiersRequest = _reflection.GeneratedProtocolMessageType('MutateAdGroupBidModifiersRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEADGROUPBIDMODIFIERSREQUEST,
  __module__ = 'google.ads.googleads_v2.proto.services.ad_group_bid_modifier_service_pb2'
  ,
  __doc__ = """Request message for
  [AdGroupBidModifierService.MutateAdGroupBidModifiers][google.ads.googleads.v2.services.AdGroupBidModifierService.MutateAdGroupBidModifiers].
  
  
  Attributes:
      customer_id:
          ID of the customer whose ad group bid modifiers are being
          modified.
      operations:
          The list of operations to perform on individual ad group bid
          modifiers.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.MutateAdGroupBidModifiersRequest)
  ))
_sym_db.RegisterMessage(MutateAdGroupBidModifiersRequest)

AdGroupBidModifierOperation = _reflection.GeneratedProtocolMessageType('AdGroupBidModifierOperation', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPBIDMODIFIEROPERATION,
  __module__ = 'google.ads.googleads_v2.proto.services.ad_group_bid_modifier_service_pb2'
  ,
  __doc__ = """A single operation (create, remove, update) on an ad group bid modifier.
  
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new ad
          group bid modifier.
      update:
          Update operation: The ad group bid modifier is expected to
          have a valid resource name.
      remove:
          Remove operation: A resource name for the removed ad group bid
          modifier is expected, in this format:  ``customers/{customer_i
          d}/adGroupBidModifiers/{ad_group_id}~{criterion_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.AdGroupBidModifierOperation)
  ))
_sym_db.RegisterMessage(AdGroupBidModifierOperation)

MutateAdGroupBidModifiersResponse = _reflection.GeneratedProtocolMessageType('MutateAdGroupBidModifiersResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEADGROUPBIDMODIFIERSRESPONSE,
  __module__ = 'google.ads.googleads_v2.proto.services.ad_group_bid_modifier_service_pb2'
  ,
  __doc__ = """Response message for ad group bid modifiers mutate.
  
  
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
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.MutateAdGroupBidModifiersResponse)
  ))
_sym_db.RegisterMessage(MutateAdGroupBidModifiersResponse)

MutateAdGroupBidModifierResult = _reflection.GeneratedProtocolMessageType('MutateAdGroupBidModifierResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEADGROUPBIDMODIFIERRESULT,
  __module__ = 'google.ads.googleads_v2.proto.services.ad_group_bid_modifier_service_pb2'
  ,
  __doc__ = """The result for the criterion mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.MutateAdGroupBidModifierResult)
  ))
_sym_db.RegisterMessage(MutateAdGroupBidModifierResult)


DESCRIPTOR._options = None

_ADGROUPBIDMODIFIERSERVICE = _descriptor.ServiceDescriptor(
  name='AdGroupBidModifierService',
  full_name='google.ads.googleads.v2.services.AdGroupBidModifierService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=1027,
  serialized_end=1527,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAdGroupBidModifier',
    full_name='google.ads.googleads.v2.services.AdGroupBidModifierService.GetAdGroupBidModifier',
    index=0,
    containing_service=None,
    input_type=_GETADGROUPBIDMODIFIERREQUEST,
    output_type=google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_ad__group__bid__modifier__pb2._ADGROUPBIDMODIFIER,
    serialized_options=_b('\202\323\344\223\0027\0225/v2/{resource_name=customers/*/adGroupBidModifiers/*}'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateAdGroupBidModifiers',
    full_name='google.ads.googleads.v2.services.AdGroupBidModifierService.MutateAdGroupBidModifiers',
    index=1,
    containing_service=None,
    input_type=_MUTATEADGROUPBIDMODIFIERSREQUEST,
    output_type=_MUTATEADGROUPBIDMODIFIERSRESPONSE,
    serialized_options=_b('\202\323\344\223\002=\"8/v2/customers/{customer_id=*}/adGroupBidModifiers:mutate:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_ADGROUPBIDMODIFIERSERVICE)

DESCRIPTOR.services_by_name['AdGroupBidModifierService'] = _ADGROUPBIDMODIFIERSERVICE

# @@protoc_insertion_point(module_scope)
