const PROTO_PATH = __dirname + "/../protos/ytube_dl_proto.proto";

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
const yTubeDl = grpc.loadPackageDefinition(packageDefinition);
const express = require("express");
const app = express();
const port = 8080;

console.log(yTubeDl);

app.use(express.json());

app.post("/download", (req, res) => {
  const { url } = req.body;
  console.log({ url });
  const client = new yTubeDl.YoutubeDownload(
    "localhost:50052",
    grpc.credentials.createInsecure()
  );
  console.log(client);
  client.Download({ url }, (err, response) => {
    //console.log("Echo: ", response.data);
    res.send();
  });
});

app.listen(port, () => {
  console.log(`Web Downloader listening at http:localhost:${port}`);
});
