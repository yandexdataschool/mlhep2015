#!/bin/bash
ln -s /REP_howto /work/REP_howto
ipython notebook --port=8888 --ip="*" /work
