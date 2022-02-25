from pytube import YouTube

print("Paste or type the url: ",end = "")
url = f"'{input()}'"

print("Video Title:")
print(YouTube(url).title)

strm = YouTube(url).streams

prog_list = [one_stream.itag for one_stream in strm.filter(progressive=True)]

print("Please select the resolution serial number & press the Enter key:")

for i in range(len(prog_list)):
    print(f"{i+1}). to download in {strm.get_by_itag(prog_list[i]).resolution}")

selected_option = int(input())
print(strm.get_by_itag(prog_list[selected_option - 1]))
strm.get_by_itag(prog_list[selected_option -1]).download()
print("Video Downloaded")
