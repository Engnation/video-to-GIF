from moviepy.editor import *
from pygame import *

clip = (VideoFileClip("2021-01-31 17-17-36.mkv")
        .subclip((0,00.00),(0,07.50))
        .resize(0.3) #1920 x 1080 -> 640 x 360
        #x1, y1 indicate the top left corner
        #.crop(x1=30, y1=330, x2=610, y2=30)) # remove left-right & top-bottom borders
        .crop(x_center= 335, y_center=160, width=520, height=260))
clip.preview()
clip.write_gif("robot_grasp.gif",program='ffmpeg',fps=clip.fps)
