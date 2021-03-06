# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='image.proto',
  package='image',
  syntax='proto3',
  serialized_options=b'\n\026com.michael.grpc.imageP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bimage.proto\x12\x05image\",\n\x08Metadata\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cimage_format\x18\x02 \x01(\t\"U\n\x12ImageUploadRequest\x12#\n\x08metadata\x18\x01 \x01(\x0b\x32\x0f.image.MetadataH\x00\x12\x0f\n\x05image\x18\x02 \x01(\x0cH\x00\x42\t\n\x07payload\"F\n\x13ImageUploadResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12#\n\x06status\x18\x02 \x01(\x0e\x32\x13.image.UploadStatus*@\n\x0cUploadStatus\x12\x0f\n\x0bIN_PROGRESS\x10\x00\x12\x06\n\x02OK\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x12\x0b\n\x07UNKNOWN\x10\x03\x32S\n\x0cImageService\x12\x43\n\x06Upload\x12\x19.image.ImageUploadRequest\x1a\x1a.image.ImageUploadResponse(\x01\x30\x01\x42\x1a\n\x16\x63om.michael.grpc.imageP\x01\x62\x06proto3'
)

_UPLOADSTATUS = _descriptor.EnumDescriptor(
  name='UploadStatus',
  full_name='image.UploadStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IN_PROGRESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=227,
  serialized_end=291,
)
_sym_db.RegisterEnumDescriptor(_UPLOADSTATUS)

UploadStatus = enum_type_wrapper.EnumTypeWrapper(_UPLOADSTATUS)
IN_PROGRESS = 0
OK = 1
FAILED = 2
UNKNOWN = 3



_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='image.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='image.Metadata.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_format', full_name='image.Metadata.image_format', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=22,
  serialized_end=66,
)


_IMAGEUPLOADREQUEST = _descriptor.Descriptor(
  name='ImageUploadRequest',
  full_name='image.ImageUploadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='image.ImageUploadRequest.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='image.ImageUploadRequest.image', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='payload', full_name='image.ImageUploadRequest.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=68,
  serialized_end=153,
)


_IMAGEUPLOADRESPONSE = _descriptor.Descriptor(
  name='ImageUploadResponse',
  full_name='image.ImageUploadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='image.ImageUploadResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='image.ImageUploadResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=155,
  serialized_end=225,
)

_IMAGEUPLOADREQUEST.fields_by_name['metadata'].message_type = _METADATA
_IMAGEUPLOADREQUEST.oneofs_by_name['payload'].fields.append(
  _IMAGEUPLOADREQUEST.fields_by_name['metadata'])
_IMAGEUPLOADREQUEST.fields_by_name['metadata'].containing_oneof = _IMAGEUPLOADREQUEST.oneofs_by_name['payload']
_IMAGEUPLOADREQUEST.oneofs_by_name['payload'].fields.append(
  _IMAGEUPLOADREQUEST.fields_by_name['image'])
_IMAGEUPLOADREQUEST.fields_by_name['image'].containing_oneof = _IMAGEUPLOADREQUEST.oneofs_by_name['payload']
_IMAGEUPLOADRESPONSE.fields_by_name['status'].enum_type = _UPLOADSTATUS
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['ImageUploadRequest'] = _IMAGEUPLOADREQUEST
DESCRIPTOR.message_types_by_name['ImageUploadResponse'] = _IMAGEUPLOADRESPONSE
DESCRIPTOR.enum_types_by_name['UploadStatus'] = _UPLOADSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:image.Metadata)
  })
_sym_db.RegisterMessage(Metadata)

ImageUploadRequest = _reflection.GeneratedProtocolMessageType('ImageUploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEUPLOADREQUEST,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:image.ImageUploadRequest)
  })
_sym_db.RegisterMessage(ImageUploadRequest)

ImageUploadResponse = _reflection.GeneratedProtocolMessageType('ImageUploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEUPLOADRESPONSE,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:image.ImageUploadResponse)
  })
_sym_db.RegisterMessage(ImageUploadResponse)


DESCRIPTOR._options = None

_IMAGESERVICE = _descriptor.ServiceDescriptor(
  name='ImageService',
  full_name='image.ImageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=293,
  serialized_end=376,
  methods=[
  _descriptor.MethodDescriptor(
    name='Upload',
    full_name='image.ImageService.Upload',
    index=0,
    containing_service=None,
    input_type=_IMAGEUPLOADREQUEST,
    output_type=_IMAGEUPLOADRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGESERVICE)

DESCRIPTOR.services_by_name['ImageService'] = _IMAGESERVICE

# @@protoc_insertion_point(module_scope)
