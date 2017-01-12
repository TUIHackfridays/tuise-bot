# Tuise-bot frontend

## Interaction

**Steps**

1. Say trigger words

2. Bot responds

3. Say command

4. Bot responds

5. Repeat

----

When you access the page you'll see something like the image bellow.

![start_screen](http://i.imgur.com/88mu7za.png)

Here you can wake the bot by saying one of the trigger words and he will respond just like the screenshot bellow. You'll also ear a beep like sound that means that you can say your command.

![triggered_screen](http://i.imgur.com/5atGdBO.png)

The commands that the bot already has are `ping` and `question`. It also has an example command for IFTTT (`play song on android`) but this needs the applet need to be configured first for it to work.

The image bellow is the result of the following steps:
- saying *trigger word*
- bot answers by saying the greeting
- saying *`"question meaning of life"`* after beep

![response_screen](http://i.imgur.com/UtYRdBC.png)


## Change the voice recognizer language
If you wish to change the language recognized you can do so by going into `js/app.js` and editing the following line (line 65):

```javascript
recognizer.lang = 'en-US'; // set language
```

### Note
Open in Google Chrome has this uses `Speech Recognition API` and currently only Chrome and Opera have partial support for it.
