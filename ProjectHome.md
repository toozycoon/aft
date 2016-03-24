

&lt;Strong&gt;

<font color='red'>WARNING</font>: The application is an work in progress so please log any bugs [here](https://code.google.com/p/aft/issues/list). Also, feel free to mail any suggestions or requests my email is given in the sidebar

Unknown end tag for &lt;/strong&gt;



Android Forensic Toolkit allows you to extract SMS records, call history, photos, browsing history, and password from an Android phone. It currently uses adb to pull the databases and photos from the phone and the rest of the processes are performed by python.

## Announcements ##
Nothing for now, but keep checking this space.

## Forensic Artefacts ##
| **Artefact** | **Status** | **Remarks** |
|:-------------|:-----------|:------------|
| Accounts     | <font color='green'>Implemented</font>| Passwords are available as plaintext only till Android version 2.3, current versions have hashed passwords|
| Browsing History | <font color='green'>Implemented</font>| History only from the default browser, will add support for other browsers in later versions |
| Browser bookmarks | <font color='green'>Implemented</font>| Same as above |
| Search history | <font color='green'>Implemented</font>| Search history for searches done through Google. Will update with details of other search engines support later. |
| Browser Saved Passwords | <font color='orange'>In Progress</font>| Only supports the default browser for now |
|Call Logs     | <font color='orange'>In Progress</font>| Code will be updated by end of the day|
|SMS History   | <font color='orange'>In Progress</font>|Code will be updated by end of the day|
|Contacts      | <font color='orange'>In Progress</font>|Code will be updated by end of the day hopefully. This is a hard database to decipher. |
|Social Networks| <font color='red'>Planned</font>|Planned support for the default apps from Facebook, Twitter, Google+ and Foursquare|
|Email         | <font color='red'>Planned</font>| Initial support only for the default email client|
|Google Wallet | <font color='red'>Planned</font>| Not sure when I will be able to support this as I don't have either the Nexus S or the Nexus Galaxy. If anyone can help out with this, please contact me.|

The table will be updated with further details as and when I add a new functionality.

The databases extracted from the device will be present in the _databases_ folder and can be viewed using [SQLite Database Browser](http://sqlitebrowser.sourceforge.net/) or [SQLiteSpy](http://www.yunqa.de/delphi/doku.php/products/sqlitespy/index) (I personally prefer the SQLiteSpy as SQLite Database Browser hasn't been updated in a long time).

A detailed explanation on what each database contains will soon be available in the wiki.

## Supported Devices ##
_I don't own an Android device, so if anyone tests it please mail me the details (device, OS version, rooted or not, and whether you are running an custom or stock ROM along with the ROM details)_

| **Device** | **OS Version** | **Rooted** | **ROM Details** |
|:-----------|:---------------|:-----------|:----------------|
| Virtual Machine|2.3.3           | N/A        | N/A             |

## Bugs & Oddities ##
  * Python 2.7.2 comes with sqlite3 version 2.6.0 while Andriod 2.3.7 uses sqlite3 version 3.7.2, which causes it to return a "DatabaseError: file is encrypted or is not a database" error. Will be updating the PySqlite module and verifying whether it works as soon as I set up the new development environment.

  * Start the adb server separately (use adb start-server) before you use the script. Added code to check and start it automatically before rest of the code is executed but it doesn't seem to work.

## Acknowledgements ##
The ADB implementation is from Ryan Brady's [python-adb](https://github.com/rbrady/python-adb/) code.