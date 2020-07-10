#include <iostream>
#include <grpcpp/server_builder.h>
#include <simple_proto.grpc.pb.h>

using grpc::Status;
using grpc::ServerContext;
using grpc::ServerBuilder;
using grpc::Server;

class SimpleGRpcServerImpl final : public SimpleGRpc::Service
{
public:
    Status Echo(ServerContext *context, const SimpleData *request, SimpleData *response) override {
        response->set_data(request->data());
        return Status::OK;
    }

    Status Add(ServerContext *context, const SimpleTwoData *request, SimpleResult *response) override {
        response->set_result(request->input1() + request->input2());
        return Status::OK;
    }
};

void runServer() {
    std::string serverAddress("0.0.0.0:50051");
    SimpleGRpcServerImpl service;

    ServerBuilder builder;
    builder.AddListeningPort(serverAddress, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);
    std::unique_ptr<Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << serverAddress << std::endl;
    server->Wait();
}
int main() {
    //std::cout << "Hello, World!" << std::endl;
    runServer();
    return 0;
}
