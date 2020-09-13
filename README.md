# pynamer_CN
A simple Chinese full name generator based on the TOP102 Chinese surname and pinyin first name.
## What is pynamer_CN?
Pynamer_CN is a simple full name generator, which can generate 17 styles of the Chinese name (e.g. zhangsan, Zhangsan, ZhangSan, ZHANGSAN, sanzhang, SanZhang, Sanzhang, SANZHANG, sz). According to the National Name Report of China in 2019, the top102 surname of Chinese has covered 80%+ surnames in China. 
There are also some common first names used by most Chinese people. Pynamer_CN is written with simple python3 codes us if-elif-else structure. Surprisingly, pynamer_CN is also supporting python2.
## What you can do with pynamer_CN?
- By pynamer_CN, you can generate a common Chinese name for yourself.
- Chinese name dictionary (with pydictor or any dictor).
- Build your own NOT USE password lists.
## How to use it?
### Name styles
- 0: SURN + 1 NAME (All lowercase e.g. zhangsan)
- 1: SURN + 1 NAME (Only the first letter uppercase e.g. Zhangsan)
- 2: SURN + 1 NAME (First letter of SURM or NAME uppercase e.g. ZhangSan)
- 3: SURN + 1 NAME (ALL uppercase e.g. ZHANGSAN)

- 4: SURN + 1 NAME (All lowercase with another order e.g. sanzhang)
- 5: SURN + 1 NAME (Only the first letter uppercase with another order e.g. Sanzhang)
- 6: SURN + 1 NAME (First letter of SURM or NAME uppercase with another order e.g. SanZhang)
- 7: SURN + 1 NAME (ALL uppercase with another oder e.g. SANZHANG)


- 8: SURN + 2 NAME (All lowercase e.g. liyiyi)
- 9: SURN + 2 NAME (Only the first letter uppercase e.g. Liyiyi)
- 10: SURN + 2 NAME (First letter of SURM or NAME uppercase e.g. LiYiYi)
- 11: SURN + 2 NAME (ALL uppercase e.g. LIYIYI)

- 12: SURN + 2 NAME (All lowercase with another order e.g. yiyili)
- 13: SURN + 2 NAME (Only the first letter uppercase with another order e.g. Yiyili)
- 14: SURN + 2 NAME (First letter of SURM or NAME uppercase with another order e.g. YiYiLi)
- 15: SURN + 2 NAME (ALL uppercase with another order e.g. YIYILI)

- 16: SURN + 1 NAME (Abbreviation e.g. zhs or zs)
- 17: SURN + 2 NAME (Abbreviation e.g. lyy)

TODO

## License
[MIT License](https://github.com/crazydogen/pynamer_CN/blob/master/LICENSE)
