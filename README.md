telegram_cam_with_motion


# telegram_cam_with_motion
control motion surveillance software with a Telegram-bot

## What does it so?

Get a gif in Telegram every time your cam detected something.
Basic controls for motion are accessable via telegram-bot.

##What do i need?
- Telegram account, bot, token
- a webcam
- a computer
- a linux (debina like)

- Python and the following libraries:
  
  ```pip install requests python-telegram-bot --upgrade```
  
- the motion software

  ```apt-get install motion```
  
## Setup
- put motion.conf and python file motion_control_telegram_bot.py in home directory
- add to /etc/rc.local:
  ```
  modprobe bcm2835-v4l2 #if running on a raspberry
  
  motion -c /home/pi/motion.conf
  
  python /home/pi/motion_control_telegram_bot.py
  ```
- replace your login credentials
- restart the computer
