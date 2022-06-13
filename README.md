# Update: Final homework for DATA620004
The homework consists of three parts -- inference on a segmentation model, training three Faster R-CNN model with different pretrain backbones and comparison with Vision Transformer and ResNet. We will provide training code for the last two tasks. Please first install `mmcv`, `mmcls` and `mmdet` according to [🛠️ mmcls](https://mmclassification.readthedocs.io/en/latest/install.html) and [🛠️mmdet](https://mmdetection.readthedocs.io/en/v2.21.0/get_started.html).

## Different pretrain backbones of Faster R-CNN
Results for three kinds of pretrain backbones, as well as the config files, model and log.
Please find the model checkpoint and log with the same name as config.
|   Pretrain        | Config name | mAP | Download |
|:---------------:|:-----------:|:-----------:|:---------:|
| Random  | [faster_rcnn_r50_random_fpn_1x12_voc0712](https://github.com/VictorLlu/DATA620004_mid/blob/f0daff11e4e770eb3e295f0659d9e0dc1f201cc5/mmdetection/configs/pascal_voc/faster_rcnn_r50_random_fpn_1x12_voc0712.py) | 0.155 | [model](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ) &#124; [log](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ)|
| ImageNet  | [faster_rcnn_r50_fpn_1x12_voc0712](https://github.com/VictorLlu/DATA620004_mid/blob/f0daff11e4e770eb3e295f0659d9e0dc1f201cc5/mmdetection/configs/pascal_voc/faster_rcnn_r50_fpn_1x12_voc0712.py)| 0.804 | [model](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ) &#124; [log](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ)|
| COCO  | [faster_rcnn_r50_maskrcnn_fpn_1x12_voc0712](https://github.com/VictorLlu/DATA620004_mid/blob/f0daff11e4e770eb3e295f0659d9e0dc1f201cc5/mmdetection/configs/pascal_voc/faster_rcnn_r50_maskrcnn_fpn_1x12_voc0712.py) | 0.815 | [model](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ) &#124; [log](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ)|

## Vision Transformer
The config files for Vison Transformer and ResNet are shown in the following table.
|   Method       | Config name | Top-1 | Download |
|:---------------:|:-----------:|:-----------:|:---------:|
| ResNet-18  | [resnet18_2xb64_mixup_cifar100](https://github.com/VictorLlu/DATA620004_mid/blob/f0daff11e4e770eb3e295f0659d9e0dc1f201cc5/mmclassification/configs/resnet/resnet18_2xb64_mixup_cifar100.py) | 82.3 | [model](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ) &#124; [log](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ)|
| PVT-tiny  | [pvt_t_2xb64_lr1e-3_mixup_cifar100](https://github.com/VictorLlu/DATA620004_mid/blob/f0daff11e4e770eb3e295f0659d9e0dc1f201cc5/mmclassification/configs/pvt/pvt_t_2xb64_lr1e-3_mixup_cifar100.py) | 76.0 | [model](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ) &#124; [log](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ)|

# Midterm homework for DATA620004
The homework consists of two parts, namely training a classification model and training a detection model. 
The code for the first part is in `mmclassification` and the code for the second part is in `mmdetection`.
Please first install `mmcv`, `mmcls` and `mmdet` according to [🛠️ mmcls](https://mmclassification.readthedocs.io/en/latest/install.html) and [🛠️mmdet](https://mmdetection.readthedocs.io/en/v2.21.0/get_started.html).

## Classification
The config files for baseline, cutout, mixup and cutmix are shown in the following table. 
Password for baidu yun is 6p6i.
Please find the model checkpoint and log with the same name as config.
|   Model         | config name  | Download |
|:---------------:|:-----------:|:---------:|
| Baseline  | [resnet18_2xb64_cifar100](https://github.com/VictorLlu/DATA620004_mid/blob/b82cd5958fbebcedb8179f1854639230320c59b7/mmclassification/configs/resnet/resnet18_2xb64_cifar100.py) | [model](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ) &#124; [log](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ)|
|Cutout | [resnet18_2xb64_cutout_cifar100](https://github.com/VictorLlu/DATA620004_mid/blob/b82cd5958fbebcedb8179f1854639230320c59b7/mmclassification/configs/resnet/resnet18_2xb64_cutout_cifar100.py) | [model](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ) &#124; [log](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ)|
|Mixup | [resnet18_2xb64_mixup_cifar100](https://github.com/VictorLlu/DATA620004_mid/blob/b82cd5958fbebcedb8179f1854639230320c59b7/mmclassification/configs/resnet/resnet18_2xb64_mixup_cifar100.py) | [model](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ) &#124; [log](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ)|
|Cutmix | [resnet18_2xb64_cutmix_cifar100](https://github.com/VictorLlu/DATA620004_mid/blob/b82cd5958fbebcedb8179f1854639230320c59b7/mmclassification/configs/resnet/resnet18_2xb64_cutmix_cifar100.py)| [model](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ) &#124; [log](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ)|

## Detection
The config files for faster R-CNN and YOLOv3 are shown in the following table.
|   Model         | config name  | Download |
|:---------------:|:-----------:|:---------:|
| Faster R-CNN  | [faster_rcnn_r50_fpn_1x_voc0712](https://github.com/VictorLlu/DATA620004_mid/blob/b82cd5958fbebcedb8179f1854639230320c59b7/mmdetection/configs/pascal_voc/faster_rcnn_r50_fpn_1x_voc0712.py) | [model](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ) &#124; [log](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ)|
|Cutout | [yolov3_mobilenetv2_320_300e_voc0712](https://github.com/VictorLlu/DATA620004_mid/blob/b82cd5958fbebcedb8179f1854639230320c59b7/mmdetection/configs/pascal_voc/yolov3_mobilenetv2_320_300e_voc0712.py) | [model](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ) &#124; [log](https://pan.baidu.com/s/1xSORdAJLN0k3O7GpfLSZKQ) |

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