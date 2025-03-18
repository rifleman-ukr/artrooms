import base64

import cv2
import numpy


def take_screenshot(driver, save=False, file_name='tmp'):
    raw_screenshot = base64.b64decode(driver.get_screenshot_as_base64())
    if save:
        with open(f'{file_name}.png', 'wb') as screenshot:
            screenshot.write(raw_screenshot)
            screenshot.close()
    return raw_screenshot


def get_normalized_image_hist(source):
    hist = cv2.calcHist([source], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist, hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    return hist

def compare_screen(driver, sample):
    sample_image = get_normalized_image_hist(cv2.imread(f'samples/{sample}.png',
                                                        flags=cv2.IMREAD_COLOR))
    screen_image = get_normalized_image_hist(cv2.imdecode(numpy.frombuffer(take_screenshot(driver), dtype=numpy.uint8),
                                                          flags=cv2.IMREAD_COLOR))
    hist_score = cv2.compareHist(sample_image, screen_image, cv2.HISTCMP_CORREL)
    return hist_score