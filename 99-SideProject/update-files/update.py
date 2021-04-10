import os
import sys
import re
import operator as op

regexes  = [
    re.compile(r'\s*\d*(V\d00.*?) ', re.I),
    # ASCII“65279”对应的是BOM标志，用于匹配UTF-8-BOM格式的文件
    re.compile(chr(65279)+r'\s*\d*(V\d00.*?) ', re.I)
]

def is_same_file_type(type, file_type):

    regexe = re.compile(file_type, re.I)
    if regexe.search(type):
        return True

    return False



def copy_file(temp_file, source_file):
    '''
    将缓存的文件内容重写回源文件，并删除缓存文件
    '''
    with open(temp_file, 'r') as file_read, open(source_file, 'w') as file_temp:
        # 逐行将缓存文件内容写回原文件
        file_read_line = file_read.readline()
        while file_read_line:
            file_temp.write(file_read_line)
            file_read_line = file_read.readline()
    # 删除缓存文件
    os.remove(temp_file)


def comp_version(verisonUpdate, versionAlready):
    '''
    功能:     比较文件版本
    返回值:   'grater'-待更新的文件内容较新，
              'equal'-待更新的文件内容一样
              'less'-待更新的文件内容较旧
    作用:     用于判断当前的文件版本是否是新版本
    '''
    length1 = len(verisonUpdate.strip())
    length2 = len(versionAlready.strip())
    length = min(length1,length2)
    for i in range(0,length):
        if (op.gt(verisonUpdate[i], versionAlready[i])):
            return 'grater'
        elif (op.lt(verisonUpdate[i], versionAlready[i])):
            return 'less'

    if length1 < length2:
        return 'grater'
    elif length1 == length2:
        return 'equal'
    else:
        return 'less'


class file(object):
    '''
    文件类对象
    '''

    def __init__(self, file_path = None):
        self.file_path = file_path


    def get_file_type(self):
        '''
        功能：获取文件类型
        '''
        return os.path.splitext(self.file_path)[1]


    def read_update_version(self):
        '''
        功能：读取文件中的第一个版本号(通常都包含更新版本内容的文件),视为软件更新版本
        '''
        with open(self.file_path, 'r')  as file:
            for line in file:
                for regexe in regexes :
                    result = regexe.search(line)
                    if result:
                        return result.group()
            return None


    def read_update_content(self):
        '''
        功能：读取文件中的内容,使用生产器循环一次读取一行内容,防止文件内容过大爆掉内存
        '''
        with open(self.file_path, 'r') as file:
            for line in file:
                yield line


    def get_last_version_and_line_num(self):
        '''
        功能：读取文件中最后一个版本号及其行号(默认最后一个版本号是最新版本)
        '''
        with open(self.file_path, 'r') as file:
            version_lineNum = []
            line_num = 0
            while True:
                line = file.readline()
                line_num += 1
                if line:
                    result = regexes[0].match(line.lstrip(chr(65279)).strip())
                    if result:
                        version_lineNum.extend([result.group(1), line_num])
                else:
                    break

            return version_lineNum


    def add_update_content(self, read_file):
        '''
        功能: 无条件增加更改内容，可能将内容放入字典中更好，形如: 目录:内容
        '''
        if self.file_path == read_file.file_path:
            print('cs')
            return

        # 取文件所在的目录名
        dir_name = os.path.split(os.path.split(self.file_path)[0])[1]
        # print(dir_name)
        with open(self.file_path, 'a') as file:
            file.write('\n'+next(read_file.read_update_content()))
            is_match = False
            for line in read_file.read_update_content():
                if  not is_match:
                    result = re.search(dir_name, line)
                    if result:
                        # 匹配到本目录内容
                        is_match = True
                        continue
                if is_match:
                    # 查找到下一个目录时退出
                    result = re.search('{.*}', line)
                    if result:
                        break
                    # 写本目录内容
                    if len(line.strip()):
                        file.write('\n'+line)
                    else:
                        # 没有内容时，写入默认内容，留足缩进
                        file.write('\n                1、内容无变化，仅升级版本号')
                        break
        self.del_blank_lines()


    def conditional_add_update_conten(self, read_file):
        '''
        功能：有条件增加更改内容
            1、文件中无版本时增加
            2、文件中版本较旧是增加
            3、文件中版本一样时删除再增加
        '''
        if self.file_path == read_file.file_path:
            return

        # if self.get_file_type() == '.txt':
        if is_same_file_type(self.get_file_type(), '.txt'):
            update_version = read_file.read_update_version()
            if update_version != None:
                last_version = self.get_last_version_and_line_num()
                if last_version == []:
                    self.add_update_content(read_file)
                else:
                    comp_result = comp_version(update_version, last_version[-2])
                    if comp_result == 'grater':
                        self.add_update_content(read_file)
                    elif comp_result == 'equal':
                        self.del_last_content()
                        self.add_update_content(read_file)


    def del_blank_lines(self):
        '''
        功能：删除文件中的空行
        原理：将原文件中的有效内容(不是空行)备份到缓存文件中，然后将缓存文件再写回原文件
               并删除缓存文件
        '''
        temp = os.path.join(os.path.split(self.file_path)[0], 'temp.txt')
        with open(self.file_path, 'r') as old_file, open(temp, 'w',) as new_file:
            for line in old_file:
                # 删除空白符及ASCII码65279对应的字符(BOM码)
                if len(line.strip().lstrip(chr(65279))) != 0:
                    new_file.write(line)
        copy_file(temp, self.file_path)


    def del_last_content(self):
        '''
        功能：删除最后一个版本内容(防止误增加一个新的版本)
        '''
        # if self.get_file_type() == '.txt':
        if is_same_file_type(self.get_file_type(), '.txt'):
            version_lineNum = self.get_last_version_and_line_num()
            if version_lineNum != []:
                temp = os.path.join(os.path.split(self.file_path)[0], 'temp.txt')
                with open(self.file_path, 'r') as file, open(temp, 'w',) as new_file:
                        count_line = 1
                        while count_line < version_lineNum[-1]:
                            new_file.write(file.readline())
                            count_line += 1

                copy_file(temp, self.file_path)


    def update_file_name(self, read_file):
        '''
        功能:更新文件版本号
        '''
        # 取文件路径及文件名
        root_dir, file_name = os.path.split(self.file_path)
        # 判断文件路径是否存在，如果存在即更改为工作目录
        if os.path.exists(root_dir):
            os.chdir(root_dir)
            if os.path.isfile(file_name):
            # 正则表达式找出所有含版本号的名称并行为指定版本号
                res = re.compile(r'(V\w+)') #缺陷：文件路径中有版本号就无法使用，报错
                new_str = res.sub(read_file.read_update_version().strip(), file_name)
                try:
                    os.rename(file_name, new_str)
                except FileExistsError as Argument:
                    return;

# wr_ff = file(r'D:\python\X1.HL009A.K05.001-1\01V100A5\01out\软件版本及更改说明.txt')
# rd_ff =file(r'D:\python\X1.HL009A.K05.001-1\b.txt')


'''
使用策略模式替代下面文件夹类的代码，因为太多重复代码了
思路：
    1、使用策略模式，也即行为模式
    2、策略模式类似于C语言中的函数指针，同一类型的几个函数其返回值，参数是一样的，取中函数指针作为参数，可以通过传入不同的函数实现不同的功能，而使用这些函数的主函数却不用修改
    3、参数的传递：参数是在实例化时传入，还是调用参数时传入？实际都可以，这里因为要根据读取的内容修改文件下所有的文件，所以使用实例化时传入，个人感觉比较清晰。
'''
# 抽象策略类
class stragety():
    def __init__(self, read_file = None):
        self.read_file = read_file

    def action(self, write_file):
        # raise NotImplementedError()
        print(write_file.file_path)


# 具体策略类1
class name_stragety(stragety):
    '''
    修改文件名(仅修改版本号)
    '''
    def __init__(self,  read_file):
        self.read_file = read_file

    def action(self, write_file):
        write_file.update_file_name(self.read_file)

# 具体策略类2
class content_stragety(stragety):
    '''
    增加版本升级内容
    '''
    def __init__(self, read_file):
        self.read_file = read_file

    def action(self, write_file):
        write_file.conditional_add_update_conten(self.read_file)

# 具体策略类3
class del_stragety(stragety):
    '''
    删除最后一个版本内容
    '''
    def __init__(self, read_file = None):
        self.read_file = read_file

    def action(self, write_file):
        write_file.del_last_content()

# 环境类
class punp_fold(object):
    '''
    文件夹操作环境
    '''
    def __init__(self, stragety, read_file = None):

        self.stragety = stragety
        self.read_file = read_file

    def operate(self, root_dir, source_dir = None):
            dirs = os.listdir(root_dir)
            for i in range(0, len(dirs)):
                # print(dirs[i])
                # 不允许访问源码文件夹
                if dirs[i] == source_dir:
                    continue
                path = os.path.join(root_dir, dirs[i])
                if os.path.isdir(path):
                    # 递归遍历所有文件夹
                    self.operate(path)
                # 创建写入文件对象
                write_file = file(path)
                self.stragety(self.read_file).action(write_file)




# cs1 = content(content_stragety, rd_ff)
# cs1.operate(path)


# cs1 = content(del_stragety)
# cs1.operate(path)

if __name__ == '__main__':

    # source_path为源代码的路径
    source_path = os.getcwd()
    # vision_path为版本目录路径，code_dir为源代码目录名
    vision_path, source_dir = os.path.split(source_path)
    # vision_dir为版本目录名
    soft_coding_path, vision_dir = os.path.split(vision_path)
    # print('vision_path=', vision_path)
    # print('source_dir=', source_dir)

    # print('soft_coding_path=' ,soft_coding_path)
    # print('vision_dir=',vision_dir)

    # 源代码的路径+vision_dir.txt为读取文件的路径
    read_path = os.path.join(source_path,vision_dir+'.txt')

    # print(read_path)
    # print('source_path=',source_path)

    # rd_ff =file(r'D:\python\X1.HL034A.K05.503-1\V100A04\sourcecode\V100A05.txt')



    # path = r'D:\python\X1.HL034A.K05.503-1\V100A04'
    rd_file = file(read_path)

    cs = punp_fold(name_stragety, rd_file)
    cs.operate(vision_path, source_dir)

    cs = punp_fold(content_stragety, rd_file)
    cs.operate(vision_path, source_dir)



