# from pyecharts import options as opts
# from pyecharts.charts import Pie
# from pyecharts.faker import Faker

# c4 = (
#     Pie()
#     .add(
#         "",
#         [list(z) for z in zip(["男","女","保密"], ["404",'103','673'])],
#         radius=["40%", "75%"],
#     )
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="性别分布"),
#         legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
#     )
#     .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#     .render_notebook()
    
# )
# c4
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(Faker.choose(), Faker.values())],
        # 饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标
        # 默认设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie-调整位置"),
        legend_opts=opts.LegendOpts(pos_left="15%"), #图例位置调整
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_position.html")
)


