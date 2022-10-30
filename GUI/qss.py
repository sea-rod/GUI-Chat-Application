style = '''
QMainWindow{
    background: qlineargradient(x1:0, y1:0, x2:2, y2:1,stop:0.2 rgb(21, 30, 63), stop: 0.4 rgb(0, 0, 17), stop:1 rgb(99, 112, 116));
    color:rgb(225, 228, 255);
    border-radius:10;
    border:1px solid;
    padding:5px;
    min-height:20px;
    }
QScrollArea{
    background:transparent;
    border-radius:10;
    border:1 solid black;
}    

QGroupBox{
    background:transparent;
    border:0; 
}
QLineEdit{
    border-radius:10;
    padding:0 5px;
}
QPushButton{
    background:qlineargradient(x1:0, y1:0, x2:2, y2:1,stop:0.1 #CBD4C2, stop: 1 #637074,stop:1 rgb(0, 0, 17));
    color:rgb(0, 0, 17);
    border-radius:10;
    padding:0 5;
}
QLabel{
    background:qlineargradient(x1:0, y1:0, x2:2, y2:1,stop:0.1 #CBD4C2, stop: 1 #637074,stop:1 rgb(0, 0, 17));
    color:rgb(0, 0, 17);
    
    border-radius:10px;
}
QPushButton[text="Connect"]{
    background-color:Green;
    color:black;
}
QPushButton:Checked{
    background-color:red;
    color:black;
}
QInputDialog{
    background: qlineargradient(x1:0, y1:0, x2:2, y2:1,stop:0.2 rgb(21, 30, 63), stop: 0.4 rgb(0, 0, 17), stop:1 rgb(99, 112, 116));
}
QInputDialog *{
    text-align:right;
    font-size:20px;
    padding:0 20px;
    border-radius:10px;    
}
QGroupBox QLabel{
    background-color:#990073;
    padding:0 5px;
}
'''