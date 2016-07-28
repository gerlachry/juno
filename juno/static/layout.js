
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { FilterChart as Component} from 'pyxley';
    var charts = [{"options": {"url": "/sensors-chart/", "chart_id": "sensors-chart", "params": {"y_accessor": "y", "x_accessor": "x", "animate_on_load": "true", "target": "#sensors-chart", "init_params": {"Data": "Basement Temperature"}, "bottom": 30, "width": 1200, "transition_on_update": "true", "left": 40, "buffer": 8, "small_width_threshold": 160, "small_height_threshold": 120, "description": "Data from IoT sensors", "top": 40, "height": 300, "right": 40, "title": "Sensor Data"}}, "type": "MetricsGraphics"}];
var filter_style = "''";
var filters = [{"options": {"label": "Data", "alias": "Data", "default": "Basement Temperature", "items": ["Basement Temperature", "Basement Humidity"]}, "type": "SelectButton"}];
var dynamic = true;
    ReactDOM.render(
        <Component
        charts = { charts }
filter_style = { filter_style }
filters = { filters }
dynamic = { dynamic } />,
        document.getElementById("component_id")
    );
    