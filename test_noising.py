from add_noise import *
import cv2
import numpy as np
import os


compute_video_noise("Pepper", 0.0009)
sortie = os.popen("python3 image_reveal.py --model models/reveal.h5 --container_image my_video/image_decomposition/stego_noise/stego_bruite_sample0.png --reveal_name ito_ilay_notadiavina")

