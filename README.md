# Aws-Greengrass-Component-Samples

## PublishSwitchState-1.0.0 Component
![](https://github.com/dsonoda/Aws-IoT-Edge-Architecture-Samples/blob/images/components/com.example.PublishSwitchState-1.0.0/architecture.png)

[commentary article](https://qiita.com/dsonoda/items/b2e6557f9bfa29ecee14)

```shell
$ sudo /greengrass/v2/bin/greengrass-cli deployment create \
   --recipeDir /home/pi/Aws-IoT-Edge-Architecture-Samples/components/recipes \
   --artifactDir /home/pi/Aws-IoT-Edge-Architecture-Samples/components/artifacts \
   --merge "com.example.PublishSwitchState=1.0.0"
```

## PublishLedStatus-1.0.0 Component
![](https://github.com/dsonoda/Aws-IoT-Edge-Architecture-Samples/blob/images/components/com.example.PublishLedStatus-1.0.0/architecture.png)

[commentary article](https://qiita.com/dsonoda/items/1c29497e2c8088296e88)

```shell
$ sudo /greengrass/v2/bin/greengrass-cli deployment create \
   --recipeDir /home/pi/Aws-IoT-Edge-Architecture-Samples/components/recipes \
   --artifactDir /home/pi/Aws-IoT-Edge-Architecture-Samples/components/artifacts \
   --merge "com.example.PublishLedStatus=1.0.0"
```
