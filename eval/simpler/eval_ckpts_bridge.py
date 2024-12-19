import os

ckpt_paths = [
    (
        "runs/VLA-Checkpoint-{epoch}-{steps}.ckpt",
        "runs/VLA-Checkpoint-config.json",
    )
]

for i, (ckpt, config) in enumerate(ckpt_paths):
    print("evaluating checkpoint {}".format(ckpt))
    os.system("bash bash/simpler_eval/bridge.bash {} {}".format(ckpt, config))