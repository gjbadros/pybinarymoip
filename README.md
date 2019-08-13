pybinarymoip 0.0.4
==================
A simple Python library for controlling a SnapAV(tm) Binary(tm)-brand
Media-Over-IP (MOIP(tm)) device for streaming video matrix-style
and creating video walls.

On PyPi, this is all pybinarymoip


Authors
-------
Greg Badros (gjbadros on github)


Installation
------------

Get the source from github.


Example
-------
    import pybinarymoip

    bm = pybinarymoip.MoIP("192.168.0.x", "host", user", "password")
    bm.load_xml_db()


License
-------
This code is released under the MIT license.
