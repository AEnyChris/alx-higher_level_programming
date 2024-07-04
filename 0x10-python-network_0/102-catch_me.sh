#!/bin/bash
# Handles redirect from page 1 to 3
curl -sX PUT -d "user_id=98" -H "Origin:School" 0.0.0.0:5000/catch_me_3
