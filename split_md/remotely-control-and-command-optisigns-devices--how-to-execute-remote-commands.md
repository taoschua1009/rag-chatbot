### How to Execute Remote Commands

To submit the command to manage the devices remotely, you will need to go to the remote command execution console. Click **Screens** , then the **More Options (Three Dots)**

Screens -> More Options Icon -> Execute Remote Commands



The Execute Remote Commands console can be broken down into three sections:

  * **Section 1** \- Where you specify the target of the commands.
  * **Section 2** \- The command you want to execute.
  * **Section 3** \- The execution result and history.





For section 1, there are 2 types of targets you can choose from:

  * **Screens** \- You can select the screen name here, it can be one screen or multiple screens.
  * **Tags** \- Utilizing tags, you can execute the command on a group of devices. In the below example, the command will be submitted to all devices tagged as Windows or Raspberry Pi.





For section 2, you can enter the command you want to execute in the text box. The command needs to be OS-specific, depending on the OS your device is running on (Android for Android Stick, Linux for OptiSigns Pro / ProMax players), you will need to build the scripts accordingly. Once you have your commands ready, just click the submit button. The command will be pushed to the devices for execution.

Other than the free-form scripts, there are some common commands built into the platform, to achieve these functions, you will just need to select it from the drop-down menu. Depending on the type of device OS, the command will be submitted accordingly.



After a command is executed, it will appear in section 3: the command history.

**NOTE**  
---  
The **Refresh & Relaunch **command can be used on any device. The **Reboot Device** command cannot be used on certain Android devices.

For additional information, see the full article [here](https://support.optisigns.com/hc/en-us/articles/30010338528659)

---
