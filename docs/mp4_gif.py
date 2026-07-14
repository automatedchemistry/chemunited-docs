from moviepy import VideoFileClip

if __name__ == "__main__":
    clip = VideoFileClip("command_list.mp4")
    clip.write_gif("_static/command_list.gif", fps=10)