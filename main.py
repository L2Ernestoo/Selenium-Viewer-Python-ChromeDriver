import time
from selenium import webdriver

#Jorge Orellana - 0909-17-7161
#https://github.com/L2Ernestoo

driver = webdriver.Chrome('webdriver/chromedriver_91.exe')

video = 'https://www.youtube.com/watch?v=gwSR2g-_N18'

#Agregue un loop para que se repita n veces el video cada n segundos

for i in range(100):
    print("Reproducciones de video: {}".format(i+1))
    driver.get(video)
    time.sleep(100)


print('Fin de la reproduccion')
driver.quit()

