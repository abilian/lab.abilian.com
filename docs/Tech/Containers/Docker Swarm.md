Docker Swarm is a container orchestration tool built and managed by Docker, Inc. It provides native clustering functionality for Docker containers, which turns a group of Docker engines into a single, virtual Docker engine.

In a Swarm, multiple Docker hosts form a self-organizing, self-healing cluster, meaning the containers can be managed across different servers. Docker Swarm allows IT administrators and developers to establish and manage a cluster of Docker nodes as a single virtual system.

The main features of Docker Swarm include:

1.  **Cluster Management:** Docker Swarm provides an integrated process for cluster management. The swarm manager nodes can manage the resources of worker nodes, which in turn run swarm services.
    
2.  **Scaling:** Docker Swarm allows services to be scaled up or down in response to a service's requirements, facilitating improved availability and reliability.
    
3.  **Load Balancing:** Swarm nodes can perform load balancing of services using ingress load balancing and DNS.
    
4.  **Service Discovery:** Swarm managers can automatically assign a DNS name to each service in the swarm, making it easier to perform inter-service networking.
    
5.  **Security:** Docker Swarm uses mutual Transport Layer Security (TLS) for authentication, authorization, and end-to-end encryption to ensure communication between the nodes in the swarm is secure.
    
6.  **Rolling Updates:** Docker Swarm allows incremental updates to be performed across the entire fleet of services, minimizing the risk and impact of application updates.

<!-- Keywords -->
#docker #swarm
<!-- /Keywords -->
