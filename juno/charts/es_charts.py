from flask import jsonify, request
from pyxley.charts.mg import LineChart


class ESSensorLineChart(LineChart):
    def __init__(self, figure, x, y, es_helper, title="Line Chart",
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
                return jsonify(self.es_helper.get_data(args,
                    timeseries=timeseries
                ))

            route_func = get_data

        super(LineChart, self).__init__(figure.chart_id, figure.url, self.plot_opts, route_func)