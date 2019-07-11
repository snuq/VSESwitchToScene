# VSE Switch To Scene Addon For Blender

This script assists in using Scene strips in the Blender VSE by providing a way to quickly switch to and from editing them.

Development for this script is supported by my multimedia and video production business, [Creative Life Productions](http://www.creativelifeproductions.com)  
But, time spent working on this addon is time I cannot spend earning a living, so if you find this addon useful, consider donating:  

PayPal | Bitcoin
------ | -------
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=XHRXZBQ3LGLH6) | ![Bitcoin Donate QR Code](http://www.snuq.com/snu-bitcoin-address.png) <br> 1JnX9ZFsvUaMp13YiQgr9V36EbTE2SA8tz  

Or support me by hiring Creative Life Productions if you have a need for the services provided.


## Installation
* Download 'VSESwitchToScene.py'.  
* Open Blender, and from the 'File' menu, select 'User Preferences'.
* In this new window, click on the "Add-ons" tab at the left.
* Click the 'Install Add-on from File...' button at the bottom of this window.
* Browse to and select the 'VSESwitchToScene.py' file, click the 'Install Add-on from File' button.
* You should now see the addon displayed in the preferences window, click the checkbox next to the name to enable it.


## VSE Panel
This addon adds a new panel to the sequence editor properties sidebar, this panel is under the 'Strip' tab and titled 'VSE Switch To Scene'.  Note this panel is only visible when a scene strip is active.

* __Workspace Menu__

    A menu for selecting the workspace to automatically switch to when the scene is switched to.

* __Switch To Scene Button__

    Switches to the selected scene strip's scene, and the above selected workspace.


## Header Buttons
This addon adds a button to the VSE, 3D View and Compositor headers.  This button is only visible when the scene has been switched to with this addon.  Clicking this button will return Blender to the original Scene and Workspace.  
The button will be called 'Switch Back To: "Scene Name"'.


## Shortcuts
* __Tab Key__

    When a scene strip is active, this will activate the 'Switch-To' function.

* __Shift-Tab__

    In the VSE, after switching to a scene, this will activate the 'Switch-Back' function.

