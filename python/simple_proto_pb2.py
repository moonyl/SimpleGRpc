# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simple_proto.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='simple_proto.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12simple_proto.proto\"\x1a\n\nSimpleData\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"/\n\rSimpleTwoData\x12\x0e\n\x06input1\x18\x01 \x01(\x05\x12\x0e\n\x06input2\x18\x02 \x01(\x05\"\x1e\n\x0cSimpleResult\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32X\n\nSimpleGRpc\x12\"\n\x04\x45\x63ho\x12\x0b.SimpleData\x1a\x0b.SimpleData\"\x00\x12&\n\x03\x41\x64\x64\x12\x0e.SimpleTwoData\x1a\r.SimpleResult\"\x00\x62\x06proto3'
)




_SIMPLEDATA = _descriptor.Descriptor(
  name='SimpleData',
  full_name='SimpleData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='SimpleData.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_end=48,
)


_SIMPLETWODATA = _descriptor.Descriptor(
  name='SimpleTwoData',
  full_name='SimpleTwoData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input1', full_name='SimpleTwoData.input1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input2', full_name='SimpleTwoData.input2', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=50,
  serialized_end=97,
)


_SIMPLERESULT = _descriptor.Descriptor(
  name='SimpleResult',
  full_name='SimpleResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SimpleResult.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=99,
  serialized_end=129,
)

DESCRIPTOR.message_types_by_name['SimpleData'] = _SIMPLEDATA
DESCRIPTOR.message_types_by_name['SimpleTwoData'] = _SIMPLETWODATA
DESCRIPTOR.message_types_by_name['SimpleResult'] = _SIMPLERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleData = _reflection.GeneratedProtocolMessageType('SimpleData', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLEDATA,
  '__module__' : 'simple_proto_pb2'
  # @@protoc_insertion_point(class_scope:SimpleData)
  })
_sym_db.RegisterMessage(SimpleData)

SimpleTwoData = _reflection.GeneratedProtocolMessageType('SimpleTwoData', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLETWODATA,
  '__module__' : 'simple_proto_pb2'
  # @@protoc_insertion_point(class_scope:SimpleTwoData)
  })
_sym_db.RegisterMessage(SimpleTwoData)

SimpleResult = _reflection.GeneratedProtocolMessageType('SimpleResult', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLERESULT,
  '__module__' : 'simple_proto_pb2'
  # @@protoc_insertion_point(class_scope:SimpleResult)
  })
_sym_db.RegisterMessage(SimpleResult)



_SIMPLEGRPC = _descriptor.ServiceDescriptor(
  name='SimpleGRpc',
  full_name='SimpleGRpc',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=131,
  serialized_end=219,
  methods=[
  _descriptor.MethodDescriptor(
    name='Echo',
    full_name='SimpleGRpc.Echo',
    index=0,
    containing_service=None,
    input_type=_SIMPLEDATA,
    output_type=_SIMPLEDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Add',
    full_name='SimpleGRpc.Add',
    index=1,
    containing_service=None,
    input_type=_SIMPLETWODATA,
    output_type=_SIMPLERESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIMPLEGRPC)

DESCRIPTOR.services_by_name['SimpleGRpc'] = _SIMPLEGRPC

# @@protoc_insertion_point(module_scope)
