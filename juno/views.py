import pandas as pd
from pyxley import UILayout
from pyxley.charts.mg import Figure
from pyxley.filters import SelectButton

from juno.charts.es_charts import ESSensorLineChart


def build_ui(app, es_helper):
    ui = UILayout(
        "FilterChart",
        "pyxley",
        "component_id",
        filter_style="''")

    # Make a Button
    cols = ['Basement Temperature', 'Basement Humidity']
    btn = SelectButton("Data", cols, "Data", "Basement Temperature")

    # Make a FilterFrame and add the button to the UI
    ui.add_filter(btn)

    # Make a Figure, add some settings, make a line plot
    fig = Figure("/sensors-chart/", "sensors-chart")
    fig.graphics.transition_on_update(True)
    fig.graphics.animate_on_load()
    fig.layout.set_size(width=450, height=200)
    fig.layout.set_margin(left=40, right=40)
    lc = ESSensorLineChart(fig, "Date", ["Basement Temperature"], es_helper, init_params={"Data": "Basement Temperature"},
                   timeseries=True)
    ui.add_chart(lc)

    sb = ui.render_layout(app, "./static/layout.js")

    # Create a webpack file and bundle our javascript
    from pyxley.utils import Webpack
    wp = Webpack(".")
    wp.create_webpack_config(
        "layout.js",
        "./static/",
        "bundle",
        "./static/"
    )
    wp.run()
