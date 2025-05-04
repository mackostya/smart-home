import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from bmp280 import BMP280
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
       
if __name__ == "__main__":
    print("Initialising BMP280 and InfluxDB client...")
    counter = 0
    # Initialise the BMP280
    bus = SMBus(1)
    bmp280 = BMP280(i2c_dev=bus)
    
    token = os.environ.get("INFLUXDB_TOKEN")
    org = "pi"
    url = "http://192.168.0.217:8086"

    write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    bucket="temperature"

    write_api = write_client.write_api(write_options=SYNCHRONOUS)
    time_sleep = 60 * 5 # time interval in seconds
    degree_sign = u"\N{DEGREE SIGN}"
    
    print("Initialised BMP280 and InfluxDB client.")
    print(f"Starting data collection with time interval of {time_sleep}s...")
    print("Press Ctrl+C to exit!")
    while True:
        counter += 1
        temperature = bmp280.get_temperature()
        pressure = bmp280.get_pressure()
        point = (
            Point("living_room")
            .tag("T", "T")
            .field("T", temperature)
        )
        write_api.write(bucket=bucket, org="pi", record=point)
        point = (
            Point("living_room")
            .tag("P", "P")
            .field("P", pressure)
        )
        write_api.write(bucket=bucket, org="pi", record=point)
        if counter % 10 == 0:
            print("10 points written to InfluxDB.")
            format_temp = "{:.2f}".format(temperature)
            format_press = "{:.2f}".format(pressure)
            print('Temperature = ' + format_temp + degree_sign + 'C')
            print('Pressure = ' + format_press + ' hPa \n')
        time.sleep(time_sleep)