import ffmpeg
import os

ip_file_path = 'input.mp4'
stream = ffmpeg.input(ip_file_path)



stream_video = stream.video
stream_audio = stream.audio

# stream_video = stream_video.filter('scale', -1, 720)
stream_op = ffmpeg.output(stream_video, stream_audio, "WA_" + ip_file_path,
                          vcodec='libx265', preset='fast')

stream_op = stream_op.overwrite_output()
ffmpeg.run(stream_op)