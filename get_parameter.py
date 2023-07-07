# 任务 1:在一个新的名字为'poem.txt'的文件里,写入一下内容:
# 我欲乘风归去,
# 又恐琼楼玉宇,
# 高处不胜寒.

# with open('./poem.txt', 'w', encoding='utf-8') as f:
#     f.write('我欲乘风归去, \n又恐琼楼玉宇, \n高处不胜寒, \n') 

# 任务 2:在上面的'poem.txt'文件结尾处,添加一下两句:
# 起舞弄清影,
# 何似在人间.
with open('./poem.txt', 'a', encoding='utf-8') as f:
    f.write('起舞弄清影, \n何似在人间.')