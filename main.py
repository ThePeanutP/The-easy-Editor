from PyQt5.QtWidgets import(QApplication,
                            QWidget,
                            QPushButton,
                            QHBoxLayout,
                            QFileDialog,
                            QListWidget,
                            QLabel,
                            QVBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
from PIL import Image

window = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("F12 Promax")
main_win.resize(700,400)
btn_dir = QPushButton("Folder")
workdir = ""

class ImageProcessor():
    def __init__(self, image = None, filename = None, sub_folder_name = None):
        self.image = image
        self.filename = filename
        self.sub_folder_name = sub_folder_name

    def loadImage(self, filename):
        # images.png
        self.filename = filename
        # /Users/mac/Desktop/algo/PenutP(Panu)/TheEasyEditor/The-easy-Editor/imageseasy/images.png
        image_path = os.path.join(workdir, filename)
        # Open Image and store in self.image
        self.image = Image.open(image_path)

    def showImage(self, path):
        image.hide()
        # Load image to pixmapimage
        pixmapimage = QPixmap(path)
        # find width amd height of widget
        w, h = image.width(), image.height()
        # Resize image to fit widget and keep same ratio
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        # set image to widget
        image.setPixmap(pixmapimage)
        # show widget
        image.show()

def chooseworkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(filename,extention):
    photofiles = []
    for file in filename:
        for ext in extention:
            if file.endswith(ext):
                photofiles.append(file)
    return photofiles

def showfilenamelist():
    extention=["png","jpg"]
    chooseworkdir()
    filenames = os.listdir(workdir)
    ph = filter(filenames,extention)
    leftside.clear()
    for p in ph:
        leftside.addItem(p)

def showChosenImage():
   # check if selecting image on list
   if leftside.currentRow() >= 0:
       # get selecting item Ex. image1.png
       filename = leftside.currentItem().text()
       # call method loadImage(image1.png) => get image
       workimage.loadImage(filename)
       # create image_path from folder path (workdir) + filename (image1.png) 
       image_path = os.path.join(workdir, workimage.filename)
       # call method showImage to set image to widget
       workimage.showImage(image_path)

#!row column
row1 = QHBoxLayout()
row2 = QHBoxLayout()
col1 = QVBoxLayout() #todo lower line
col2 = QVBoxLayout() #? image

#* make widget 
btn_dir.clicked.connect(showfilenamelist)
left = QPushButton("left")
right = QPushButton("right")
mirror = QPushButton("mirror")
sharpness = QPushButton("sharpness")
bw = QPushButton("b/w")
leftside = QListWidget() 
image= QLabel("image")

# add widget
col1.addWidget(btn_dir)
col1.addWidget(leftside)
col2.addWidget(image)
row1.addWidget(left)
row1.addWidget(right)
row1.addWidget(mirror)
row1.addWidget(sharpness)
row1.addWidget(bw)
col2.addLayout(row1)
row2.addLayout(col1,stretch=1)
row2.addLayout(col2,stretch=3)
main_win.setLayout(row2)

# set state
leftside.currentRowChanged.connect(showChosenImage)
workimage = ImageProcessor()

main_win.show()
window.exec_()

#Hwllo ia am PeanutP () [] {} :; "" ' ' // ? https//satitm