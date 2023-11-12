from time import perf_counter

import boto3
from botocore.client import BaseClient

LOCAL_PATH: str = (
    "/Users/eliasbenaddouidrissi/Desktop/dev/repos/python-s3-threading-examples/"
)
BUCKET_NAME: str = "s3-threading-examples"


def upload_object(s3_client: BaseClient, file_name: str) -> str:
    """
    Uploads a file to an S3 bucket.

    Args:
        s3_client (BaseClient): An instance of the boto3 S3 client.
        file_name (str): The name of the file to upload.

    Returns:
        str: A message indicating that the file has been uploaded.
    """
    print(f"Uploading {file_name}")
    upload_filename = f"{LOCAL_PATH}/{file_name}"
    s3_client.upload_file(
        Filename=upload_filename, Bucket=BUCKET_NAME, Key=f"{file_name}"
    )
    return f"{file_name} uploaded"


if __name__ == "__main__":
    session = boto3.Session(profile_name="default")
    s3_client = session.client("s3")

    t1_start = perf_counter()
    keys_lst = [
        "example1.txt",
        "example2.txt",
        "example3.txt",
        "example4.txt",
        "example5.txt",
        "example6.txt",
        "example7.txt",
        "example8.txt",
        "example9.txt",
        "example10.txt",
        "example11.txt",
        "example12.txt",
        "example14.txt",
        "example14.txt",
        "example15.txt",
    ]
    for key in keys_lst:
        upload_object(s3_client, key)
    t1_stop = perf_counter()
    print("Elapsed time in seconds:", t1_stop - t1_start)
