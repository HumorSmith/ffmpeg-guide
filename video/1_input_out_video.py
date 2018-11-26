import ffmpeg
stream = ffmpeg.input('dummy1.mp4')
stream = ffmpeg.output(stream, 'dummy2.mp4')
ffmpeg.run(stream)