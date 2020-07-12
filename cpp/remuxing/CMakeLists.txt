cmake_minimum_required(VERSION 3.16)
project(remuxing C CXX)

set(CMAKE_CXX_STANDARD 17)

#if(MSVC)
#    add_definitions(-D_WIN32_WINNT=0xA00)
#endif()

message(STATUS ${CMAKE_PREFIX_PATH})
find_package(ffmpeg REQUIRED)


add_executable(remuxing remuxing.c)
target_link_libraries(remuxing PRIVATE ${FFMPEG_LIBRARIES})
target_include_directories(remuxing PRIVATE ${FFMPEG_INCLUDE_DIRS})
