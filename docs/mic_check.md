# Microphone in Raspberry Pi

Open a terminal and before you connect your usb microphone/camera with microphone run the command `$ lsusb`
![lsusb_command1](http://i.imgur.com/MX5WMtM.png)

This command will display information about the USB buses in the system and the devices connected to them.

Now connect you microphone device and run the same command again.
![lsusb_command2](http://i.imgur.com/sOPOszK.png)
There a new device listed, your microphone.

Right click the volume icon on the topbar.
If the device is listed then click `External Device Settings`.

If not try updating the system `sudo apt-get update && sudo apt-get upgrade` and reboot (keep the device connected). After the reboot the device should show just like the image bellow.
![mic_1](http://i.imgur.com/s2ttirT.png)

Select the sound card, check that it's indeed the microphone and change the volume to your liking.
![mic_2](http://i.imgur.com/83Ox0Y3.png)
![mic_3](http://i.imgur.com/dkkN3eH.png)

In the browser click on the media icon and select the correct device.
![mic_4](http://i.imgur.com/zhuzxEu.png)
