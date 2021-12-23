AWS IoT Greengrass V2 Component samples.
___

# Software versions  
- Raspberry Pi 4
- Raspbian Ver.11
- Python 3.9.2
- pip 20.3.4
- Java 11.0.13
- aws cli 1.22.23

# PublishSwitchState-1.0.0 Component  
<img src="https://github.com/dsonoda/Aws-IoT-Edge-Architecture-Samples/blob/images/components/com.example.PublishSwitchState-1.0.0/main.png" width="600px">  

\> [article page](https://qiita.com/dsonoda/items/b2e6557f9bfa29ecee14)  

Extend the configuration on the cloud side and try to work with AWS IoT Events, which can detect events on edge devices (Raspberry Pi) and lead to arbitrary action execution.  

![](https://github.com/dsonoda/Aws-IoT-Edge-Architecture-Samples/blob/images/components/com.example.PublishSwitchState-1.0.0/architecture.png)  

On the edge device side, we will use a circuit with two switches and one LED connected as a way to represent a pseudo "status". The "status" is determined by the on/off combination of the two switches and is sent to the cloud via MQTT.  

The relationship between the "status", the state of the switch, and the value sent to the cloud is as follows.  

| switch 2 | switch 1 | status to be sent to the cloud |
|:---:|:---:|:---:|
|off |off |0 |
|off |on |1 |
|on |off |2 |
|on |on |3 |

The following is a state machine diagram of AWS IoT Events prepared on the cloud side.  

<img src="https://github.com/dsonoda/Aws-IoT-Edge-Architecture-Samples/blob/images/components/com.example.PublishSwitchState-1.0.0/aws_iot_events_state_machine.png" width="600px">  

It is assumed that there are only two types of flows as follows.  

- 0 (system is booting) -> 1 (processing) -> 2 (processing completed) -> 0 (system is booting)...  
- 0 (system is running) -> 1 (processing) -> 3 (error occurred) -> 0 (system is running)...  

When an error occurs, a notification email is sent using Amazon SNS.  
Since the status transition on the edge device side is pseudo-expressed by turning the button on and off, it is necessary to press the buttons so that the status changes in the above order.  

deploy command  
```shell
$ sudo /greengrass/v2/bin/greengrass-cli deployment create \
 --recipeDir /home/pi/Aws-IoT-Edge-Architecture-Samples/components/recipes \
 --artifactDir /home/pi/Aws-IoT-Edge-Architecture-Samples/components/artifacts \
 --merge "com.example.PublishSwitchState=1.0.0"
```

# PublishLedStatus-1.0.0 Component  
<img src="https://github.com/dsonoda/Aws-IoT-Edge-Architecture-Samples/blob/images/components/com.example.PublishLedStatus-1.0.0/main.png" width="600px">  

\> [article page](https://qiita.com/dsonoda/items/1c29497e2c8088296e88)  

Try remote monitoring of devices using AWS IoT Core on the cloud side and Raspberry Pi 4 on the edge side devices.  

Build an electronic circuit on the Raspberry Pi that will cause the LED to blink when the switch is turned on and off. We will also send MQTT messages to the IoT Core on the cloud side while monitoring the LED blinking on and off from the Greengrass component in 3-second cycles.
Eventually, we aim to be able to check the blinking status of the Raspberry Pi from the AWS IoT Core console in the cloud.

![](https://github.com/dsonoda/Aws-IoT-Edge-Architecture-Samples/blob/images/components/com.example.PublishLedStatus-1.0.0/architecture.png)  

The relationship between the switch, the LED status, and the status sent by MQTT is as follows.

| switch | led | status to be sent to the cloud |
|:---:|:---:|:---:|
|on |lighting |1 |
|off |off the light |0 |

deploy command  
```shell
$ sudo /greengrass/v2/bin/greengrass-cli deployment create \
 --recipeDir /home/pi/Aws-IoT-Edge-Architecture-Samples/components/recipes \
 --artifactDir /home/pi/Aws-IoT-Edge-Architecture-Samples/components/artifacts \
 --merge "com.example.PublishLedStatus=1.0.0"
```
