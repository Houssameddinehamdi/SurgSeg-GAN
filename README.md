# SurgSeg-GAN
Occlusion-Resilient Instance Segmentation of Surgical Instrument Parts Using YOLO and Generative Adversarial Networks for Minimal Invasive Robotic Surgery
# Abstract 
accurate segmentation of surgical instruments is critical for improving safety and precision in minimally invasive robotic surgery. However, real-world surgical scenes often involve occlusions, overlapping instruments, and visual noise, such as blood or glare, which challenge conventional segmentation models. To address these limitations, we propose SurgSeg-GAN, a hybrid instance segmentation framework that integrates a fine-tuned YOLOv11 model with a Generative Adversarial Network (GAN) designed to generate occlusion masks and recover missing features. Our method is validated on the publicly available EndoVis 2017 and EndoVis 2018 surgical instrument segmentation datasets. SurgSeg-GAN achieves a mean Intersection over Union (mIoU) of 77% and a Dice coefficient of 90% on EndoVis 2017, and mIoU of 71% and Dice coefficient of 87% on EndoVis 2018—outperforming several state-of-the-art instance segmentation. Integrating occlusion-aware GANs enables the recovery of instrument parts even under partial visibility, enhancing model robustness and generalizability. These results demonstrate that SurgSeg-GAN significantly improves segmentation accuracy in challenging surgical environments, contributing to safer and more reliable real-time guidance in robotic-assisted procedures.
# Requirements 
python>=3.8
ultralytics>=8.3.40
torch>=1.10
torchvision>=0.11
pytorch-cuda>=11.2  # if using CUDA GPU acceleration
opencv-python>=4.5
numpy>=1.21
