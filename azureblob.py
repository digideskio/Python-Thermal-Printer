from azure.storage.blob import BlobService
import sys

name = str(sys.argv[0])
print(name)


blob_service = BlobService(account_name='rpprinter', account_key='JMak74DHgi654oBKBGEWKPaVPynUA+w0H8Po9y5gqWwt8HVyQ9NLLg8aTWzRjC3eD/t2tVsswzXVs9NUJ9WjPg==')

blob_service.create_container('printerpics', x_ms_blob_public_access='container')

blob_service.put_block_blob_from_path(
    'printerpics',
    'image.jpg',
    'image.jpg',
    x_ms_blob_content_type='image/jpg'
)

