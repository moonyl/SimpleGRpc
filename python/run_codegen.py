from grpc_tools import protoc

print(protoc)
protoc.main((
    '',
    '-I../protos',
    '--python_out=.',
    '--grpc_python_out=.',
    '../protos/simple_proto.proto',
))

protoc.main((
    '',
    '-I../protos',
    '--python_out=.',
    '--grpc_python_out=.',
    '../protos/ytube_dl_proto.proto',
))
