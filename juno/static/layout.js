
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { FilterChart as Component} from 'pyxley';
    var charts = [{"options": {"chart_id": "sensors-chart", "url": "/sensors-chart/", "params": {"x_accessor": "x", "bottom": 30, "small_width_threshold": 160, "buffer": 8, "description": "Sensor Data", "transition_on_update": "true", "right": 40, "title": "Line Chart", "small_height_threshold": 120, "left": 40, "target": "#sensors-chart", "animate_on_load": "true", "height": 400, "init_params": {"Data": "Basement Temperature"}, "top": 40, "y_accessor": "y", "width": 600}}, "type": "MetricsGraphics"}];
var dynamic = true;
var filters = [{"options": {"label": "Data", "default": "Basement Temperature", "alias": "Data", "items": ["Basement Temperature", "Basement Humidity"]}, "type": "SelectButton"}];
var filter_style = "''";
    ReactDOM.render(
        <Component
        charts = { charts }
dynamic = { dynamic }
filters = { filters }
filter_style = { filter_style } />,
        document.getElementById("component_id")
    );
    