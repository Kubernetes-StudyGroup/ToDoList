# kubernetesManifest

## Jenny's step
1. Create a `k8s-study-group` namespace
    ```shell
    kubectl create namespace k8s-study-group
    ```
2. Apply secret yaml & configmap yaml
    ```shell
    kubectl apply -f todo-secret.yaml
    kubectl apply -f todo-mysql-init-configmap.yaml
    ```
3. Apply mysql statefulset yaml
    ```shell
    kubectl apply -f todo-mysql-statefulset.yaml
    ```
4. Apply todo server yaml
    ```shell
    kubectl apply -f todo-deployment.yaml
    ```
5.  Port forwarding
    ```shell
    kubectl port-forward service/todo-server-svc 8080:8080 --namespace=k8s-study-group
    ```
8. Go to http://127.0.0.1:8080/?user_id=2
