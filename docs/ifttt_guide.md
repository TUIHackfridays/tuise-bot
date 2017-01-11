# IFTTT Guide

This guide will help you create an IFTTT account, configure it and give an example on using it with this bot.

The interaction between the bot and IFTTT will work with the usage of the Maker functionality of IFTTT. This functionality allows you to create an applet that can receive a web request to a created weebhock. You'll create an event, pass parameters to it and call it using your own DIY project.

The request consists of an URL with the event name and the payload:
```
request_url = https://maker.ifttt.com/trigger/{SOME-CREATED-EVENT}/with/key/{IFTTT-KEY-HERE};
payload = {"value1" : "{A-VALUE-HERE}", "value2" : "{A-VALUE-HERE}", "value3" : "{A-VALUE-HERE}"};
post(request_url, data=payload);
```

The bot already has a function that makes this request. You just need to pass the event and the payload as parameters. (See bellow)
#TODO add-link-to-example

## Sign Up/Sign In
In order to connect to IFTTT you'll need to create an account first [sign up](https://ifttt.com/join) or if you already have one [sign in](https://ifttt.com/login).

![0-sign-in](http://i.imgur.com/Azs8pih.png)

## Maker connect
After creating the account access the [maker](https://ifttt.com/maker) to integrate IFTTT with the bot. Click the connect button.

![1-maker-connect](http://i.imgur.com/ljX3y7F.png)

You'll see the following screen after.

![2-maker-connected](http://i.imgur.com/GMRFcor.png)

Click the settings *button* on the right.

## Maker Setting
In the Maker settings you can see your key (in the image in red). Copy it into your `config.cfg` file in the `ifttt_key`.

![3-maker-settings](http://i.imgur.com/PuvqCns.png)

## Creating new applet
Click in `My Applets` you'll go to the screen shown in the image bellow.

![4-ifttt_my_applets](http://i.imgur.com/4nSDLGP.png)

Click the `New Applet` button on the top right.

## Applet Maker (this)
![5-new-applet-this](http://i.imgur.com/KXctlUg.png)

## Choose a Service
![6-choose-service](http://i.imgur.com/cBTD2g5.png)

## Choose a trigger
![7-service-triggers](http://i.imgur.com/hJDWM67.png)

## Set Event
![8-service-create-trigger](http://i.imgur.com/EFvEKRJ.png)

## Applet Maker (that)
![9-new-applet-that](http://i.imgur.com/ExHbIYp.png)

## Example of a that action
### Choose Action Service
![10-choose-action-service](http://i.imgur.com/YWJ743Q.png)

### Connect Device
![11-connect-device](http://i.imgur.com/l77HXxu.png)

### Set Parameters configuration
![12-device-config](http://i.imgur.com/CcikDW7.png)

## Review and Finish
![13-review-finish](http://i.imgur.com/kV14PGl.png)
