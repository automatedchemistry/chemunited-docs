from moviepy.editor import VideoFileClip

if __name__ == "__main__":
    clip = VideoFileClip("_static/add_valve_tutorial.mp4")
    clip.write_gif("_static/add_valve_tutorial.gif", fps=10)