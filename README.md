reGeorg
=========
Fork of regeorg to include support for python2 and python3 and to have
proper socks4 and socks5 support.


```                    _____
  _____   ______  __|___  |__  ______  _____  _____   ______
 |     | |   ___||   ___|    ||   ___|/     \|     | |   ___|
 |     \ |   ___||   |  |    ||   ___||     ||     \ |   |  |
 |__|\__\|______||______|  __||______|\_____/|__|\__\|______|
                    |_____|
                    ... every office needs a tool like Georg
```

Installation
----

You can install it via pip:
```
pip install regeorg
```

## Quick usage

```
reGeorgSocksProxy.py -p 1080 -u http://upload.sensepost.net:8080/tunnel/tunnel.jsp
```


Dependencies
-----------

reGeorg works with both Python 2.7 and Python 3.x and the following modules:

* [urllib3] - HTTP library with thread-safe connection pooling, file post, and more.


Usage
--------------

```
usage: reGeorgSocksProxy.py [-h] [-c] [-l] [-p] [-r] [-s] -u  [-v]

Socks server for reGeorg HTTP(s) tunneller

optional arguments:
  -h, --help           show this help message and exit
  -c , --creds         Credentials for basic authentication as user:pass
  -l , --listen-on     The default listening socks address
  -p , --listen-port   The default listening socks port
  -r , --read-buff     Local read buffer, max data to be sent per POST
  -s , --ssl           check TLS/SSL certificate
  -u , --url           The url containing the tunnel script
  -v , --verbose       Verbose output[INFO|DEBUG]
```

* **Step 1.**
Upload tunnel.(aspx|ashx|jsp|php) to a webserver (How you do that is up to
you)

* **Step 2.**
Configure you tools to use a socks proxy, use the ip address and port you
specified when
you started the reGeorgSocksProxy.py

** Note, if you tools, such as NMap doesn't support socks proxies, use
[proxychains] (see wiki) 

* **Step 3.** Hack the planet :)


Example
---------
```
$ python reGeorgSocksProxy.py -p 8080 -u http://upload.sensepost.net:8080/tunnel/tunnel.jsp
```

License
----

MIT


##  More agents/tunnels

List of tunnels / agent compatible with this release

- ReGeorGo - regeorg in Go: https://github.com/kost/regeorgo

- original regeorg tunnels : https://github.com/sensepost/regeorg


# References

References to original tool, similar tools and forks

- original regeorg: https://github.com/sensepost/regeorg

- Refactored regeorg (not compatible with this): https://github.com/L-codes/Neo-reGeorg

- pivotnacci - tool inspired by the reGeorg: https://github.com/blackarrowsec/pivotnacci

# Credits

This fork is maintained by [@k0st](http://twitter.com/k0st).

Original by:

- [@\_w\_m\_\_](http://twitter.com/_w_m__)

- [@trowalts](http://twitter.com/trowalts)

- [@kamp_staaldraad](http://twitter.com/kamp_staaldraad)

Tools:

- [urllib3](https://pypi.python.org/pypi/urllib3)

- [proxychains](http://sourceforge.net/projects/proxychains/)

