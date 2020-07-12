from pytube import YouTube

yt = YouTube(
    "https://www.youtube.com/watch?v=ANME783tf9s&list=PLfwl0UX08oUDdICWnXmatR0wuFMRqguES&index=1")
streams = yt.streams.filter(mime_type="video/mp4",
                            res="720p", progressive="False")
if streams.count() > 0:
    print("streams is list")
    streams[0].download()
#streams = yt.streams.filter(res="720p")

print(type(streams))
# print(streams)
print(streams[0])
