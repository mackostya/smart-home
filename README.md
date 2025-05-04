# Smart Home

Smart home deployment with [grafana](https://grafana.com/) and [influx-db](https://www.influxdata.com/).

# Deployment

The deployment is on raspberry pi:
- [Grafana Deployment on Raspberry Pi](https://grafana.com/tutorials/install-grafana-on-raspberry-pi/)
- [InfluxDB Deployment on Raspberry Pi](https://pimylifeup.com/raspberry-pi-influxdb/)

# Grafana configs

- **/etc/grafana/grafana.ini**
- **/usr/share/grafana/conf**

For anonymous authentification:

```ini
[auth]
disable_login_form = true

[auth.basic]
enabled = false

[auth.anonymous]
enabled = true
org_name = Main Org.
org_role = Viewer
```


```sh
sudo systemctl restart grafana-server
```