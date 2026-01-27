from moviepy.editor import VideoFileClip

if __name__ == "__main__":
    clip = VideoFileClip("_static/connection.mp4")
    clip.write_gif("_static/connection.gif", fps=10)