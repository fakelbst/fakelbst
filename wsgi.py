#!/usr/bin/env python

import os
import fakelbst
from flask import Flask

application = app = fakelbst.app

if __name__ == '__main__':
    app.run(debug=True)
