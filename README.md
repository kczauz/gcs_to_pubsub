# gcs_to_pubsub
A simple Google Cloud Function to read a file from a Google Storage bucket and publish it to a Pub/Sub topic

Example deployment:
```
gcloud functions deploy gcs_to_pubsub --runtime python37 --trigger-resource gs://my_test_bucket --trigger-event google.storage.object.finalize
```
