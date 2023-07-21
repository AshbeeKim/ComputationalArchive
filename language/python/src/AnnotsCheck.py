import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class annotsBasic:
    c_opt = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    l_opt = ['-', '--', '-.', ':']  # same as ['solid', 'dashed', 'dashdot', 'dotted']
    linewidth = .5

    def __init__(self, image, labels=None):
        self.image = image.copy()
        self.labels = labels
        self.colors = self.cvColor()

    def cvColor(self):
        # R, G, B
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GRAY = (125, 125, 125)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        CYAN = (0, 255, 255)
        MAGENTA = (255, 0, 255)
        YELLOW = (255, 255, 0)
        PINK = (238, 130, 238)
        ORANGE = (255, 165, 0)
        MINT = (60, 179, 113)
        LAVENDER = (106, 90, 205)
        IVORY = (240, 240, 240)
        SALMON = (240, 150, 120)

        colors = {"RED": RED, "GREEN": GREEN, "BLUE": BLUE, "MAGENTA": MAGENTA, "CYAN": CYAN, "YELLOW": YELLOW, "WHITE": WHITE, "GRAY": GRAY, "BLACK": BLACK, \
                  "PINK": PINK, "ORANGE": ORANGE, "MINT": MINT, "LAVENDER": LAVENDER, "IVORY": IVORY, "SALMON": SALMON}
        return colors

    def img2points(self, x, y, color):
        image = self.image.copy()
        plt.grid(color=self.c_opt[-1], linestyle=self.l_opt[-2], linewidth=self.linewidth)
        cv.circle(image, (x, y), 5, self.colors[color], -1)
        plt.imshow(image)

    def img2rectangle(self, x1, y1, x2, y2, color):
        image = self.image.copy()
        plt.grid(color=self.c_opt[-1], linestyle=self.l_opt[-2], linewidth=self.linewidth)
        cv.rectangle(image, (x1, y1), (x2, y2), self.colors[color], 2)
        plt.imshow(image)

    # def img2polygon(self, color, **kwargs):
    #     image = self.image.copy()
    #     assert len(kwargs["x_pts"]) == len(kwargs["y_pts"])
    #     plt.grid(color=self.c_opt[-1], linestyle=self.l_opt[-2], linewidth=self.linewidth)
    #     cv.polygon(image, #####, self.colors[color], 2)
    #     plt.imshow(image)

    def cvtContour2Mask(self, bounded_img_path=None):
        # 공식 문서 참고한 내용이지만, 조금 더 확인해야하는 부분 >> 정리 완료되면 CVCheck.py로 이동 여부 결정
        image = np.array(self.image * 255.).copy()
        gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        hsv = cv.cvtColor(image, cv.COLOR_RGB2HSV)

        # HSV values
        lower_skin = np.array([5, 36, 53])
        upper_skin = np.array([19, 120, 125])

        # annotation을 제대로 해야하는 이유가 이후로 진행된 코드를 보면 알 수 있으나, step-by-step으로 체크하면서 확인하기
        mask = cv.inRange(hsv, lower_skin, upper_skin)
        mask = cv.erode(mask, None, iterations=2)
        mask = cv.dilate(mask, None, iterations=2)

        # Finds contours
        im2, cnts, hierarchy = cv.findContours(mask.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        # Draws contours
        for c in cnts:
            if cv.contourArea(c) < 3000:
                continue
            (x, y, w, h) = cv.boundingRect(c)
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            ## BEGIN - draw rotated rectangle
            rect = cv.minAreaRect(c)
            box = cv.boxPoints(rect)
            box = np.int0(box)
            cv.drawContours(image, [box], 0, (0, 191, 255), 2)
            ## END - draw rotated rectangle
        return cv.imwrite(bounded_img_path, image)


class annotsCats(annotsBasic):
    '''
    large, medium 등으로 나눈 뒤 분석이 가능해야 yolov3 혹은 타 논문을 참고해서 작성할 코드 베이스가 완성될 듯
    그런 의미에서 일단은 보류하지만, CVCheck.py >> CVCats로 이어지도록 작성
    '''

    def __init__(self, large_category=None, medium_category=None):
        super(annotsCats, self).__init__()
        self.lg_cat = large_category if large_category is not None else None
        self.md_cat = medium_category if large_category is not None else None

    def LgColor(self, *args):
        assert len(args) == len(self.lg_cat)
        lg_color = {_v: self.colors[_c] for _c, (_k, _v) in zip(list(args), self.lg_cat.items())}
        return lg_color

    def MdColor(self, *args):
        assert len(args) == len(self.md_cat)
        md_color = {_v: self.colors[_c] for _c, (_k, _v) in zip(list(args), self.md_cat.items())}
        return md_color
