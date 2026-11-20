from PyQt5.QtWidgets import(QApplication,
                            QWidget,
                            QPushButton,
                            QHBoxLayout,
                            QFileDialog,
                            QListWidget,
                            QLabel,
                            QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os
from PIL import Image, ImageFilter

window = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("F12 Promax")
main_win.resize(700,400)
btn_dir = QPushButton("Folder")
workdir = ""

class ImageProcessor():
    def __init__(self, images = None, filename = None, save_dir = "Edit"):
        self.images = images
        self.filename = filename
        self.save_dir = save_dir

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


    #! v pin error: 52
    def saveimage(self):
        print("workdir:", workdir)
        print("save_dir:", self.save_dir)
        workdir_split = workdir.split("/")
        if workdir_split[-1] == self.save_dir:
            path = workdir
        else:    
            path = os.path.join(workdir, self.save_dir)
            if not(os.path.exists(path) or os.path.isdir(path)):
                os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
        self.showImage(image_path)
    
    def dobw(self):
        self.image = self.image.convert("L")
        self.saveimage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)

    def dorotatel(self):
            self.image = self.image.transpose(Image.ROTATE_270)
            self.saveimage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)

    def dorotater(self):
            self.image = self.image.transpose(Image.ROTATE_90)
            self.saveimage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)

    def domirror(self):
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.saveimage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)

    def dosharpen(self):
            self.image = self.image.filter(ImageFilter.SHARPEN)
            self.saveimage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)

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

def showchosenimage():
    if leftside.currentRow()>=0:
        filename = leftside.currentItem().text()
        workimage.loadImage(filename)
        imagepath = os.path.join(workdir, workimage.filename)
        image_path = os.path.join(workdir, workimage.filename)
        workimage.showImage(image_path)

#!row column
row1 = QHBoxLayout()
row2 = QHBoxLayout()
col1 = QVBoxLayout() #todo lower line 
col2 = QVBoxLayout() #? image

workimage = ImageProcessor()

#* make widget 
btn_dir.clicked.connect(showfilenamelist)
left = QPushButton("left")
right = QPushButton("right")
mirror = QPushButton("mirror")
sharpness = QPushButton("sharpness")
bw = QPushButton("b/w")
left.clicked.connect(workimage.dorotatel)
right.clicked.connect(workimage.dorotater)
mirror.clicked.connect(workimage.domirror)
sharpness.clicked.connect(workimage.dosharpen)
bw.clicked.connect(workimage.dobw)
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

leftside.currentRowChanged.connect(showchosenimage)

main_win.show()
window.exec_()

#Hwllo ia am PeanutP () [] {} :; "" ' ' // ? https//satitm