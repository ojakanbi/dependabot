"""Sample Lambda handler."""
import json
import os


def handler(event, context):
    stage = os.environ.get("STAGE", "dev")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(
            {
                "message": "hello from sample-lambda",
                "stage": stage,
            }
        ),
    }
