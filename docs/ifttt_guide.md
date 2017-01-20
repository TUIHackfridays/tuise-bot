# IFTTT Guide

This guide will help you create an IFTTT account, configure it and give an example on using it with this bot.

The interaction between the bot and IFTTT will work with the usage of the Maker functionality of IFTTT. This functionality allows you to create an applet that can receive a web request to a created weebhock. You'll create an event, pass parameters to it and call it using your own DIY project.

The request consists of an URL with the event name and the payload:
```
request_url = https://maker.ifttt.com/trigger/{SOME-CREATED-EVENT}/with/key/{IFTTT-KEY-HERE};
payload = {"value1" : "{A-VALUE-HERE}", "value2" : "{A-VALUE-HERE}", "value3" : "{A-VALUE-HERE}"};
post(request_url, data=payload);
```

The bot already has a function that makes this request. You just need to pass the event and the payload as parameters. [(See bellow)](#TUISE-BOT)


## Sign Up / Sign In
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
After clicking on the `New Applet` button you'll be in the Applet Maker.
Here yoou'll have to click on the **+this** to select the service we want to use.

![5-new-applet-this](http://i.imgur.com/KXctlUg.png)


## Choose a Service
In this step type maker and select it. The Maker service is what we'll be using to call the event and trigger the corresponding action using the bot.

![6-choose-service](http://i.imgur.com/cBTD2g5.png)


## Choose a trigger
Here you'll select the trigger but since we are using the Maker you'll only have one trigger. The receive a web request trigger.

![7-service-triggers](http://i.imgur.com/hJDWM67.png)


## Set Event
Set the event name. This will the event that you'll be calling to trigger the that action.

![8-service-create-trigger](http://i.imgur.com/EFvEKRJ.png)


## Applet Maker (that)
After you create the trigger you'll be sent back to the applet maker screen. Now you'll select the service action you want to execute when you call the trigger.

![9-new-applet-that](http://i.imgur.com/ExHbIYp.png)


## Example of a that action
For an example of what you can do for actions we are going to show you how to setup an action that will interact with an android device.


### Choose Action Service
First select the android device service.

![10-choose-action-service](http://i.imgur.com/YWJ743Q.png)


### Connect Device
Connect with the device. And install IFTTT in your android device.

![11-connect-device](http://i.imgur.com/l77HXxu.png)


### Set Parameters configuration
Set the parameters for the trigger. In this example it's the the `value1` that is the song name.

![12-device-config](http://i.imgur.com/CcikDW7.png)


## Review and Finish
Check if everythinh is ok and finish.

![13-review-finish](http://i.imgur.com/kV14PGl.png)


## TUISE-BOT
In the bot you'll to add a new command and add it to the configurations and the `main_commands.py`.
For the above example we want the event **"play song android"**.

### Add the command to bot_config
We added the following commands to the commands object in bot_config file.

```
"play song on android": {
  "triggers": [
    "play song on android",
    "play song in android",
    "play song android",
    "play android song"
  ]
}
```

### Add the code to call the command
Now in the `main_commands.py` we added the following code:

```python
elif command == "play song on android":
      talk, result = ifttt_call("play_song_on_android", {"value1" : "Alan Walker - Fade", "value2" : "", "value3" : ""})
```

- The **ifttt_call()** function is what will call the applet we just made.
- This function receives 2 parameters: the **event** and the **payload**.
 * **event**: the name you game the event in the IFTTT configuration in this example: `play_song_android`.
 * **payload**: a dictionary with the following structure:
 ```
 {"value1" : "DATA-HERE", "value2" : "DATA-HERE", "value3" : "DATA-HERE"}
 ```
 When you make the applet you'll see the these values `value1`, `value2` and `value3` that match with the payload values. Just like the example above we used `value1` to pass the song name.
