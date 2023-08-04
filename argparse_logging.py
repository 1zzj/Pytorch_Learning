import argparse
import logging
import torch
# 命令行传参 python .py -name value
# 建立ArgumentParse 参数解析器
parser = argparse.ArgumentParser(description='argparse learning practice')
# 添加参数
parser.add_argument('--epoch','-e',metavar='E',type=int,default=60,help='迭代次数')
parser.add_argument('--batchsize','-b',metavar='B',type=int,default=4,help='批大小')  # 第二个名字只能是单个字母
parser.set_defaults(epoch=1,batchsize=4)
args = parser.parse_args()
# vars() 显示parse.parse_args()对象的属性
print(vars(args))   # vars()函数 返回类的__dict__属性，其以字典的形式显示属性和方法
# 命令行输出日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
logging.info(f'Using device {device}')
