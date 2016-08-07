
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { FilterChart as Component} from 'pyxley';
    var dynamic = true;
var filters = [{"options": {"label": "Data", "alias": "Data", "default": "Basement Temperature", "items": ["Basement Temperature", "Basement Humidity"]}, "type": "SelectButton"}];
var filter_style = "''";
var charts = [{"options": {"chart_id": "sensors-chart", "url": "/juno/sensors-chart/", "params": {"target": "#sensors-chart", "left": 40, "x_accessor": "x", "top": 40, "init_params": {"Data": "Basement Temperature"}, "transition_on_update": "true", "y_accessor": "y", "bottom": 30, "small_height_threshold": 120, "description": "Data from IoT sensors", "right": 40, "small_width_threshold": 160, "width": 1200, "height": 300, "buffer": 8, "animate_on_load": "true", "title": "Sensor Data"}}, "type": "MetricsGraphics"}];
    ReactDOM.render(
        <Component
        dynamic = { dynamic }
filters = { filters }
filter_style = { filter_style }
charts = { charts } />,
        document.getElementById("component_id")
    );
    