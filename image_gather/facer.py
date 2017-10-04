
import cv2
import sys
import numpy as np

class Facer:

    def __init__(self,cascade):
        self.classifier = cv2.CascadeClassifier('haarcascade/'+ str(cascade))

    def draw_rect(self, encode, color=tuple([0, 0, 255]), thickness=5):
        img_raw = self.decode_img_for_cv(encode)
        gray = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
        face = self.classifier.detectMultiScale(gray, 1.11, 3)
        if len(face) > 0:
            for lect in face:
                x, y, w, h = lect
                cv2.rectangle(img_raw, (x, y), (x+w, y+h),color=color,thickness=thickness)
        else:
            sys.stdout.write('(no face) ')
        return img_raw

    def cut_face(self, encode):
        img_raw = self.decode_img_for_cv(encode)
        try:
            gray = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
            face = self.classifier.detectMultiScale(gray, 1.11, 3)
            if len(face) > 0:
                x, y, w, h = face[0]
                cropd = img_raw[y:y+h, x:x+w]
                return cropd
            else:
                sys.stdout.write('(no face) ')
                return img_raw
        except:
            sys.stdout.write('(CV error) ')
            return img_raw

    def decode_img_for_cv(self, encode):
        return cv2.imdecode(encode, -1)

    def save_img(self, img, file):
        try:
            cv2.imwrite(file, img)
        except:
            sys.stdout.write('(Error in image saving) ')