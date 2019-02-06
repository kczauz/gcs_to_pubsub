from google.cloud import pubsub_v1
from google.cloud import storage

PROJECT = 'REPLACE_WITH_PROJECT_NAME'
PUBSUB_TOPIC = 'REPLACE_WITH_PUBSUB_TOPIC_NAME'

def gcs_to_pubsub(data, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This function reads a file from a gcs bucket and sends to a pub/sub sink
    Args:
        data (dict): The Cloud Functions event payload.
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """

    if data['name'].endswith('json') :
        pubsub = pubsub_v1.PublisherClient()
        topic_path = pubsub.topic_path(PROJECT, PUBSUB_TOPIC)

        print('Sending content of gs://{0}/{1} to {2}'.format(
                data['bucket'], data['name'], topic_path))

        client = storage.Client()
        bucket = client.get_bucket(data['bucket'])

        billing_data = str(bucket.get_blob(data['name']).download_as_string()).encode('utf-8')
        pubsub.publish(topic_path, data=billing_data)

    else:
        print('This file gs://{0}/{1} is not json, not publishing'.format(
                data['bucket'], data['name'], topic_path))
