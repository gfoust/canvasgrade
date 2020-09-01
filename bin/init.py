#!/usr/bin/env python

import sys

import config

force = '-f' in sys.argv

if not force:
  try:
    config.get_config()
    print("You already have a config.yaml!")
    print("Use -f flag to overwrite")
    sys.exit()
  except:
    pass

config.store_config({
  "token": "Your token goes here",
  "diff_cmd": "kdiff3",
  "editor_cmd": "code",
})
