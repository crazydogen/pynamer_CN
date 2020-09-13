#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:crazydogen
# have fun &_7 d_d ^_6 a_ 4_$

# ************************************
#    _____    _______       __ __ 
#  /__  /___/ / ___/____ _/ // / 
#    / / __  / __ \/ __ `/ // /_ 
#   / / /_/ / /_/ / /_/ /__  __/ 
#  /_/\__,_/\____/\__,_/  /_/  
#                                 
# ************************************

# Ref. News about National Name Report of China in 2019
#TOP102 Surnname Coverage above 80% (based on news about the offical file of china gov) -> 89 pinyin of chinese surname
SURN = ("wang", "li", "zhang", "liu", "chen", "yang", "huang", "zhao", "wu", "zhou",
        "xu", "xv","sun", "ma", "zhu", "hu", "guo", "he", "lin", "gao", "luo",
        "zheng", "liang", "xie", "song", "tang", "deng", "han", "feng", "cao",
        "peng", "zeng", "xiao", "tian", "dong", "pan", "yuan", "cai", "jiang", "yu",
        "du", "ye", "cheng", "wei", "su", "lv", "ding", "ren", "lu",
        "yao", "shen", "zhong", "cui", "tan", "fan", "liao",
        "shi", "jin", "jia", "xia", "fu", "fang", "zou", "xiong", "bai",
        "meng", "qin", "qiu", "hou", "yin", "xue", "yan", "duan", "lei",
        "long", "tao", "mao", "hao", "gu", "gong", "shao",
        "wan", "qian", "dai", "ou", "mo", "kong", "xiang", "chang")

# SURN_ABBREV = tuple(set([i[0] for i in SURN])) + ('ch', 'sh', 'zh')

#Common single elements of the first name -> 68  
MOST_USE_NAME = ("ying", "hua", "wen", "yu", "xiu", "ming", "li", "lan", "hong", "jin",
                 "guo", "chun", "xiao", "hai", "mei", "ping", "yun", "zhi", "jian", "fang",
                 "rong", "lin", "zhen", "feng", "jun", "yong", "wei", "yan", "gui",
                 "ling", "jie", "xia", "cheng", "de", "zi", "jia",
                 "xiang", "long", "xin", "qing", "shu", "qiang", "juan", "hui",
                 "ze", "han", "chen", "yi", "si", "xuan", "rui",
                 "hao", "bo", "shi", "nuo", "ran", "mu", "xi", "yue",
                 "yang", "qi", "tong", "ya", "yao", "le", "hang", "an", "ruo")

# MOST_USE_NAME_ABBREV = tuple(set([i[0] for i in MOST_USE_NAME])) + ('ch', 'sh', 'zh')

#Handpicked elements of the first name -> 225
# Ref. http://xh.5156edu.com/pinyi.html 
HANDPICK_NAME = ("ai", "an", "ang",
                "bo", "bi", "bai", "bei", "bao", "ban", "bben", "bin", "bang", "bing", "biao",
                "ci", "cai", "can", "cen", "cun", "ceng", "cong", "cang", "er"
                "de", "di", "du", "dai", "dao", "dan", "deng", "ding", "dong",
                "fa", "fu", "fei", "fan", "feng", "fang", "fing", 
                "gu", "gui", "gao", "gan", "gen", "guo", "gang", "geng", "guan", "guang",
                "hu", "hui", "hao", "han", "he", "hen", "huo", "hang", "heng", "huan", "huang",
                "ji", "ju", "jiu", "jie", "jin", "jun", "jue", "jing", "jia", "jiao", "jian", "juan",
                "kai", "kui", "kan", "kun", "kuo", "kang", "kong", "kuan", "kuang",
                "le", "lei", "li", "lu", "lai", "lie", "lan", "lin", "lun", "lang", "ling", "long", "liao", "lian", "luan", "liang",
                "mi", "mu", "mai", "mei", "mao", "miu", "man", "min", "mang", "meng", "ming", "miao", "mian",
                "na", "ni", "niu", "nie", "nan", "nuo", "neng", "ning",
                "pi", "pu", "pai", "pei", "pan", "pin", "pang", "peng", "ping", "pian",
                "qi", "qiu", "qing", "qiang", "quan", "qian",
                "sa", "so", "se", "si", "su", "sai", "suo", "sang", "song",
                "ta", "to", "te", "ti", "tu", "tai", "tao", "tan", "tuo", "tang", "teng", "ting", "tong", "tian",
                "wa", "wo", "wai", "wei", "wang", "wan",
                "xi", "xu", "xv", "xie", "xin", "xun", "xue", "xing", "xiang", "xiong", "xia", "xuan",
                "ya", "yi", "yu", "yao", "you", "yan", "yun", "yue", "ying", "yang", "yong", "yia", "yuan",
                "zu", "zao", "zan", "zun", "zuo", "zeng", "zong",
                "zhi", "zhou", "zhan", "zhen", "zhong", "zhuan", "zhuo", "zhu", "zhe", "zheng",
                "cha", "che", "chi", "chu", "chai", "chao", "chan", "chen", "chong", "chuang", "chuan",
                "sha", "shi", "shu", "shao", "shou", "shan", "shen", "shuo", "shuang", "shun")

# HANDPICK_NAME_ABBREV = tuple(set([i[0] for i in HANDPICK_NAME])) + ('ch', 'sh', 'zh')

# FOR DEBUG
# print(len(SURN), len(MOST_USE_NAME), len(HANDPICK_NAME))
# # Duplication detection
# import collections
# print([item for item, count in collections.Counter(SURN).items() if count > 1])


def dump2file(path, lines):
    import os
    if not os.path.exists(path):
        with open(path, 'a') as f:
            for i in lines:
                f.writelines(i + '\n')
        print(f"Successfully writed to {path}")
    else:
        raise FileExistsError

def main(path, names, mode):
    """
    Args:
        path (str): path to output
        names (tuple): names to use
        mode (int): 0 - 17
                    0: SURN + 1 NAME (All lowercase e.g. zhangsan)
                    1: SURN + 1 NAME (Only first letter uppercase e.g. Zhangsan)
                    2: SURN + 1 NAME (Fisrt letter of SURM or NAME uppercase e.g. ZhangSan)
                    3: SURN + 1 NAME (ALL uppercase e.g. ZHANGSAN)
                    -------------------------------------------------------------
                    4: SURN + 1 NAME (All lowercase with another oder e.g. sanzhang)
                    5: SURN + 1 NAME (Only first letter uppercase with another oder e.g. Sanzhang)
                    6: SURN + 1 NAME (Fisrt letter of SURM or NAME uppercase with another oder e.g. SanZhang)
                    7: SURN + 1 NAME (ALL uppercase with another oder e.g. SANZHANG)

                    *************************************************************
                    8: SURN + 2 NAME (All lowercase e.g. liyiyi)
                    9: SURN + 2 NAME (Only first letter uppercase e.g. Liyiyi)
                    10: SURN + 2 NAME (Fisrt letter of SURM or NAME uppercase e.g. LiYiYi)
                    11: SURN + 2 NAME (ALL uppercase e.g. LIYIYI)
                    -------------------------------------------------------------
                    12: SURN + 2 NAME (All lowercase with another oder e.g. yiyili)
                    13: SURN + 2 NAME (Only first letter uppercase with another oder e.g. Yiyili)
                    14: SURN + 2 NAME (Fisrt letter of SURM or NAME uppercase with another oder e.g. YiYiLi)
                    15: SURN + 2 NAME (ALL uppercase with another oder e.g. YIYILI)
                    *************************************************************

                    16: SURN + 1 NAME (Abbreviation e.g. zhs or zs)
                    17: SURN + 2 NAME (Abbreviation e.g. lyy)
    """ 
    if mode not in range(18):
        raise ValueError

    if mode == 17:
        surn_abbrev = tuple(set([i[0] for i in SURN])) + ('ch', 'sh', 'zh')
        name_abbrev = tuple(set([i[0] for i in names])) + ('ch', 'sh', 'zh')
        tmp = []
        for i in surn_abbrev:
            for j in name_abbrev:
                for k in name_abbrev:
                    tmp.append(i+j+k)
    elif mode == 16:
        surn_abbrev = tuple(set([i[0] for i in SURN])) + ('ch', 'sh', 'zh')
        name_abbrev = tuple(set([i[0] for i in names])) + ('ch', 'sh', 'zh')
        tmp = []
        for i in surn_abbrev:
            for j in name_abbrev:
                tmp.append(i+j)
    elif mode == 15:
        tmp = []
        for i in names:
            for j in names:
                for k in SURN:
                    tmp.append((i+j+k).upper())
    elif mode == 14:
        tmp = []
        for i in names:
            for j in names:
                for k in SURN:
                    tmp.append(i.capitalize()+j.capitalize()+k.capitalize())
    elif mode == 13:
        tmp = []
        for i in names:
            for j in names:
                for k in SURN:
                    tmp.append((i+j+k).capitalize())
    elif mode == 12:
        tmp = []
        for i in names:
            for j in names:
                for k in SURN:
                    tmp.append(i+j+k)
    elif mode == 11:
        tmp = []
        for i in SURN:
            for j in names:
                for k in names:
                    tmp.append((i+j+k).upper())
    elif mode == 10:
        tmp = []
        for i in SURN:
            for j in names:
                for k in names:
                    tmp.append(i.capitalize()+j.capitalize()+k.capitalize())
    elif mode == 9:
        tmp = []
        for i in SURN:
            for j in names:
                for k in names:
                    tmp.append((i+j+k).capitalize())
    elif mode == 8:
        tmp = []
        for i in SURN:
            for j in names:
                for k in names:
                    tmp.append(i+j+k)
    elif mode == 7:
        tmp = []
        for i in names:
            for j in SURN:
                tmp.append((i+j).upper())
    elif mode == 6:
        tmp = []
        for i in names:
            for j in SURN:
                tmp.append(i.capitalize()+j.capitalize())
    elif mode == 5:
        tmp = []
        for i in names:
            for j in SURN:
                tmp.append((i+j).capitalize())
    elif mode == 4:
        tmp = []
        for i in names:
            for j in SURN:
                tmp.append(i+j)
    elif mode == 3:
        tmp = []
        for i in SURN:
            for j in names:
                tmp.append((i+j).upper())
    elif mode == 2:
        tmp = []
        for i in SURN:
            for j in names:
                tmp.append(i.capitalize()+j.capitalize())
    elif mode == 1:
        tmp = []
        for i in SURN:
            for j in names:
                tmp.append((i+j).capitalize())
    elif mode == 0:
        tmp = []
        for i in SURN:
            for j in names:
                tmp.append(i+j)
    else: 
        raise NotImplementedError
    dump2file(path, tmp)

if __name__ == "__main__":
    Path = r'E:\XingMing\example1.txt'
    # dump2file(Path, SURN)
    main(Path, HANDPICK_NAME, 0)
