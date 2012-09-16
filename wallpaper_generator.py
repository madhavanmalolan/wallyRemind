#! /usr/bin/python
"""
Author : Madhavan Malolan, IIIT Hyderabad
App : Wallpaper Reminder. Why waste the desktop space?
App Name : Reminder Wall

Email : madhavan.chetlur[at]students[dot]iiit[dot]ac[dot]in


"""


import sys
import os
import getpass


class wallpaper_generator:
  def __init__(self):
    pass

  def get_user(self):
    return getpass.getuser()
  def get_tasks(self):
    fin = open("/home/"+self.get_user()+"/.alerts/tasks/tasks","r")
    content = fin.readlines()
    list_of_tasks = []
    for line in content:
      if line.rstrip():
        list_of_tasks.append(line.strip())
    print(list_of_tasks)
    return list_of_tasks

  def create_image(self,tasks,src):
    user = self.get_user()
    """ Creates the image using commandline Image Magik. Can be improved to use PythonMagik/PIL APIs"""
    x_shift = 50
    y_shift = 150
    image_magik_command = "convert -fill white -pointsize 50 -font helvetica "
    for task in tasks:
      image_magik_command += " -draw 'text "+str(x_shift)+","+str(y_shift)+' "'+task+'"\''
      y_shift += 100
    image_magik_command +=" "+src+" "+"/home/"+user+"/.alerts/tempimg.jpg"
    print(image_magik_command)
    try:
      os.system(image_magik_command)
    except:
      print("ImageMagik not found. Please install it. \n-Madhavan")

    try:
      set_bg = "gsettings set org.gnome.desktop.background picture-uri file:////home/"+user+"/.alerts/tempimg.jpg"
      ret_val =  os.system(set_bg)
      print(set_bg)
      if ret_val:
        print("Running compatiblity Mode for Gnome-2.x")
        set_bg = "gconftool-2 -t string -s /desktop/gnome/background/picture_filename "+"/home/"+user+"/.alerts/tempimg.jpg"
        os.system(set_bg)
    except:
      print("Unable to set Wallpaper :(")
    

def main():
  w = wallpaper_generator()
  tasks = w.get_tasks()
  if len(sys.argv) >1:
    w.create_image(tasks,sys.argv[1])
  else:
    w.create_image(tasks,"/home/"+w.get_user()+"/.alerts/default.jpg")



if __name__ == "__main__":
  main()  
      
