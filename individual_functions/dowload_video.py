import yt_dlp
def download_au_vi(url):
  video_url = url
  ydl = yt_dlp.YoutubeDL()
  video_info = ydl.extract_info(video_url, download=False)
  video_name = video_info['title']
  print("Video Name:", video_name)
  output_dir = f"./content/{video_name}/"

  ydl = yt_dlp.YoutubeDL({
      'format': 'bestvideo+bestaudio',
      'outtmpl': output_dir + '%(title)s.%(ext)s',
  })

  video_info = ydl.extract_info(video_url, download=True)

  video_path = output_dir + video_name+'.webm'

  return {'video_path': video_path,
          'video_name': video_name,
          'output_dir': output_dir,
          'url':url,
          'video_info': video_info}