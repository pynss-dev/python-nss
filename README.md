python-nss is a Python binding for NSS (Network Security Services) and
NSPR (Netscape Portable Runtime). NSS provides cryptography services
supporting SSL, TLS, PKI, PKIX, X509, PKCS*, etc. NSS is an
alternative to OpenSSL and used extensively by major software
projects. NSS is FIPS-140 certified.

NSS is built upon NSPR because NSPR provides an abstraction of common
operating system services, particularly in the areas of networking and
process management. Python also provides an abstraction of common
operating system services but because NSS and NSPR are tightly bound
python-nss exposes elements of NSPR.

More information on python-nss can be found on the
`python-nss project page <http://www.mozilla.org/projects/security/pki/python-nss>`_

For information on NSS and NSPR, see the following:

* Network Security Services. `NSS project page <http://www.mozilla.org/projects/security/pki/nss/>`_.
* Netscape Portable Runtime. `NSPR project page <http://www.mozilla.org/projects/nspr/>`_.

To build python-nss you the C language header files and libraries for
both NSPR and NSS will need to be installed. This is system and
distribution specific, as such we cannot give you explicit
instructions. On Linux typically these packages are called:

* nss-devel
* nspr-devel

Use your system package manger to install them, for example on Fedora:

```
sudo yum install nss-devel nspr-devel
```

After all packages are installed, then:

```
python setup.py build
sudo python setup.py install
```

To generate the API documentation:

```
python setup.py build_doc
```
