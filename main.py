from PyQt5.QtWidgets import(QApplication,
                            QWidget,
                            QPushButton,
                            QHBoxLayout,
                            QFileDialog,
                            QVBoxLayout)

window = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("F12 Promax")
btn_dir = QPushButton("Folder")
workdir = QFileDialog.getExistingDirectory()
main_win.resize(700,400)

#row column
row = QHBoxLayout()
col1 = QVBoxLayout()
col1.addWidget(btn_dir)

# make widget 
left = QPushButton("left")
right = QPushButton("right")
mirror = QPushButton("mirror")
sharpness = QPushButton("sharpness")
bw = QPushButton("b/w")

# add widget
row.addWidget(left)
row.addWidget(right)
row.addWidget(mirror)
row.addWidget(sharpness)
row.addWidget(bw)
main_win.setLayout(row)

main_win.show()
window.exec_()

#Hwllo ia am PeanutP () [] {} :; "" ' ' // ? https//satitm