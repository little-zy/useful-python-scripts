

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

# 打开文本
f = open('xsx.txt', 'r', encoding='utf-8')
t = f.read()
f.close()

# 中文分词
text = ' '.join(jieba.lcut(t))
# 生成对象

wc = WordCloud(font_path='msyh.ttc', width=800, height=600,background_color='white')
#  mode='RGBA', )
wc.generate(text)
# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
# 保存到文件
wc.to_file('wordcloud3.png')
