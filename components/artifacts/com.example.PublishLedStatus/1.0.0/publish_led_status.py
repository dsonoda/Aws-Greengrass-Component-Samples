import RPi.GPIO as GPIO
import time
import datetime
import json
import awsiot.greengrasscoreipc
from awsiot.greengrasscoreipc.model import (
    QOS,
    PublishToIoTCoreRequest
)


# Raspberry Pi4 GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

SLEEP_SEC = 3
TIMEOUT = 10
qos = QOS.AT_LEAST_ONCE

# AWS IoT Core topic
topic = "raspberrypi4/led"

ipc_client = awsiot.greengrasscoreipc.connect()

status = GPIO.LOW
while True:
    now_timestamp = datetime.datetime.now()

    if GPIO.input(24) == GPIO.HIGH:
        GPIO.output(25, GPIO.HIGH)
        status = GPIO.HIGH
    else:
        GPIO.output(25, GPIO.LOW)
        status = GPIO.LOW

    message = {
        "timestamp": str(now_timestamp),
        "led_status": status
    }
    message_json = json.dumps(message).encode('utf-8')

    request = PublishToIoTCoreRequest()
    request.topic_name = topic
    request.payload = message_json
    request.qos = qos
    operation = ipc_client.new_publish_to_iot_core()
    operation.activate(request)
    future = operation.get_response()
    future.result(TIMEOUT)

    with open('/tmp/Greengrass_PublishLedStatus.log', 'a') as f:
        print(f"{str(now_timestamp)} / status: {status}.", file=f)

    time.sleep(SLEEP_SEC)