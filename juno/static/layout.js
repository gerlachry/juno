
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { FilterChart as Component} from 'pyxley';
    var dynamic = true;
var filter_style = "''";
var charts = [{"options": {"chart_id": "sensors-chart", "params": {"title": "Sensor Data", "small_width_threshold": 160, "target": "#sensors-chart", "small_height_threshold": 120, "x_accessor": "x", "bottom": 30, "top": 40, "width": 1200, "right": 40, "animate_on_load": "true", "y_accessor": "y", "description": "Data from IoT sensors", "transition_on_update": "true", "left": 40, "buffer": 8, "height": 300, "init_params": {"Data": "Basement Temperature"}}, "url": "/sensors-chart/"}, "type": "MetricsGraphics"}];
var filters = [{"options": {"items": ["Basement Temperature", "Basement Humidity"], "label": "Data", "alias": "Data", "default": "Basement Temperature"}, "type": "SelectButton"}];
    ReactDOM.render(
        <Component
        dynamic = { dynamic }
filter_style = { filter_style }
charts = { charts }
filters = { filters } />,
        document.getElementById("component_id")
    );
    