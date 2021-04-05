from pyecharts import options as opts
from pyecharts.charts import Map

# 2010年全国平均气温分布图
data ={
"海南":30,
"云南":28,
"广东":29,
"澳门":28,
"香港":29,
"福建":27,
"山东":17,
"河南":18,
"四川":22,
"江苏":21,
"河北":17,
"湖南":24,
"安徽":19,
"湖北":21,
"浙江":23,
"广西":27,
"江西":25,
"辽宁":4,
"吉林":0,
"陕西":15,
"山西":14,
"贵州":17,
"重庆":23,
"甘肃":5,
"内蒙古":10,
"新疆":7,
"上海":24,
"台湾":29,
"北京":14,
"天津":13,
"宁夏":15,
"青海":3,
"西藏":-2,
"黑龙江":-2,
"南海诸岛":29
}


map_data = list(data.items()) 

c = (
    Map()
    .add("2010年平均气温（单位：摄氏度）", 
         data_pair=map_data, 
         maptype="china",
         is_map_symbol_show=False, # 不描点             
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2010年全国平均气温数据分级设色图"),# 设置标题
        visualmap_opts=opts.VisualMapOpts(min_=-4, max_=30)# 设置渐变色范围
    )
)

c.render('./output/全国平均气温地图_map.html')