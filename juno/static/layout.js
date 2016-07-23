
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { FilterChart as Component} from 'pyxley';
    var filters = [{"options": {"alias": "Data", "default": "Basement Temperature", "label": "Data", "items": ["Basement Temperature", "Basement Humidity"]}, "type": "SelectButton"}];
var charts = [{"options": {"url": "/sensors-chart/", "params": {"right": 40, "left": 40, "small_width_threshold": 160, "top": 40, "transition_on_update": "true", "buffer": 8, "init_params": {"Data": "Basement Temperature"}, "height": 200, "animate_on_load": "true", "width": 450, "target": "#sensors-chart", "x_accessor": "x", "description": "Line Chart", "bottom": 30, "title": "Line Chart", "small_height_threshold": 120, "y_accessor": "y"}, "chart_id": "sensors-chart"}, "type": "MetricsGraphics"}];
var filter_style = "''";
var dynamic = true;
    ReactDOM.render(
        <Component
        filters = { filters }
charts = { charts }
filter_style = { filter_style }
dynamic = { dynamic } />,
        document.getElementById("component_id")
    );
    