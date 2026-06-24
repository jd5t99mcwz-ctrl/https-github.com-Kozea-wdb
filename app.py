#!/usr/bin/env python
"""
WDB Web Debugger Server
A simple web debugger application
"""

if __name__ == '__main__':
    # Start the WDB server
    import wdb.server
    wdb.server.run()
