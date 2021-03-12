from kubernetes import client, config

config.load_kube_config()

# There are many differents apis with different use, thats why there are different apis in here
v1 = client.CoreV1Api()
v2 = client.ExtensionsV1beta1Api()
v3 = client.AppsV1Api()

# Get all pods
print("Listing pods with their IPs:")
pod = v1.list_namespaced_pod("dev-ngp")
for i in pod.items:
    print(i.metadata.name, i.status.pod_ip, i.metadata.namespace)

# Get all deployments
print("LISTING DEPLOYMENTS")
deployments = v3.list_namespaced_deployment("dev-ngp")
for i in deployments.items:
    print(i.metadata.name, i.status.ready_replicas, i.status.available_replicas,)

# Get all services
print("LISTING SERVICES")
services = v1.list_namespaced_service("dev-ngp")
for i in services.items:
    print(i.metadata.name)

# Get all ingresses
print("LISTING INGRESSES")
services = v2.list_namespaced_ingress("dev-ngp")
for i in services.items:
    print(i.metadata.name)
