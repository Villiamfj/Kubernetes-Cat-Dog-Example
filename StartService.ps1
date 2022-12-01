Param(
        [string]$Path,
        [string]$Name
    )

If ($Path -eq '' -or $Name -eq '') 
{
    Write-Error "Both Path and Name cannot be empty cannot be empty"
} 
Else 
{
    docker build $Path --tag $Name

    kubectl apply -f $Path/deployment.yaml

    kubectl apply -f $Path/service.yaml
}

