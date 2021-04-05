from pyecharts import options as opts
from pyecharts.charts import Pie

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

p=Pie()
p.add( "",
        wordfreq_list[0:18],#取数据中出现次数最多的前十八
        radius=["40%", "75%"],#设置饼图的半径，数组的第一项是内半径，第二项是外半径
        label_opts=opts.LabelOpts(is_show=True, position="inside"),#展示标签，让其处在中间位置
        #设置阴线（图形的描边颜色）与描边宽度
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
        )
p.set_global_opts(title_opts=opts.TitleOpts(title="水浒传",subtitle="十八好汉饼图"))

# render会生成HTML文件。当前目录为指定文件名参数
out_filename = './output/Pie_opts.html'
p.render(out_filename)

print('生成结果文件：' + out_filename)

