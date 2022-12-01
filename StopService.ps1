Param(
    [string]$Name
)

If ( $Name -eq '')
{
    Write-Error "Name not given"
}
Else 
{
    kubectl delete deployment $Name-deploy

    kubectl delete service $Name-service
}