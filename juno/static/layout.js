
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { FilterChart as Component} from 'pyxley';
    var charts = [{"type": "MetricsGraphics", "options": {"url": "/sensors-chart/", "chart_id": "sensors-chart", "params": {"small_height_threshold": 120, "animate_on_load": "true", "top": 40, "description": "Data from IoT sensors", "width": 1200, "height": 300, "small_width_threshold": 160, "target": "#sensors-chart", "y_accessor": "y", "title": "Sensor Data", "transition_on_update": "true", "x_accessor": "x", "bottom": 30, "init_params": {"Data": "Basement Temperature"}, "left": 40, "buffer": 8, "right": 40}}}];
var filter_style = "''";
var filters = [{"type": "SelectButton", "options": {"alias": "Data", "default": "Basement Temperature", "items": ["Basement Temperature", "Basement Humidity"], "label": "Data"}}];
var dynamic = true;
    ReactDOM.render(
        <Component
        charts = { charts }
filter_style = { filter_style }
filters = { filters }
dynamic = { dynamic } />,
        document.getElementById("component_id")
    );
    