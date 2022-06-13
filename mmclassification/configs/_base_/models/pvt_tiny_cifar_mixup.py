# model settings
model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='PyramidVisionTransformerCifar',
        patch_sizes=[3, 3, 3, 3],
        strides=[1, 2, 2, 2],
        paddings=[1, 1, 1, 1],
        num_layers=[2, 2, 2, 2],
        sr_ratios=[1, 1, 1, 1],
        out_indices=(3, ),
        ),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='MultiLabelLinearClsHead',
        num_classes=10,
        in_channels=512,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0, use_soft=True)),
    train_cfg=dict(
        augments=dict(type='BatchMixup', alpha=1., num_classes=10, prob=1.)))
