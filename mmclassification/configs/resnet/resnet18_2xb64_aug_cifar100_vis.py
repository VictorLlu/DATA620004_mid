_base_ = [
    '../_base_/schedules/cifar10_bs128.py', '../_base_/default_runtime.py'
]
# model settings
model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='ResNet_CIFAR',
        depth=18,
        num_stages=4,
        out_indices=(3, ),
        style='pytorch'),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='MultiLabelLinearClsHead',
        num_classes=100,
        in_channels=512,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0, use_soft=True)),
    # train_cfg=dict(
    #     augments=dict(type='BatchCutMix', alpha=1.0, num_classes=100,
    #                   prob=1.0)))
    train_cfg=dict(
        augments=dict(type='BatchMixup', alpha=1., num_classes=100, prob=1.)))

# dataset settings
dataset_type = 'CIFAR100'
img_norm_cfg = dict(
    mean=[129.304, 124.070, 112.434],
    std=[68.170, 65.392, 70.418],
    to_rgb=False)
train_pipeline = [
    # dict(type='RandomCrop', size=32, padding=4),
    # dict(type='RandomFlip', flip_prob=0.5, direction='horizontal'),
    # dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='ToTensor', keys=['gt_label']),
    dict(type='Collect', keys=['img', 'gt_label'])
]
test_pipeline = [
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='Collect', keys=['img'])
]
data = dict(
    samples_per_gpu=32,
    workers_per_gpu=8,
    train=dict(
        type=dataset_type,
        data_prefix='data/cifar100',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        data_prefix='data/cifar100',
        pipeline=test_pipeline,
        test_mode=True),
    test=dict(
        type=dataset_type,
        data_prefix='data/cifar100',
        pipeline=test_pipeline,
        test_mode=True))


optimizer = dict(type='SGD', lr=0.1, momentum=0.9, weight_decay=0.0005)
lr_config = dict(policy='step', step=[60, 120, 160], gamma=0.2)