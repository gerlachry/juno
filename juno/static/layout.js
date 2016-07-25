
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { FilterChart as Component} from 'pyxley';
    var filter_style = "''";
var filters = [{"options": {"label": "Data", "alias": "Data", "items": ["Basement Temperature", "Basement Humidity"], "default": "Basement Temperature"}, "type": "SelectButton"}];
var dynamic = true;
var charts = [{"options": {"params": {"top": 40, "description": "Line Chart", "animate_on_load": "true", "small_width_threshold": 160, "height": 200, "width": 450, "buffer": 8, "right": 40, "left": 40, "x_accessor": "x", "small_height_threshold": 120, "init_params": {"Data": "Basement Temperature"}, "y_accessor": "y", "title": "Line Chart", "bottom": 30, "target": "#sensors-chart", "transition_on_update": "true"}, "url": "/sensors-chart/", "chart_id": "sensors-chart"}, "type": "MetricsGraphics"}];
    ReactDOM.render(
        <Component
        filter_style = { filter_style }
filters = { filters }
dynamic = { dynamic }
charts = { charts } />,
        document.getElementById("component_id")
    );
    