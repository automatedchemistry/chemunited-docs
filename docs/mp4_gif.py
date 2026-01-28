from moviepy.editor import VideoFileClip

if __name__ == "__main__":
    clip = VideoFileClip("_static/protocol04.mp4")
    clip.write_gif("_static/protocol04.gif", fps=10)