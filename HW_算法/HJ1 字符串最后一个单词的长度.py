# 输入：
# hello nowcoder
# 复制
# 输出：
# 8
# 复制
# 说明：
# 最后一个单词为nowcoder，长度为8


your_word = str(input())
new_word = your_word.split(" ")
print(len(new_word[-1]))