from pytube import YouTube
import os



def download_and_convert(link):
  try:
    youtube_object = YouTube(link)
    video_stream = youtube_object.streams.get_audio_only()
    output_file = video_stream.download()
    base, ext = os.path.splitext(output_file)
    new_file = base + '.mp3'
    os.rename(output_file, new_file)
    print("Download and conversion is completed successfully.")
    return True
  except Exception as e:
    print("An error has occurred: {}".format(e))
    return False


def main():
  while True:
    link = input("Enter the YouTube video URL: ")
    successful = download_and_convert(link)
    if not successful:
      continue

    choice = input(
        "Do you want to continue converting more files? (yes/no): ").lower()
    if choice == 'no':
      break


main()
