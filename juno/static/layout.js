
    import React from 'react';
    import ReactDOM from 'react-dom';
    import { FilterChart as Component} from 'pyxley';
    var filters = [{"options": {"alias": "Data", "label": "Data", "default": "Basement Temperature", "items": ["Basement Temperature", "Basement Humidity"]}, "type": "SelectButton"}];
var filter_style = "''";
var charts = [{"options": {"chart_id": "sensors-chart", "params": {"width": 1200, "buffer": 8, "top": 40, "height": 300, "right": 40, "init_params": {"Data": "Basement Temperature"}, "description": "Data from IoT sensors", "bottom": 30, "animate_on_load": "true", "transition_on_update": "true", "small_width_threshold": 160, "small_height_threshold": 120, "target": "#sensors-chart", "x_accessor": "x", "y_accessor": "y", "title": "Sensor Data", "left": 40}, "url": "/sensors-chart/"}, "type": "MetricsGraphics"}];
var dynamic = true;
    ReactDOM.render(
        <Component
        filters = { filters }
filter_style = { filter_style }
charts = { charts }
dynamic = { dynamic } />,
        document.getElementById("component_id")
    );
    