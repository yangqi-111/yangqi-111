from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

c = (
    Geo()
    .add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(color="grey", border_color="black"),)
    .add(
        "",
        [("常德", 40), ("咸宁", 60), ("长沙", 50), ("襄阳", 60), ("北京", 90),
         ("天津", 70), ("延安", 70), ("昆明", 60), ("海口", 70), ("连云港",50),
         ("上海", 80), ("深圳", 80), ("郴州", 60)],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.EFFECT_SCATTER,
        color="white",
    )
    .add(
        "",
        [("三明", 30), ("宁波", 20), ("南昌", 40), 
         ("西安", 20), ("成都", 10), ("阿勒泰", 20),
         ("乌鲁木齐", 10), ("吐鲁番", 20),("西宁", 30),
         ("兰州", 20), ("宝鸡", 30), ("遵义", 10),
         ("安顺", 20), ("西双版纳", 10), ("大理",20)],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.SCATTER,
        color="white",
    )
    .add(
        "参加工作前",
        [("常德", "咸宁"), ("常德","长沙"), ("常德","襄阳"),
         ("常德", "北京"), ("北京", "天津"),("北京", "延安"),
         ("常德", "昆明"),("昆明", "海口"), ("海口", "常德"),
         ("北京", "连云港"),("北京","上海"), ("北京","郴州"),
         ("北京","深圳"),("北京","常德")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=4, color="green"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "参加工作后",
        [("常德", "三明"), ("三明", "宁波"), ("三明", "南昌"), 
         ("三明", "西安"), ("三明", "成都"), ("三明","阿勒泰"),
         ("阿勒泰","乌鲁木齐"),("乌鲁木齐","吐鲁番"),("三明","西宁"),
         ("西宁", "兰州"), ("兰州", "宝鸡"), ("三明", "常德"),
         ("常德", "遵义"), ("遵义", "安顺"), ("安顺", "西双版纳"),
         ("西双版纳","大理"), ("大理","三亚"), ("三亚","常德")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=4, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="小明的一生"))
    
    .render('./output/geo_line.html')
)
