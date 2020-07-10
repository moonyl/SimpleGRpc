#include <iostream>

#include <grpcpp/channel.h>
#include <grpcpp/create_channel.h>

#include "simple_proto.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;

class SimpleGRpcClient {
public:
    SimpleGRpcClient(std::shared_ptr<Channel> channel) : stub_(SimpleGRpc::NewStub(channel)) {

    }

    void Echo(SimpleData reqData) {
        SimpleData repData;
        ClientContext context;
        Status status = stub_->Echo(&context, reqData, &repData);
        if (!status.ok()) {
            std::cout << "Echo rpc failed." << std::endl;
            return;
        }
        std::cout << "echo: " << repData.data() << std::endl;
    }

    void Add(SimpleTwoData reqData) {
        SimpleResult result;
        ClientContext context;
        Status status = stub_->Add(&context, reqData, &result);
        if (!status.ok()) {
            std::cout << "Add rpc failed." << std::endl;
            return;
        }
        std::cout << "add: " << result.result();
    }

private:
    std::unique_ptr<SimpleGRpc::Stub> stub_;
};
int main() {
    SimpleGRpcClient client(grpc::CreateChannel("localhost:50051", grpc::InsecureChannelCredentials()));
    SimpleData reqData;
    reqData.set_data("my data");
    client.Echo(reqData);

    SimpleTwoData reqTwoData;
    reqTwoData.set_input1(10);
    reqTwoData.set_input2(20);
    client.Add(reqTwoData);
    return 0;
}
