# Skillshare video + german subtitles downloader in python

### Support your content creators, do NOT use this for piracy!

You will need a skillshare premium account to access premium content.
This script will not handle login for you.

### Requirements:
Install Python-slugify and add it to PATH

### Instructions:

1. Log-in to skillshare in your browser.
2. Download "CookieManager - Cookie Editor" extension: https://chrome.google.com/webstore/detail/cookiemanager-cookie-edit/hdhngoamekjhmnpenphenpaiindoinpo
3. Go to skillshare course you want to download.
4. Open CookieManager extension.
5. Search for PHPSESSID and copy it.
6. Open cmd and navigate to skillshare-downloader-master\code folder.
7. Write example.py
8. Paste PHPSESSID you copied ealier.
9. Copy last numbers from course url.
e.g.: https://www.skillshare.com/classes/Art-Fundamentals-in-One-Hour/189505397 || Copy: 189505397
10. Wait for it to finish.
11. Downloaded course is in "skillshare-downloader-master\code\data" folder.
12. Enjoy!

#### Example:
(In cmd)
```
example.py

PHPSESSID=779286ffc5a65d33c137acdeaaef7d41

Course id:189505397
```
