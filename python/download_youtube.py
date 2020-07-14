import logging
import ytube_dl_proto_pb2_grpc
import ytube_dl_proto_pb2
import grpc
from concurrent import futures
from pytube import YouTube

# yt = YouTube(
#     "https://www.youtube.com/watch?v=ANME783tf9s&list=PLfwl0UX08oUDdICWnXmatR0wuFMRqguES&index=1")
# streams = yt.streams.filter(mime_type="video/mp4",
#                             res="720p", progressive="False")
# if streams.count() > 0:
#     print("streams is list")
#     streams[0].download(filename="secretJuJu.mp4", output_path="../downloads")
# #streams = yt.streams.filter(res="720p")

# print(type(streams))
# # print(streams)
# print(streams[0])


class YoutubeDownloadServicer(ytube_dl_proto_pb2_grpc.YoutubeDownloadServicer):
    def Download(self, request, context):
        print(request.url)
        streams = YouTube(request.url).streams.filter(mime_type="video/mp4",
                                                      res="720p", progressive="False")
        # print(YouTube(request.url).streams)
        streams[0].download(filename="secretJuJu.mp4",
                            output_path="../downloads")
        # print(ytube_dl_proto_pb2.DownloadResult)
        return ytube_dl_proto_pb2.DownloadResult(result=0)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ytube_dl_proto_pb2_grpc.add_YoutubeDownloadServicer_to_server(
        YoutubeDownloadServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
