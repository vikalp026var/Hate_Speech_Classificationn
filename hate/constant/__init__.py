import os
from datetime import datetime

TIMESTAMP:str =datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR=os.path.join("artifacts",TIMESTAMP)
data_path_imbalance="https://drive.google.com/file/d/1nPuGEsT8xssZ2igF4u4xStCdhEn1ATHu/view?usp=drive_link"
data_path_raw_data="https://drive.google.com/file/d/1Hfy5fbyE5gKWyge0ZgRHDPf3D1cAyX-N/view?usp=drive_link"
LABEL='label'
TWEET='tweet'

