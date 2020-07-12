cmake_minimum_required(VERSION 3.16)
project(mediaServer C CXX)

set(CMAKE_CXX_STANDARD 17)

#if(MSVC)
#    add_definitions(-D_WIN32_WINNT=0xA00)
#endif()

message(STATUS ${CMAKE_PREFIX_PATH})
#find_package(live555 CONFIG REQUIRED)
find_library(liveMedia
        NAMES liveMedia.lib REQUIRED)
find_library(BasicUsageEnv
        NAMES BasicUsageEnvironment.lib REQUIRED)
find_library(UsageEnv
        NAMES UsageEnvironment.lib REQUIRED)
find_library(groupSock
        NAMES groupsock.lib REQUIRED)

find_path(LIVE555_INCLUDES
        NAMES liveMedia.hh REQUIRED)

find_package(OpenSSL REQUIRED)

add_executable(mediaServer live555MediaServer.cpp DynamicRTSPServer.cpp)
target_link_libraries(mediaServer PRIVATE ${liveMedia} ${BasicUsageEnv} ${UsageEnv} ${groupSock} OpenSSL::SSL OpenSSL::Crypto ws2_32)
target_include_directories(mediaServer PRIVATE ${LIVE555_INCLUDES})
