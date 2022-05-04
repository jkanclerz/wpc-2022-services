import os
def create_slide_show(srcs, dest):
    cmd = "./bin/slideshow {} {}".format(dest, " ".join(srcs))
    os.system(cmd)
