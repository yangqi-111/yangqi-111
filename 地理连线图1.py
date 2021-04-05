from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType, GeoType

geo = Geo()
geo.add_coordinate(name="2012-1221-22:28-880000", longitude=167.2778, latitude=-14.3591)  
geo.add_coordinate(name="2012-1210-16:53-9490000",longitude=129.8684, latitude=-6.4969)  
geo.add_coordinate(name="2012-1207-8:18-23630000", longitude=144.1594, latitude=37.8201)
geo.add_coordinate(name="2012-1116-18:12-43260000",longitude=155.6545, latitude=49.2365)
geo.add_coordinate(name="2012-1111-11:23-9150000",longitude=95.848, latitude=22.8908)
geo.add_coordinate(name="2012-1107-16:35-49310000",longitude=-92.0669, latitude=14.0318)
geo.add_coordinate(name="2012-1028-03:04-7790000", longitude=-132.1724, latitude=52.6777)
geo.add_coordinate(name="2012-1012-03:13-370000",longitude=134.0822, latitude=-4.8858)
geo.add_coordinate(name="2012-1009-12:32-8820000", longitude=153.9333, latitude=-60.64)
geo.add_coordinate(name="2012-0930-16:31-3470000", longitude=-76.3716, latitude=1.9079)
geo.add_coordinate(name="2012-0926-23:39-56500000",longitude=-178.1844, latitude=51.5408)
geo.add_coordinate(name="2012-0905-14:42-7730000",longitude=-85.3884, latitude=10.0242)
geo.add_coordinate(name="2012-0831-12:47-35540000",longitude=126.8262, latitude=10.8107)
geo.add_coordinate(name="2012-0830-13:43-25300000",longitude=-11.0341, latitude=71.4464)
geo.add_coordinate(name="2012-0827-04:37-19650000",longitude=-88.6604, latitude=12.1318)
geo.add_coordinate(name="2012-0826-15:53-7160000",longitude=126.8696, latitude=2.1983)
geo.add_coordinate(name="2012-0814-02:59-3886000",longitude=145.3057, latitude=49.75)
geo.add_coordinate(name="2012-0811-12:23-17670000",longitude=46.838, latitude=38.4023)
geo.add_coordinate(name="2012-0728-20:35-970000",longitude=153.1678, latitude=-4.654)
geo.add_coordinate(name="2012-0726-05:33-3386000",longitude=66.2905, latitude=-17.5507)
geo.add_coordinate(name="2012-0725-11:20-27880000",longitude=159.8561, latitude=-9.669)
geo.add_coordinate(name="2012-0528-07:23-520000",longitude=-63.1134, latitude=-28.021)
geo.add_coordinate(name="2012-0428-10:27-220000",longitude=-174.6864, latitude=-18.7293)
geo.add_coordinate(name="2012-0421-01:16-5370000",longitude=134.3225, latitude=-1.6946)
geo.add_coordinate(name="2012-0417-07:13-49880000",longitude=147.125, latitude=-5.5336)
geo.add_coordinate(name="2012-0417-03:50-15280000",longitude=-71.5641, latitude=-32.6374)
geo.add_coordinate(name="2012-0412-07:15-49170000",longitude=-113.127, latitude=28.8386)
geo.add_coordinate(name="2012-0411-22:55-10820000",longitude=-102.8762, latitude=18.2042)
geo.add_coordinate(name="2012-0411-10:43-10530000",longitude=92.4284, latitude=0.7675)
geo.add_coordinate(name="2012-0411-08:38-37800000",longitude=93.0144, latitude=2.2376)
geo.add_coordinate(name="2012-0325-22:37-6560000",longitude=-72.1268, latitude=-35.2035)
geo.add_coordinate(name="2012-0321-22:15-5590000",longitude=146.0083, latitude=-6.2233)
geo.add_coordinate(name="2012-0320-18:24-7620000",longitude=-98.3694, latitude=16.4734)
geo.add_coordinate(name="2012-0314-09:08-36230000",longitude=145.0154, latitude=40.8421)
geo.add_coordinate(name="2012-0309-19:53-320000", longitude=169.7495, latitude=-19.2236)
geo.add_coordinate(name="2012-0303-12:19-55730000",longitude=170.3882, latitude=-22.1221)
geo.add_coordinate(name="2012-0226-06:17-19920000",longitude=95.9804, latitude=51.8008)
geo.add_coordinate(name="2012-0206-03:49-13920000",longitude=123.2167, latitude=9.9194)
geo.add_coordinate(name="2012-0202-13:34-4110000", longitude=167.1814, latitude=-17.7532)
geo.add_coordinate(name="2012-0115-13:40-21400000",longitude=-55.8579, latitude=-60.7016)
geo.add_coordinate(name="2012-0110-18:37-0190000", longitude=93.2081, latitude=2.4307)
geo.add_coordinate(name="2012-0101-5:27-55800000", longitude=138.1834, latitude=31.4682)

prov_list = [("2012-1221-22:28-880000",6.7),("2012-1210-16:53-9490000",7.1),
             ("2012-1207-8:18-23630000",7.2),("2012-1116-18:12-43260000",6.5),
             ("2012-1111-11:23-9150000",6.8),("2012-1107-16:35-49310000",7.4),
             ("2012-1028-03:04-7790000",7.8),("2012-1012-03:13-3700000",6.6),
             ("2012-1009-12:32-8820000",6.6),("2012-0930-16:31-3470000",7.2),
             ("2012-0926-23:39-5650000",6.5),("2012-0905-14:42-7730000",7.6),
             ("2012-0831-12:47-35540000",7.6),("2012-0830-13:43-25300000",6.7),
             ("2012-0827-04:37-19650000",7.3),("2012-0826-15:53-7160000",6.6),
             ("2012-0814-02:59-3886000",7.7),("2012-0811-12:23-17670000",6.5),
             ("2012-0728-20:35-970000",6.7),("2012-0726-05:33-3386000",6.7),
             ("2012-0725-11:20-27880000",6.7),("2012-0528-07:23-520000",6.9),
             ("2012-0428-10:27-220000",6.7),("2012-0421-01:16-5370000",7.0),
             ("2012-0417-07:13-49880000",6.7),("2012-0417-03:50-15280000",8.2),
             ("2012-0412-07:15-49170000",8.6),("2012-0411-22:55-10820000",7.1),
             ("2012-0411-10:43-10530000",6.6),("2012-0411-08:38-37800000",7.5),
             ("2012-0325-22:37-6560000",7.0),("2012-0321-22:15-5590000",6.6),
             ("2012-0320-18:24-7620000",6.7),("2012-0314-09:08-36230000",6.7),
             ("2012-0309-19:53-320000",7.0),("2012-0303-12:19-55730000",6.6),
             ("2012-0226-06:17-19920000",6.7),("2012-0206-03:49-13920000",6.7),
             ("2012-0202-13:34-4110000",7.0),("2012-0115-13:40-21400000",6.6),
             ("2012-0110-18:37-0190000",7.2),("2012-0101-5:27-55800000",6.8)]

geo.add("",
        prov_list, 
        type_=ChartType.EFFECT_SCATTER
        )
# 添加数据项（即设置全图的范围）
geo.add_schema(maptype="world")

# 设置相关属性
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=6,max_=9),
                    title_opts=opts.TitleOpts(title="2012年大地震分布图"))

# 输出到网页文件
geo.render('./output/geo地震.html')