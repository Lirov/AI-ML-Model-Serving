@echo off
echo Building Docker image...
docker build -t ml-inference:0.1.0 .

if %ERRORLEVEL% neq 0 (
    echo Docker build failed!
    pause
    exit /b 1
)

echo Docker build successful!
echo.
echo Loading image to Minikube...
minikube image load ml-inference:0.1.0

if %ERRORLEVEL% neq 0 (
    echo Minikube image load failed! Make sure minikube is running.
    pause
    exit /b 1
)

echo Image loaded to Minikube successfully!
echo.
echo Applying Kubernetes deployment...
kubectl apply -f k8s/deployment.yaml

if %ERRORLEVEL% neq 0 (
    echo Kubernetes deployment failed!
    pause
    exit /b 1
)

echo Deployment applied successfully!
echo.
echo Checking pod status...
kubectl -n ml-inference get pods

echo.
echo Done! You can monitor with: kubectl -n ml-inference get pods -w
pause
