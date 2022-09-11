import cv2
import random
import time
import pyautogui as pg
import cv2
import mss
import numpy
#up-1, down-2, right-3, left-4


def rand():
    a = random.uniform(5.9, 6.7)
    return a


with mss.mss() as sct:
    monitor = {"top": 350, "left": 550, "width": 800, "height": 640}

    while "Screen capturing":
        time.sleep(rand()/10)
        work = 0
        last_time = time.time()
        img = numpy.array(sct.grab(monitor))
    #Скорее всего ебашится зеленая обводка
        #Начало обнаружения право
        template3 = cv2.imread("right.jpg", cv2.IMREAD_GRAYSCALE)
        w3, h3 = template3.shape[::-1]
        gray_frame3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        res3 = cv2.matchTemplate(gray_frame3, template3, cv2.TM_CCOEFF_NORMED)
        loc3 = numpy.where(res3 >= 0.7)
        for pt3 in zip(*loc3[::-1]):
            #можно int ебнуть
            cv2.rectangle(img, pt3, (pt3[0] + w3, pt3[1] + h3), (0, 255, 0), 3)
            work = 3
        #Конец обнаружения право

        #Начало обнаружения лево
        template4 = cv2.imread("left.jpg", cv2.IMREAD_GRAYSCALE)
        w4, h4 = template4.shape[::-1]
        gray_frame4 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        res4 = cv2.matchTemplate(gray_frame4, template4, cv2.TM_CCOEFF_NORMED)
        loc4 = numpy.where(res4 >= 0.7)
        for pt4 in zip(*loc4[::-1]):
            #можно int ебнуть
            cv2.rectangle(img, pt4, (pt4[0] + w4, pt4[1] + h4), (0, 255, 242), 3)
            work = 4
        #Конец обнаружения лево

        #Начало обнаружения вверх
        template1 = cv2.imread("up.jpg", cv2.IMREAD_GRAYSCALE)
        w1, h1 = template1.shape[::-1]
        gray_frame1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        res1 = cv2.matchTemplate(gray_frame1, template1, cv2.TM_CCOEFF_NORMED)
        loc1 = numpy.where(res1 >= 0.7)
        for pt1 in zip(*loc1[::-1]):
            #можно int ебнуть
            cv2.rectangle(img, pt1, (pt1[0] + w1, pt1[1] + h1), (255, 0, 230), 3)
            work = 1
        #Конец обнаружения вверх

        #Начало обнаружения вниз
        template2 = cv2.imread("down.jpg", cv2.IMREAD_GRAYSCALE)
        w2, h2 = template2.shape[::-1]
        gray_frame2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        res2 = cv2.matchTemplate(gray_frame2, template2, cv2.TM_CCOEFF_NORMED)
        loc2 = numpy.where(res2 >= 0.7)
        for pt2 in zip(*loc2[::-1]):
            #можно int ебнуть
            cv2.rectangle(img, pt2, (pt2[0] + w2, pt2[1] + h2), (0, 0, 255), 3)
            work = 2
        # Конец обнаружения вниз
        cv2.imshow("Frame", img)
        if work == 1:
            pg.press('up')
        elif work == 2:
            pg.press('down')
        elif work == 3:
            pg.press('right')
        elif work == 4:
            pg.press('left')
        if cv2.waitKey(10) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
