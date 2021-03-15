import re
import subprocess
from influxdb import InfluxDBClient


def _run(exec_count=0):
    try:
        response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True,
                                    stdout=subprocess.PIPE).stdout.read().decode('utf-8')
        ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
        download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
        upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

        ping = ping[0].replace(',', '.')
        download = download[0].replace(',', '.')
        upload = upload[0].replace(',', '.')

        speed_data = [
            {
                "measurement": "internet_speed",
                "tags": {
                    "host": "bananapi"
                },
                "fields": {
                    "download": float(download),
                    "upload": float(upload),
                    "ping": float(ping)
                }
            }
        ]

        client = InfluxDBClient('localhost', 8086,
                                username='',
                                password='',
                                database='')
        client.write_points(speed_data)
    except Exception:
        if exec_count < 5:
            exec_count += 1
            _run(exec_count)


_run()
