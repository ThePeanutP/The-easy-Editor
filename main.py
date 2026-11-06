from PyQt5.QtWidgets import(QApplication,
                            QWidget,
                            QPushButton,
                            QHBoxLayout,
                            QFileDialog,
                            QListWidget,
                            QLabel,
                            QVBoxLayout)
import os

window = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("F12 Promax")
main_win.resize(700,400)
btn_dir = QPushButton("Folder")
workdir = QFileDialog.getExistingDirectory()
filenames = os.listdir(workdir)
def filter(filename,extention):
    photofiles = []
    for file in filename:
        for ext in extention:
            if file.endswith(ext):
                photofiles.append(file)
    return photofiles

#row column
row1 = QHBoxLayout()
row2 = QHBoxLayout()
col1 = QVBoxLayout() #lower line
col2 = QVBoxLayout() #image

# make widget 
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

main_win.show()
window.exec_()

#Hwllo ia am PeanutP () [] {} :; "" ' ' // ? https//satitm