from pyecharts import Bar

attr = ["T-shirt", "sweater", "georgette", "pants", "high-heeled shoes", "socks"]
v1 = [50, 10, 80, 30, 15, 50]
v2 = [10, 90, 50, 10, 50, 10]
bar = Bar("Histogram data case")
bar.add("merchant1", attr, v1, is_stack=True)
bar.add("merchant2", attr, v2, is_stack=True)
bar.use_theme("dark")
bar.render()
