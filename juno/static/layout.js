
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { FilterChart as Component} from 'pyxley';
    var dynamic = true;
var filters = [{"type": "SelectButton", "options": {"items": ["Basement Temperature", "Basement Humidity"], "label": "Data", "default": "Basement Temperature", "alias": "Data"}}];
var filter_style = "''";
var charts = [{"type": "MetricsGraphics", "options": {"params": {"left": 40, "height": 300, "transition_on_update": "true", "small_width_threshold": 160, "width": 1200, "animate_on_load": "true", "top": 40, "bottom": 30, "description": "Data from IoT sensors", "y_accessor": "y", "title": "Sensor Data", "init_params": {"Data": "Basement Temperature"}, "right": 40, "small_height_threshold": 120, "target": "#sensors-chart", "buffer": 8, "x_accessor": "x"}, "chart_id": "sensors-chart", "url": "/sensors-chart/"}}];
    ReactDOM.render(
        <Component
        dynamic = { dynamic }
filters = { filters }
filter_style = { filter_style }
charts = { charts } />,
        document.getElementById("component_id")
    );
    