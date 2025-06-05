# SurgSeg-GAN
Occlusion-Resilient Instance Segmentation of Surgical Instrument Parts Using YOLO and Generative Adversarial Networks for Minimal Invasive Robotic Surgery
# Abstract 
accurate segmentation of surgical instruments is critical for improving safety and precision in minimally invasive robotic surgery. However, real-world surgical scenes often involve occlusions, overlapping instruments, and visual noise, such as blood or glare, which challenge conventional segmentation models. To address these limitations, we propose SurgSeg-GAN, a hybrid instance segmentation framework that integrates a fine-tuned YOLOv11 model with a Generative Adversarial Network (GAN) designed to generate occlusion masks and recover missing features. Our method is validated on the publicly available EndoVis 2017 and EndoVis 2018 surgical instrument segmentation datasets. SurgSeg-GAN achieves a mean Intersection over Union (mIoU) of 77% and a Dice coefficient of 90% on EndoVis 2017, and mIoU of 71% and Dice coefficient of 87% on EndoVis 2018—outperforming several state-of-the-art instance segmentation. Integrating occlusion-aware GANs enables the recovery of instrument parts even under partial visibility, enhancing model robustness and generalizability. These results demonstrate that SurgSeg-GAN significantly improves segmentation accuracy in challenging surgical environments, contributing to safer and more reliable real-time guidance in robotic-assisted procedures.
# Requirements 
conda virtual environment is recommended: 

    conda create -n Surgseg python=3.8
    pip install -r requirements.txt

# Data Preparation 
1- Yolo formating is needed for the images (Refer to "Preprocessing" folder). 

2- Data split is needed, folowing a known split for fair comparison with the state of the art techniques (Refer to the "Data Split" folder).

3- Download and extract Endovis 2017, and Endovis 2017 train and val images from: https://opencas.dkfz.de/endovis/datasetspublications/ . The training and validation data are expected to be in the train folder and val folder respectively: 

for images:

    |-- /path/to/Endovis/
    |-- images/train
    |-- images/val
    
for labels (in yolo format): 

    |-- /path/to/Endovis/
    |-- images/train
    |-- images/val

# Train 
1- Refere to "Train" folder above and "config.yaml" file.

2- For the Training you have to prepare your "config.yaml" file following ours and then call it in Train code which is provided in "Train" folder.

# Test 
For the testing part use the testing files in Endovis Dataset and Refer to the codes provided in "Test" folder above. 
