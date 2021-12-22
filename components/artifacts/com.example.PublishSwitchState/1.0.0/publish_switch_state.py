import RPi.GPIO as GPIO
import time
import datetime
import json
import awsiot.greengrasscoreipc
from awsiot.greengrasscoreipc.model import (
    QOS,
    PublishToIoTCoreRequest
)


BIT_10_PLACE_PIN = 23
BIT_1_PLACE_PIN = 24
LED_PIN = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BIT_10_PLACE_PIN, GPIO.IN)
GPIO.setup(BIT_1_PLACE_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

DEVICE_ID = "RaspberryPi4"
SLEEP_TIME = 4
topic = "raspberrypi4/switches"
qos = QOS.AT_LEAST_ONCE

ipc_client = awsiot.greengrasscoreipc.connect()


def convert_bin_2_int(pin2_status: int, pin1_status: int) -> int:
    return int("%s%s" % (pin2_status, pin1_status), 2)


while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)

    datetime_now = str(datetime.datetime.now())
    switch_status = convert_bin_2_int(GPIO.input(BIT_10_PLACE_PIN), GPIO.input(BIT_1_PLACE_PIN))

    message = {
        "device_id": DEVICE_ID,
        "switch_status": switch_status,
        "timestamp": datetime_now
    }
    message_json = json.dumps(message).encode('utf-8')

    request = PublishToIoTCoreRequest()
    request.topic_name = topic
    request.payload = message_json
    request.qos = qos
    operation = ipc_client.new_publish_to_iot_core()
    operation.activate(request)
    future = operation.get_response()
    future.result(10)

    with open('/tmp/Greengrass_PublishSwitchState.log', 'a') as f:
        print(f"{datetime_now} / switch_status: {switch_status}.", file=f)

    time.sleep(SLEEP_TIME)


GPIO.cleanup()