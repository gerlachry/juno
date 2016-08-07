
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { FilterChart as Component} from 'pyxley';
    var dynamic = true;
var charts = [{"options": {"chart_id": "sensors-chart", "url": "/juno/sensors-chart/", "params": {"y_accessor": "y", "target": "#sensors-chart", "buffer": 8, "right": 40, "bottom": 30, "width": 1200, "x_accessor": "x", "title": "Sensor Data", "description": "Data from IoT sensors", "left": 40, "transition_on_update": "true", "small_height_threshold": 120, "small_width_threshold": 160, "animate_on_load": "true", "top": 40, "init_params": {"Data": "Basement Temperature"}, "height": 300}}, "type": "MetricsGraphics"}];
var filter_style = "''";
var filters = [{"options": {"label": "Data", "alias": "Data", "default": "Basement Temperature", "items": ["Basement Temperature", "Basement Humidity"]}, "type": "SelectButton"}];
    ReactDOM.render(
        <Component
        dynamic = { dynamic }
charts = { charts }
filter_style = { filter_style }
filters = { filters } />,
        document.getElementById("component_id")
    );
    