# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/enums/feed_item_target_device.proto

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
  name='google/ads/googleads_v3/proto/enums/feed_item_target_device.proto',
  package='google.ads.googleads.v3.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v3.enumsB\031FeedItemTargetDeviceProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V3.Enums\312\002\035Google\\Ads\\GoogleAds\\V3\\Enums\352\002!Google::Ads::GoogleAds::V3::Enums'),
  serialized_pb=_b('\nAgoogle/ads/googleads_v3/proto/enums/feed_item_target_device.proto\x12\x1dgoogle.ads.googleads.v3.enums\x1a\x1cgoogle/api/annotations.proto\"\\\n\x18\x46\x65\x65\x64ItemTargetDeviceEnum\"@\n\x14\x46\x65\x65\x64ItemTargetDevice\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\n\n\x06MOBILE\x10\x02\x42\xee\x01\n!com.google.ads.googleads.v3.enumsB\x19\x46\x65\x65\x64ItemTargetDeviceProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v3/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V3.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V3\\Enums\xea\x02!Google::Ads::GoogleAds::V3::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FEEDITEMTARGETDEVICEENUM_FEEDITEMTARGETDEVICE = _descriptor.EnumDescriptor(
  name='FeedItemTargetDevice',
  full_name='google.ads.googleads.v3.enums.FeedItemTargetDeviceEnum.FeedItemTargetDevice',
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
      name='MOBILE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=158,
  serialized_end=222,
)
_sym_db.RegisterEnumDescriptor(_FEEDITEMTARGETDEVICEENUM_FEEDITEMTARGETDEVICE)


_FEEDITEMTARGETDEVICEENUM = _descriptor.Descriptor(
  name='FeedItemTargetDeviceEnum',
  full_name='google.ads.googleads.v3.enums.FeedItemTargetDeviceEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEEDITEMTARGETDEVICEENUM_FEEDITEMTARGETDEVICE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=222,
)

_FEEDITEMTARGETDEVICEENUM_FEEDITEMTARGETDEVICE.containing_type = _FEEDITEMTARGETDEVICEENUM
DESCRIPTOR.message_types_by_name['FeedItemTargetDeviceEnum'] = _FEEDITEMTARGETDEVICEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedItemTargetDeviceEnum = _reflection.GeneratedProtocolMessageType('FeedItemTargetDeviceEnum', (_message.Message,), dict(
  DESCRIPTOR = _FEEDITEMTARGETDEVICEENUM,
  __module__ = 'google.ads.googleads_v3.proto.enums.feed_item_target_device_pb2'
  ,
  __doc__ = """Container for enum describing possible data types for a feed item target
  device.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.enums.FeedItemTargetDeviceEnum)
  ))
_sym_db.RegisterMessage(FeedItemTargetDeviceEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
