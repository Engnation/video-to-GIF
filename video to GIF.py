from moviepy.editor import *
from pygame import *

#Some resources on moviepy: http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/

clip = (VideoFileClip("2021-02-26 15-48-26.mkv")
        .subclip((0,00.00),(0,13.00))
        .resize(0.3) #1920 x 1080 -> 640 x 360
        #x1, y1 indicate the top left corner
        #.crop(x1=30, y1=330, x2=610, y2=30)) # remove left-right & top-bottom borders
        .crop(x_center= 270, y_center=160, width=295, height=290))
clip.preview()
#clip.write_gif("robot_grasp.gif",program='ffmpeg',fps=clip.fps)
clip.write_gif("robot_pointcloud.gif",program='ffmpeg',fps=15)
