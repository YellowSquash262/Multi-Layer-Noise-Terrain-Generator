# Multi-Layer-Noise-Terrain-Generator


Description:
  This script creates 2 lists of diferent intensities of perlin noise and adds them together to add diferent layers. it then goes through each value and if it is within a certian range, it gives it a specific color (layers of terain). it then displays the colored list on the screen using pygame.
  

Link: Here is the link but be warned this code in uncomented and im a child so wtv good luck https://replit.com/@YellowSquash262/Multi-layer-noise-Terrain-simulator#main.py:~:text=Pane%20Actions-,Output,-Pane%20Actions


Deatailed description:
  Lists: This script creates 2 lists of 'rows' colomns and rows.
  
  Random Numbers: It then goes through the lists and gives each item a random int (using 'import random') between 'intensity' and -'intensity'. 
  
  Smoothing: After this, the script goes through every item and takes in all the numbers in a square around it (if the item is on the border it just gets the other items around it that are in the lists) and averages them out and changes it by 'changeV' for the first list and 'changeV2' for the second.
  
  Iterations: it repeates this "Smoothing" prosess for 'iterationsV', first lisiterationsrationsV2', second list.
  (Both lists of noise are created by now)
  
  Combining: To make the Perlin Noise layered, it combines both lists by just adding each parallel item to each other.
  (the final list of multi layer noise is created bt now)
  
  Displaying: Using pygame to display (it worked and I couldn't think of anything else) I go through and check what color (terrain layer) the int falls under and display it in its proper place on the screen with its proper color.
  
  
Why this is ground breaking:
  Im new to GitHub this is my first rep and i would really apritiate it if u upvoted it or whatever GitHub has, this isn't ground breaking but whatever thanks bye feel free to copy or wtv. if u wanna give me money im down.
  
  :) Max
  
  

