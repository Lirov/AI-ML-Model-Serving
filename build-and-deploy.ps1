Write-Host "Building Docker image..." -ForegroundColor Green
docker build -t ml-inference:0.1.0 .

if ($LASTEXITCODE -ne 0) {
    Write-Host "Docker build failed!" -ForegroundColor Red
    Read-Host "Press Enter to continue"
    exit 1
}

Write-Host "Docker build successful!" -ForegroundColor Green
Write-Host ""
Write-Host "Loading image to Minikube..." -ForegroundColor Green
minikube image load ml-inference:0.1.0

if ($LASTEXITCODE -ne 0) {
    Write-Host "Minikube image load failed! Make sure minikube is running." -ForegroundColor Red
    Read-Host "Press Enter to continue"
    exit 1
}

Write-Host "Image loaded to Minikube successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Applying Kubernetes deployment..." -ForegroundColor Green
kubectl apply -f k8s/deployment.yaml

if ($LASTEXITCODE -ne 0) {
    Write-Host "Kubernetes deployment failed!" -ForegroundColor Red
    Read-Host "Press Enter to continue"
    exit 1
}

Write-Host "Deployment applied successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Checking pod status..." -ForegroundColor Green
kubectl -n ml-inference get pods

Write-Host ""
Write-Host "Done! You can monitor with: kubectl -n ml-inference get pods -w" -ForegroundColor Cyan
Read-Host "Press Enter to continue"
