"""
@author: Erdogan
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import math

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    
    def setUI(self):
        
        logo = QLabel(self)
        pixmap = QPixmap('logo-400.png')
        logo.setPixmap(pixmap)
        
        self.l1 = QLabel(self)      #arayüzde "a" olarak görünen label
        self.l1.move(30,400)
        self.l1.setText("x^2'nin katsayısını giriniz (a):")
        self.l1.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")
        self.input1 = QLineEdit(self)   #a değirini aldığımız giriş
        self.input1.move(290,400)
        self.input1.resize(50,20)
        self.input1.setStyleSheet("width: 100%;border: 0;border-bottom: 2px solid gray;outline: 0;color: white;background: transparent;transition: border-color 0.2s;")
        
        self.l2 = QLabel(self)      #arayüzde "b" olarak görünen label
        self.l2.move(30,440)
        self.l2.setText("x'in katsayısını giriniz (b):")
        self.l2.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")          
        self.input2 = QLineEdit(self)   #b değirini aldığımız giriş
        self.input2.move(290,440)
        self.input2.resize(50,20)
        self.input2.setStyleSheet("width: 100%;border: 0;border-bottom: 2px solid gray;outline: 0;color: white;background: transparent;transition: border-color 0.2s;")

        self.l3 = QLabel(self)      #arayüzde "c" olarak görünen label
        self.l3.move(30,480)
        self.l3.setText("Sabit sayıyı giriniz (c):")
        self.l3.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")  
        self.input3 = QLineEdit(self)   #c değirini aldığımız giriş
        self.input3.move(290,480)
        self.input3.resize(50,20)
        self.input3.setStyleSheet("width: 100%;border: 0;border-bottom: 2px solid gray;outline: 0;color: white;background: transparent;transition: border-color 0.2s;")
        
        self.rl1 = QLabel(self)     #arayüzde "ROOT 1" olarak görünen label
        self.rl1.move(55,540)
        self.rl1.setText("ROOT 1")
        self.rl1.setStyleSheet("color: white; font-family: Arial Black; font-size: 17px;")
        self.r1 = QLineEdit(self)   #1. kökü ytazdıracağımız kısım
        self.r1.move(40,580)
        self.r1.resize(100,20)
        self.r1.setStyleSheet("width: 100%;border: 0;border-bottom: 2px solid gray;outline: 0;color: white;background: transparent;transition: border-color 0.2s;")
        
        self.rl2 = QLabel(self)     #arayüzde "ROOT 2" olarak görünen label
        self.rl2.move(250,540)
        self.rl2.setText("ROOT 2")
        self.rl2.setStyleSheet("color: white; font-family: Arial Black; font-size: 17px;")
        self.r2 = QLineEdit(self)   #2. kökü yazdıracağımız kısım
        self.r2.move(235,580)
        self.r2.resize(100,20)
        self.r2.setStyleSheet("width: 100%;border: 0;border-bottom: 2px solid gray;outline: 0;color: white;background: transparent;transition: border-color 0.2s;")
        
        self.button = QPushButton(self)
        self.button.move(100,630)
        self.button.setText("Calculate")
        self.button.setStyleSheet("background-color: #000066;border-style: outset;color: white;border-width: 2px;border-radius: 10px;font: bold 14px;min-width: 10em;padding: 6px;")
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button.clicked.connect(self.calculate)
        
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle("Denklem Hesaplayıcı")
        centerPoint = QDesktopWidget().availableGeometry().center()
        self.setGeometry(centerPoint.x() - 200, centerPoint.y() - 350,400,700)
        self.setMinimumSize(QSize(400,700))
        self.setMaximumSize(QSize(400,700))
        self.setStyleSheet("background-color: #000066")
        self.show()
        
    def is_square(self, apositiveint):  #tam kare kontrol fonksiyonu
        x = apositiveint // 2   
        seen = set([x])
        while x * x != apositiveint:
            x = (x + (apositiveint // x)) // 2  
            if x in seen: return False
            seen.add(x)
        return True
        
    def calculate(self):
        try:
            a = int(self.input1.text())
            b = int(self.input2.text())
            c = int(self.input3.text())
        
            delta = (b**2) - (a*c*4)

            if delta < 0:   #delta sıfırdan küçük ise denklemin karmaşık 2 kökü vardır
                real = (-1*b) / (2*a)   #tam ve imajiner kısmı hesaplıyoruz
                ima = abs(delta)/((2*a)**2)
                
                if ima > 1 and not self.is_square(ima): #imajiner kısım tam kare mi(kök ifadesinden kurtulabilecek mi) diye kontrole yolluyoruz
                    self.r1.setText(str(real) + "+" + "√" + str(round(ima, 4)) + "i") #tam kare değil ise kök işreti ile birlikte yazdırıyoruz
                    self.r2.setText(str(real) + "-" + "√" + str(round(ima, 4)) + "i")
                else:
                    self.r1.setText(str(real) + "+"  + str(round(math.sqrt(ima), 4)) + "i") #tam kare ise kökten kurtulmuş hali ile yazdırıyoruz
                    self.r2.setText(str(real) + "-"  + str(round(math.sqrt(ima), 4)) + "i")
            
            else :  #deltanın sıfırdan büyük veya sıfıra eşit olması durumu
                root1 = round(((-1*b) - (math.sqrt(delta))) / (2*a), 4)
                root2 = round(((-1*b) + (math.sqrt(delta))) / (2*a), 4)
                self.r1.setText(str(root1))
                self.r2.setText(str(root2))
        except ZeroDivisionError:   #sıfıra bölme hatası yakalama
            mesajKutusu = QMessageBox()
            mesajKutusu.setWindowTitle("Hata!")
            mesajKutusu.setText("Denkleminiz 2. derece bir denklem olmalıdır")
            mesajKutusu.setInformativeText("a'nın sıfır olması, işlemlerde sıfıra bölme hatasına yol açmaktadır. Lütfen kontrol edip tekrar deneyiniz.")
            mesajKutusu.setIcon(QMessageBox.Critical)
            mesajKutusu.setStandardButtons(QMessageBox.Ok)
            mesajKutusu.exec()
        except ValueError:      #girdilerin boş bırakılması veya farklı karakter girilmesi hatalarını yakalama
            mesajKutusu2 = QMessageBox()
            mesajKutusu2.setWindowTitle("Hata!")
            mesajKutusu2.setText("Veriler düzgün formatta girilmemiş. Lütfen kontrol ediniz.")
            mesajKutusu2.setIcon(QMessageBox.Warning)
            mesajKutusu2.setStandardButtons(QMessageBox.Ok)
            mesajKutusu2.exec()
            
            
def window():
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())

if __name__ == "__main__":
    window()
