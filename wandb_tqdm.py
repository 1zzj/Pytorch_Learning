import wandb
from tqdm import tqdm
import time

config = dict(
    learning_rate=0.01,
    momentum=0.2,
    architecture="CNN",
    dataset_id="peds-0192",
    infra="AWS",
)

wandb.init(
    project="detect-pedestrians",
    notes="tweak baseline",
    tags=["baseline", "paper1"],
    config=config,
)


with tqdm(total=200,unit='s',desc='P') as pbar:  # unit单位  desc描述
    # pbar.set_description('Processing:')
    # total表示总的项目, 循环的次数20*10(每次更新数目) = 200(total)
    for i in range(20):
        # 进行动作, 这里是过0.1s
        time.sleep(0.1)
        # 显示指标
        pbar.set_postfix({'loss': '{0:1.5f}'.format(i)})
        # 进行进度更新, 这里设置10个
        pbar.update(10)
