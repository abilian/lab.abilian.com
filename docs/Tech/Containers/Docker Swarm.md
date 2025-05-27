Docker Swarm is a container orchestration tool built and managed by Docker, Inc. It provides native clustering functionality for Docker containers, which turns a group of Docker engines into a single, virtual Docker engine.

In a Swarm, multiple Docker hosts form a self-organizing, self-healing cluster, meaning the containers can be managed across different servers. Docker Swarm allows IT administrators and developers to establish and manage a cluster of Docker nodes as a single virtual system.

The main features of Docker Swarm include:

1.  **Cluster Management:** Docker Swarm provides an integrated process for cluster management. The swarm manager nodes can manage the resources of worker nodes, which in turn run swarm services.

2.  **Scaling:** Docker Swarm allows services to be scaled up or down in response to a service's requirements, facilitating improved availability and reliability.

3.  **Load Balancing:** Swarm nodes can perform load balancing of services using ingress load balancing and DNS.

4.  **Service Discovery:** Swarm managers can automatically assign a DNS name to each service in the swarm, making it easier to perform inter-service networking.

5.  **Security:** Docker Swarm uses mutual Transport Layer Security (TLS) for authentication, authorization, and end-to-end encryption to ensure communication between the nodes in the swarm is secure.

6.  **Rolling Updates:** Docker Swarm allows incremental updates to be performed across the entire fleet of services, minimizing the risk and impact of application updates.

## Managing a Docker Swarm

You can get the status of a Docker Swarm using several `docker` CLI commands, primarily executed from a **manager node**.

Here are the most common ones:

### `docker node ls`

This is the primary command to see the status of all nodes in the swarm.

*   **Output shows:**
    *   `ID`: The unique ID of the node.
    *   `HOSTNAME`: The hostname of the node.
    *   `STATUS`:
        *   `Ready`: The node is healthy and can accept tasks.
        *   `Down`: The node is unhealthy or unreachable.
        *   `Unknown`: The manager has lost contact with the node.
    *   `AVAILABILITY`:
        *   `Active`: The node can receive new tasks.
        *   `Pause`: The node will not receive new tasks, but existing tasks continue to run.
        *   `Drain`: The node will not receive new tasks, and existing tasks are stopped and rescheduled on other active nodes.
    *   `MANAGER STATUS`:
        *   `Leader`: This is the primary manager node.
        *   `Reachable`: This is a manager node that is part of the Raft consensus quorum and can become a leader if the current leader fails.
        *   `<blank>`: This is a worker node.
    *   `ENGINE VERSION`: The Docker Engine version running on the node.


```
docker node ls
```

Example output:

```
ID                            HOSTNAME        STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
x7y2z...q5r6t*                manager1        Ready     Active         Leader           20.10.7
a1b2c...g7h8i                 worker1         Ready     Active                          20.10.7
k9l0m...o5p6q                 worker2         Down      Active                          20.10.5
```

*(The `*` indicates the node you are currently connected to.)*

### `docker service ls`

To see the status of services running on the swarm.

*   **Output shows:**
    *   `ID`: The unique ID of the service.
    *   `NAME`: The name of the service.
    *   `MODE`: `replicated` (a specified number of tasks) or `global` (one task per node).
    *   `REPLICAS`: The desired number of tasks vs. the actual number of running tasks (e.g., `3/3`).
    *   `IMAGE`: The Docker image used by the service.
    *   `PORTS`: Any published ports.

```
docker service ls
```

Example output:

```
ID                  NAME            MODE                REPLICAS            IMAGE               PORTS
a1b2c3d4e5f6        my_web_app      replicated          3/3                 nginx:latest        *:80->80/tcp
g7h8i9j0k1l2        my_api          replicated          0/2                 myuser/myapi:v1.2
```

(Here, `my_api` has an issue as 0 out of 2 desired replicas are running).

### `docker service ps <service_name_or_id>`

To get detailed status of the tasks for a specific service. This is useful for troubleshooting why a service might not have the desired number of replicas.

*   **Output shows:**
    *   `ID`: Task ID.
    *   `NAME`: Task name (e.g., `service_name.replica_number`).
    *   `IMAGE`: Image used.
    *   `NODE`: Node the task is (or was) running on.
    *   `DESIRED STATE`: The state the scheduler wants the task to be in (e.g., `Running`).
    *   `CURRENT STATE`: The actual state of the task (e.g., `Running`, `Shutdown`, `Failed`, `Pending`).
    *   `ERROR`: Any error message if the task failed.
    *   `PORTS`: Published ports.

```
docker service ps my_web_app
```

Example output:

```
ID                  NAME                IMAGE               NODE            DESIRED STATE       CURRENT STATE           ERROR               PORTS
r2q7...             my_web_app.1        nginx:latest        worker1         Running             Running 2 minutes ago
p5o9...             my_web_app.2        nginx:latest        manager1        Running             Running 2 minutes ago
t4n8...             my_web_app.3        nginx:latest        worker1         Running             Running 2 minutes ago
```

### `docker info`

Provides general information about the Docker installation, including swarm status if the node is part of a swarm.

*   Look for the `Swarm:` section.
*   **Output shows:**
    *   `Swarm: active` (or `inactive`)
    *   `NodeID`: ID of the current node.
    *   `Is Manager: true` (or `false`)
    *   `ClusterID`: ID of the swarm.
    *   `Managers`: Number of manager nodes.
    *   `Nodes`: Total number of nodes in the swarm.
    *   `Default Address Pool`: Default subnet for overlay networks.
    *   `SubnetSize`: Subnet mask size.
    *   `Data Path Port`: Port for VXLAN data path.
    *   `Orchestration`: Details about task history.
    *   `Raft`: Raft consensus status (if manager).
    *   `Manager Addresses`: List of manager IPs.

```
docker info
```

Relevant section from example output:

```
...
Swarm: active
 NodeID: x7y2z...q5r6t
 Is Manager: true
 ClusterID: abc123def456
 Managers: 1
 Nodes: 3
 Default Address Pool: 10.0.0.0/8
 SubnetSize: 24
 Data Path Port: 4789
 Orchestration:
  Task History Retention Limit: 5
 Raft:
  Snapshot Interval: 10000
  Number of Old Snapshots to Retain: 0
  Heartbeat Tick: 1
  Election Tick: 10
 Dispatcher:
  Heartbeat Period: 5 seconds
 CA Configuration:
  Expiry Duration: 3 months
  Force Rotate: 0
  External CAs:
   None
 Autolock Managers: false
 Root Rotation In Progress: false
 Node Address: 192.168.65.3
 Manager Addresses:
  192.168.65.3:2377
...
```

### `docker node inspect <node_id_or_hostname>`

To get detailed low-level information about a specific node in JSON format.

```
docker node inspect self  # Inspect the current node
docker node inspect worker1 # Inspect a node named 'worker1'
```

### Summary of what to look for

*   **Node Health:** `docker node ls` - ensure all nodes are `Ready` and `Active` (unless intentionally `Drained` or `Paused`). Pay attention to `MANAGER STATUS` for quorum.
*   **Service Health:** `docker service ls` - check if `REPLICAS` shows `desired/actual` (e.g., `3/3`). If not, investigate further.
*   **Task Health:** `docker service ps <service_name>` - check `CURRENT STATE` and `ERROR` for failing tasks. This often points to application issues, resource limits, or image problems.


<!-- Keywords -->
#docker
<!-- /Keywords -->
