#!/bin/bash
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS
# Sukbong Kwon (Galois)

port=9008

[ -f path.sh ] && . ./path.sh
. ./scripts/parse_options.sh || exit 1;

streamlit run app.py --server.port ${port}
