_base_ = [
    '../_base_/models/pvt_tiny_cifar_mixup.py', '../_base_/datasets/cifar100_bs16.py',
    '../_base_/schedules/cifar10_bs128.py', '../_base_/default_runtime.py'
]

model = dict(
    head=dict(num_classes=100),
    train_cfg=dict(augments=dict(num_classes=100))
)

optimizer = dict(
    _delete_=True,
    type='AdamW',
    lr=1e-3 * 128 / 512,
    weight_decay=0.05,
)
optimizer_config = dict(grad_clip=None)

# learning policy
# FIXME: lr in the first 300 epochs conforms to the CosineAnnealing and
# the lr in the last 10 epoch equals to min_lr
lr_config = dict(
    _delete_=True,
    policy='CosineAnnealingCooldown',
    min_lr=1e-5,
    cool_down_time=10,
    cool_down_ratio=0.1,
    by_epoch=True,
    warmup_by_epoch=True,
    warmup='linear',
    warmup_iters=10,
    warmup_ratio=1e-6)
custom_hooks = [dict(type='EMAHook', momentum=4e-5, priority='ABOVE_NORMAL')]
runner = dict(type='EpochBasedRunner', max_epochs=310)

data = dict(
    samples_per_gpu=64, 
    workers_per_gpu=8,)