from moviepy.editor import VideoFileClip

if __name__ == "__main__":
    clip = VideoFileClip("_static/build_connection.mp4")
    clip.write_gif("_static/build_connection.gif", fps=10)