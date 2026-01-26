from moviepy.editor import VideoFileClip

if __name__ == "__main__":
    clip = VideoFileClip("_static/workflow.mp4")
    clip.write_gif("_static/workflow.gif", fps=10)