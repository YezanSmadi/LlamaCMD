// Welcome to LlamaCMD //

<img width="256" height="256" alt="llama" src="https://github.com/user-attachments/assets/9edb2907-db0a-406a-b8aa-4f7e0f78b7c1" />

This tool is intended to help accelerate your video editing workflow by allowing you to 
encode/mux clips in one place with the choice of trimming those clips down without having to
resort to ffmpeg commands in the terminal or batch scripts within the directory.

Clip aggregation in video editing is one of the most time consuming parts of the process,
so hopefully this helps.


// Set Up //

To get the cleanest use out of LlamaCMD, you'll want to add the .exe to your PATH environment. This way, you can
call LlamaCMD from the terminal anywhere on your computer rather than drag the .exe around everywhere you want to 
use it.

If you don't know how to do it, I'll guide you through it.

#
|    First, place the .exe in a cozy folder it can sit in. Keep it secret, keep it safe.                     
|                                                                                                            
|    Copy the directory address to this folder by double clicking an empty area in the bar                   
|    detailing the address at the top of your file explorer, selecting the entire address, and               
|    copying it. We'll need this for later.                                                                  
|                                                                                                            
|    Next, go to your control panel. Click "System". It'll pop up another window detailing your PC.          
|    Scroll to the bottom and click "Advanced System Settings". This will pop up a tiny window that          
|    should already be on the Advanced tab.                                                                  
|                                                                                                            
|    From here, click on "Environment Variables..." at the bottom. This will pop up yet another window       
|    (we have one last window after this, I promise). Here, under "User variables for ____" click on the     
|    "Path" row and hit the "Edit..." button.                                                                
|                                                                                                            
|    Now, hit the new button and paste the directory address where LlamaCMD.exe resides into the box. Hit    
|    okay. Now close out                                                                                     
|    all those windows littered everywhere.                                                                  
|                                                                                                            
|    You can now use LlamaCMD anywhere.                                                                      
#

If you don't want to add to PATH, just make sure LlamaCMD.exe is in the same directory as the files you want to use.


The text in LlamaCMD is also colorcoded. By default (without termcolor installed), the text is plain. But if you would like, you can enable this 
colorcoding by opening up a regular CMD window and installing termcolor by inputting:

#
|   pip install termcolor
#

You should now have color in LlamaCMD.


