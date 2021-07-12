# -*_coding:utf8-*-

import argparse
import os
import os.path as osp


def set_parser():
    # 命令行参数解析
    parser = argparse.ArgumentParser()
    # 传入参数类型
    parser.add_argument("--square", help="display a square of a given number", type=int)
    parser.add_argument("--verbosity", help="increase output verbosity")
    # 参数的数目，+为至少一个，？为0个或一个，*为0或所有
    parser.add_argument("filename", nargs="?", help="image or label filename")
    parser.add_argument(
        "--labels",
        help="comma separated list of labels OR file containing labels",
        default=argparse.SUPPRESS,
    )
    # config for the gui
    parser.add_argument(
        "--nodata",
        dest="store_data",
        action="store_false",  # 动作的基本类型，store_false默认值是true，store_true默认值false
        help="stop storing image data to JSON file",
        default=argparse.SUPPRESS,  # 默认值，使用参数没有对应的值的话使用
    )
    parser.add_argument(
        "--flags",
        help="comma separated list of flags OR file containing flags",
        default=argparse.SUPPRESS,
    )
    # 解析
    args = parser.parse_args()
    # print(args.square**2)
    # 运行命令：python3 prog.py 4 输出：16

    # 判断执行命令输出的是否为verbosity
    if args.verbosity:
        print("条件满足输出")

    # 判断对象args是否有square，返回true
    print(hasattr(args, 'square'))
    # print(args.flags)
    # 获取命令行输入参数labels对应的值
    print(os.path.isfile(args.labels))


def a():
    #获取当前文件的文件夹
    here = osp.dirname(osp.abspath(__file__))
    print(here)


if __name__ == '__main__':
    a()