@echo off
setlocal

echo Building Hugo site...
hugo --cleanDestinationDir
if %errorlevel% neq 0 (
    echo Hugo build failed!
    exit /b %errorlevel%
)

echo Syncing to S3...
aws s3 sync public/ s3://awsinsiders.com/ --delete
if %errorlevel% neq 0 (
    echo S3 sync failed!
    exit /b %errorlevel%
)

echo Re-uploading CSS with correct headers...
aws s3 cp public/assets/css/stylesheet.36819bea596090d8b48cf10d9831382996197aa7e4fc86f792f7c08c9ca4d23b.css s3://awsinsiders.com/assets/css/ --content-type "text/css" --cache-control "max-age=31536000"
if %errorlevel% neq 0 (
    echo CSS re-upload failed!
    exit /b %errorlevel%
)

echo Invalidating CloudFront cache...
aws cloudfront create-invalidation --distribution-id E1MKTY726JN9P --paths "/*"
if %errorlevel% neq 0 (
    echo CloudFront invalidation failed!
    exit /b %errorlevel%
)

echo Deployment complete! Open https://awsinsiders.com in incognito to verify.
endlocal
pause
