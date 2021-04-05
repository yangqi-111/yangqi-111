from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType

pvo_list1=[('China',199),('Russia',156),('France',122),('Argentina',50),
           ('United States',200),('Philippines',100),('Indonesia',131),('United ArabEmirates',122),
           ('Germany',144),('Switzerland',99),('Britain',77),('Ireland',123),
           ('Italy',177),('Australia',175),('Canada',30),('Brazil',20)]
pvo_list2=[('Peru',9),('Egypt',11), ('Libya',5), ('Morocco',7),
           ('Congo',3),('Afghanistan',11),('Bengal',15),('India',5),('Togo',6),
           ('Comorin',3),('Mauritius',5),('Ethiopia',10),('Niger',9)]

c = (
    Map()
    .add("商品1", 
         pvo_list1, 
         maptype="world",
         is_map_symbol_show=False,
    )
    .add("商品2", 
         pvo_list2, 
         maptype="world",
         is_map_symbol_show=False, # 不描点
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="商品投资金额(单位：亿元)"),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
)

c.render('./output/世界大亨投资.html')
