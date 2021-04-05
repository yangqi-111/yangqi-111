from pyecharts import options as opts
from pyecharts.charts import WordCloud

##-------从文件中读出人物词频------------------
src_filename = './data/水浒传-一百零八好汉词频.csv'
# 格式：人物,出现次数

src_file = open(src_filename, 'r')
line_list = src_file.readlines()  #返回列表，文件中的一行是一个元素
src_file.close()

wordfreq_list = []  #用于保存元组(人物姓名,出现次数)
for line in line_list:
    line = line.strip()  #删除'\n'
    line_split = line.split(',')
    wordfreq_list.append((line_split[0],line_split[1]))

del wordfreq_list[0] #删除csv文件中的标题行
print('总人物数量：' + str(len(wordfreq_list)))
##-------从文件中读出人物词频完成------------------

##-------生成词云---------------------------------
cloud = WordCloud()

# 设置词云图
cloud.add('', 
          wordfreq_list, #元组列表，词和词频
          shape='star', # 轮廓形状
          # 轮廓图
          is_draw_out_of_bound=False, #允许词云超出画布边界
          word_size_range=[10, 60], #字体大小范围
          textstyle_opts=opts.TextStyleOpts(font_family="等线") #字体
          )

# 设置标题
cloud.set_global_opts(title_opts=opts.TitleOpts(title="水浒传",subtitle="一百零八好汉好汉词云图"))

# render会生成HTML文件。当前目录为指定文件名参数
out_filename = './output/wordcloud_opts.html'
cloud.render(out_filename)

print('生成结果文件：' + out_filename)

