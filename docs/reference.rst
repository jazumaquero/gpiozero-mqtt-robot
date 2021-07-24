{%- macro heading(text) -%}
{{text}}
{% for _ in text %}-{% endfor %}
{%- endmacro -%}
Reference
=========

.. contents::
    :local:
    :backlinks: none


{{ heading( gpiozero_mqtt_robot) }}

.. automodule:: gpiozero_mqtt_robot.main
   :members:
