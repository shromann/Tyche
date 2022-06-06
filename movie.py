from moviepy.editor import ImageSequenceClip

clip = ImageSequenceClip('crypto/images/', fps=10)
clip.write_gif('crypto/videos/Dirr.gif', fps=10)