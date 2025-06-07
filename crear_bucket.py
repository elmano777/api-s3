import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    try:
        # Parse the request body
        body = json.loads(event['body'])
        bucket_name = body.get('bucket_name')
        
        if not bucket_name:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'error': 'El nombre del bucket es requerido'
                })
            }
        
        # Create S3 client
        s3_client = boto3.client('s3')
        
        # Create the bucket
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'us-east-1'
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Bucket {bucket_name} creado exitosamente'
            })
        }
        
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': f'Error al crear el bucket: {str(e)}'
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': f'Error inesperado: {str(e)}'
            })
        } 