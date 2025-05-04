import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from bmp280 import BMP280
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
       
if __name__ == "__main__":
    # Initialise the BMP280
    bus = SMBus(1)
    bmp280 = BMP280(i2c_dev=bus)
    
    token = os.environ.get("INFLUXDB_TOKEN")
    org = "pi"
    url = "http://192.168.0.217:8086"

    write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    bucket="temperature"

    write_api = write_client.write_api(write_options=SYNCHRONOUS)
    
    
    while True:
        temperature = bmp280.get_temperature()
        pressure = bmp280.get_pressure()
        point = (
            Point("living_room")
            .tag("T", "T")
            .field("T", temperature)
        )
        write_api.write(bucket=bucket, org="pi", record=point)
        time.sleep(5) # separate points by 1 second