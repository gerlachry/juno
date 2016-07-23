from flask import jsonify, request
from pyxley.charts.mg import LineChart


class ESSensorLineChart(LineChart):
    def __init__(self, df, figure, x, y, es_helper, title="Line Chart",
                 description="Line Chart", init_params={}, timeseries=False,
                 route_func=None):

        self.plot_opts = {
            "title": title,
            "description": description,
            "target": "#" + figure.chart_id,
            "x_accessor": "x",
            "y_accessor": "y",
            "init_params": init_params
        }
        for k, v in list(figure.get().items()):
            self.plot_opts[k] = v

        self.es_helper = es_helper

        if not route_func:
            def get_data():
                args = {}
                for c in init_params:
                    if request.args.get(c):
                        args[c] = request.args[c]
                    else:
                        args[c] = init_params[c]
                data_frame = self.es_helper.test_df()
                return jsonify(LineChart.to_json(
                    self.apply_filters(data_frame, args),
                    x,
                    y,
                    timeseries=timeseries
                ))

            route_func = get_data

        super(LineChart, self).__init__(figure.chart_id, figure.url, self.plot_opts, route_func)