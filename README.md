Leapy
=======
Collection of Leap Motion code in Python

To start
--------
Install dependencies
```Bash

$ pip install -r requirements.txt

```
[Set up a different Python for Leap to use](https://developer.leapmotion.com/documentation/python/devguide/Project_Setup.html). This is important if you're using Python installed from Homebrew or Macports. The current one is Python2.7.9 from Homebrew's Cellar.

To run
------
```Bash

$ python leap.py

```
This code adopts [gevent](http://www.gevent.org/ "gevent") instead of threading with *Listener* class from Leap APIs.



