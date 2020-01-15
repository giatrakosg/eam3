#!/usr/bin/env bash

markdown-pdf README.md
zip sdi150041_db.zip ./api/oasa.db
git archive --format zip --output ./sdi150041_src.zip master
zip sdi150041.zip sdi150041_db.zip sdi150041_src.zip
