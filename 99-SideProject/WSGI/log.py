import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

logfile = './log.txt'
fh = logging.FileHandler(logfile, mode='a')  # open的打开模式这里可以进行参考
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)   # 输出到console的log等级的开关

formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
