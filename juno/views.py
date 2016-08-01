import os
from pyxley import UILayout
from pyxley.charts.mg import Figure, LineChart
from pyxley.filters import SelectButton

from charts.es_charts import ESSensorLineChart

DIR = os.path.dirname(os.path.realpath(__file__))


def build_ui(app, db, build=False):
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
    fig.layout.set_size(width=1200, height=300)
    fig.layout.set_margin(left=40, right=40)
    lc = LineChart(None, fig, "Date", ["Basement Temperature"], init_params={"Data": "Basement Temperature"},
                   route_func=db.get_data, timeseries=True, title='Sensor Data', description="Data from IoT sensors")
    ui.add_chart(lc)
    sb = ui.render_layout(app, os.path.join(DIR, "static/layout.js"))

    if build:
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
