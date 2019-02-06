#!/usr/bin/env python3

import main

if __name__ == "__main__":
    data = {}; context = {}
    data['bucket'] = 'my_test_bucket'
    data['name'] = 'test_file.json'
    main.gcs_to_pubsub(data, context)
