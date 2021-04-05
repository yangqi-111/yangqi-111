from pyecharts import options as opts
from pyecharts.charts import Bar

##-------从文件中读出人物词频------------------
src_filename = './data/水浒传-一百零八好汉词频.csv'
# 格式：人物,出现次数

src_file = open(src_filename, 'r')
line_list = src_file.readlines()  #返回列表，文件中的一行是一个元素
src_file.close()

#用于保存人物姓名,出现次数
word_list = []
cnt_list = []

del line_list[0] #删除csv文件中的标题行

for line in line_list:
    line = line.replace('\n', '')
    word_cnt = line.split(',')
    word_list.append(word_cnt[0])
    cnt_list.append(int(word_cnt[1]))
    
##-------从文件中读出人物词频完成------------------

c = (
    Bar()
    .add_xaxis(word_list)
    .add_yaxis("出现次数", cnt_list)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="水浒传",subtitle="一百零八好汉好汉柱状图"),
        datazoom_opts=opts.DataZoomOpts(),)
    )

# render会生成HTML文件。当前目录为指定文件名参数
out_filename = './output/Bar_opts.html'
c.render(out_filename)

print('生成结果文件：' + out_filename)
