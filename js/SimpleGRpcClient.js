const PROTO_PATH = __dirname + "/../protos/simple_proto.proto";

const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

//console.log(grpc.loadPackageDefinition(packageDefinition));
const simpleProto = grpc.loadPackageDefinition(packageDefinition);
console.log(simpleProto);
const main = () => {
  //console.log(simpleProto);
  const client = new simpleProto.SimpleGRpc(
    "localhost:50051",
    grpc.credentials.createInsecure()
  );

  client.Echo({ data: "from js" }, (err, response) => {
    console.log("Echo: ", response.data);
  });
};

main();
