cmake_minimum_required(VERSION 3.16)
project(SimpleGRpcPair C CXX)

set(CMAKE_CXX_STANDARD 17)

if(MSVC)
    add_definitions(-D_WIN32_WINNT=0xA00)
endif()

find_package(Protobuf CONFIG REQUIRED)
set(_PROTOBUF_PROTOC $<TARGET_FILE:protobuf::protoc>)
find_package(gRPC CONFIG REQUIRED)

set(_GRPC_CPP_PLUGIN_EXECUTABLE $<TARGET_FILE:gRPC::grpc_cpp_plugin>)

get_filename_component(sgr_proto "../protos/simple_proto.proto" ABSOLUTE)
get_filename_component(sgr_proto_path "${sgr_proto}" PATH)

# Generated sources
set(sgr_proto_src "${CMAKE_CURRENT_BINARY_DIR}/simple_proto.pb.cc")
set(sgr_proto_hdr "${CMAKE_CURRENT_BINARY_DIR}/simple_proto.pb.h")
set(sgr_grpc_src "${CMAKE_CURRENT_BINARY_DIR}/simple_proto.grpc.pb.cc")
set(sgr_grpc_hdr "${CMAKE_CURRENT_BINARY_DIR}/simple_proto.grpc.pb.h")

add_custom_command(
        OUTPUT ${sgr_proto_src} ${sgr_proto_hdr} ${sgr_grpc_src} ${sgr_grpc_hdr}
        COMMAND ${_PROTOBUF_PROTOC}
        ARGS --grpc_out "${CMAKE_CURRENT_BINARY_DIR}"
        --cpp_out "${CMAKE_CURRENT_BINARY_DIR}"
        -I "${sgr_proto_path}"
        --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXECUTABLE}"
        ${sgr_proto}
        DEPENDS ${sgr_proto}
)
add_custom_target(genexdebug COMMAND ${CMAKE_COMMAND} -E echo "${_PROTOBUF_PROTOC}, ${_GRPC_CPP_PLUGIN_EXECUTABLE}")

include_directories(${CMAKE_CURRENT_BINARY_DIR})

foreach(_target simpleGRpcServer simpleGRpcClient)
    add_executable(${_target} ${_target}.cpp ${sgr_proto_src} ${sgr_grpc_src})
    target_link_libraries(${_target} PRIVATE
            gRPC::grpc++_unsecure
            protobuf::libprotobuf)
endforeach()

add_subdirectory(mediaServer)