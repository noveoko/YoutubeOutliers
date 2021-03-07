from youtube_transcript_api import YouTubeTranscriptApi

links = [] #links to youtube videos

links = map(lambda video: video.split("=")[-1], links)

videos = {}
for id in links:
  try:
    videos[id] = YouTubeTranscriptApi.get_transcript(id)
  except Exception as ee:
    print(f'Unable to fetch {id}')

len(videos.keys())

with open('video_transcripts.txt','w') as outfile:
  for video, text in videos.items():
    line = f"{video}\t{text}\n"
    outfile.write(line)