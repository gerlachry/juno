
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { FilterChart as Component} from 'pyxley';
    var dynamic = true;
var filters = [{"options": {"items": ["Basement Temperature", "Basement Humidity"], "label": "Data", "default": "Basement Temperature", "alias": "Data"}, "type": "SelectButton"}];
var charts = [{"options": {"params": {"y_accessor": "y", "small_height_threshold": 120, "left": 40, "description": "Data from IoT sensors", "bottom": 30, "height": 300, "target": "#sensors-chart", "width": 1200, "title": "Sensor Data", "small_width_threshold": 160, "animate_on_load": "true", "right": 40, "init_params": {"Data": "Basement Temperature"}, "x_accessor": "x", "top": 40, "buffer": 8, "transition_on_update": "true"}, "url": "/sensors-chart/", "chart_id": "sensors-chart"}, "type": "MetricsGraphics"}];
var filter_style = "''";
    ReactDOM.render(
        <Component
        dynamic = { dynamic }
filters = { filters }
charts = { charts }
filter_style = { filter_style } />,
        document.getElementById("component_id")
    );
    