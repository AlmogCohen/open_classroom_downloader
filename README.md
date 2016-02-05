Stanford OpenClassroom Downloader
===================

Enchance the great learning experience of [Stanford OpenClassroom](http://openclassroom.stanford.edu/MainFolder/HomePage.php):

 - Watch the videos offline when you have no internet coneection.
 
 - Download a player such as [VLC](http://www.videolan.org/vlc/) and watch the videos with varying playback speeds.

----------


Installation
-------------
Based on python 3.5, pull requests for generalization are welcome :)
 1. Git Checkout
 2. cd the project folder
 3. Install the project requirements with `pip install -r requirements.txt`
 4. Use the tool as described in the Usage section.

Usage
-------------

Just run this is the command line `python3.5 downloader.py`

The full list will be printed in that format:

    ##############################
    Possible course selections are: (course ID or the course name)
    0. Compilers
    1. Crypto
    2. DeepLearning
    3. DiscreteProbability
    4. HCI
    5. HCIPresentations
    etc...
    ##############################

Just hit your selection id and watch the videos added to `<CourseName>` folder. Enjoy!