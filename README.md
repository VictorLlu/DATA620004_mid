# Midterm homework for DATA620004
The homework consists of two part, namely training a classification model and training a detection model. 
The code for the first part is in `mmclassification` and the code for the second part is in `mmdetection`.
Please first install `mmcv`, `mmcls` and `mmdet` according to [🛠️ mmcls](https://mmclassification.readthedocs.io/en/latest/install.html) and [🛠️mmdet](https://mmdetection.readthedocs.io/en/v2.21.0/get_started.html).

## Classification
The config files for baseline, cutout, mixup and cutmix are shown in the following table.
|   Model         | config name  | Download |
|:---------------:|:-----------:|:---------:|
| Baseline  | [resnet18_2xb64_cifar100](https://github.com/VictorLlu/DATA620004_mid/blob/b82cd5958fbebcedb8179f1854639230320c59b7/mmclassification/configs/resnet/resnet18_2xb64_cifar100.py) | model &#124; log|
|Cutout | [resnet18_2xb64_cutout_cifar100](https://github.com/VictorLlu/DATA620004_mid/blob/b82cd5958fbebcedb8179f1854639230320c59b7/mmclassification/configs/resnet/resnet18_2xb64_cutout_cifar100.py) | model &#124; log|
|Mixup | [resnet18_2xb64_mixup_cifar100](https://github.com/VictorLlu/DATA620004_mid/blob/b82cd5958fbebcedb8179f1854639230320c59b7/mmclassification/configs/resnet/resnet18_2xb64_mixup_cifar100.py) | model &#124; log|
|Cutmix | [resnet18_2xb64_cutmix_cifar100](https://github.com/VictorLlu/DATA620004_mid/blob/b82cd5958fbebcedb8179f1854639230320c59b7/mmclassification/configs/resnet/resnet18_2xb64_cutmix_cifar100.py)| model &#124; log|

## Detection
The config files for faster R-CNN and YOLOv3 are shown in the following table.
|   Model         | config name  | Download |
|:---------------:|:-----------:|:---------:|
| Faster R-CNN  | [faster_rcnn_r50_fpn_1x_voc0712](https://github.com/VictorLlu/DATA620004_mid/blob/b82cd5958fbebcedb8179f1854639230320c59b7/mmdetection/configs/pascal_voc/faster_rcnn_r50_fpn_1x_voc0712.py) | model &#124; log|
|Cutout | [yolov3_mobilenetv2_320_300e_voc0712](https://github.com/VictorLlu/DATA620004_mid/blob/b82cd5958fbebcedb8179f1854639230320c59b7/mmdetection/configs/pascal_voc/yolov3_mobilenetv2_320_300e_voc0712.py) | model &#124; log|

## Training
please first shift to the mmclassifcation or mmdetection and then run 
```
bash ./tools/dist_train.sh ${CONFIG_FILE} ${GPU_NUM} 
```

## Test
To test our trained model, please run
```
bash tools/dist_test.sh ${CONFIG_FILE} ${CHECKPOINT_FILE} ${GPU_NUM} --eval mAP
```