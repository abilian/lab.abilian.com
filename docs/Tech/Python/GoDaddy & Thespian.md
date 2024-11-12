Post saved from:
https://web.archive.org/web/20160304014153/http://engineering.godaddy.com/why-godaddy-built-an-actor-system-library/

#actors #python

## Why GoDaddy Built an Actor System Library

GoDaddy had a number of challenges to solve when designing its Virtual Private Server (VPS) and Dedicated Hosting Platform. The system had to be highly scalable, capable of operating across multiple datacenters spread across the world, and support over 5,000 systems hosting tens of thousands of customers. The system had to be capable of running simultaneous operations directly on those remote systems, interact with external services, and it must be fault tolerant, adaptable, extensible, and operationally agile.

There are many different approaches to these problems, but one simple yet very powerful approach that met all the requirements is the [Actor Model](https://web.archive.org/web/20160304014153/https://en.wikipedia.org/wiki/Actor_model). The Actor Model was conceived in MIT’s Artificial Intelligence labs back in the mid 1970’s, and recently has seen renewed interest because of the way it addresses development architecture.

GoDaddy uses the [Python Language](https://web.archive.org/web/20160304014153/http://python.org/) for many of its internal systems and production applications. Evaluating the available Python Actor Libraries, we found that the existing ones were relatively simple with a focus on academic exploration and did not support key features that we needed:

- Simple and direct actor implementation
- Remote distributed execution
- Flexible implementation with debugging support
- Dynamic source code loading

GoDaddy therefore developed an Actor Library for Python called **Thespian** to support this highly-scalable architecture. GoDaddy has open-sourced the [Thespian Library](https://web.archive.org/web/20160304014153/http://github.com/godaddy/Thespian) to share it with the community for others looking to use Python Actors to deploy real, distributed, enterprise-level services. This blog talks about the Thespian Library and some of the challenges GoDaddy has overcome using it.

## Why we chose to use actors

GoDaddy Virtual and Dedicated Hosting distributed provisioning application creates Virtual Private Servers (VPS) or Dedicated Servers for customers, and provides ongoing management of those servers. The provisioning application implements the business logic of the VPS and Dedicated Hosting Platform as well as coordinating operations that run either locally or on one of the thousands of remote systems that support customer servers.

Customer requests (creating a server, rebooting a server, changing passwords, etc.) are passed to our application server through a primary REST API (via our Web-based User access control panel). The application server is responsible for handling all of these requests in parallel in order to support our thousands of customers; although the requests for a specific customer server are processed in the order they are received. The Django front-end, coupled with the MySQL database is sufficient to provide the API interface and handle any requests that simply query static information and return their results synchronously, however, longer-running requests (like rebooting a Windows Server) cannot be performed in a blocking manner by a Django gunicorn thread. In addition, many portions of these requests must be executed remotely on the host system where the customer’s server is actually running as well as interact with external services which may take varying amounts of time to complete their operation.

The distributed nature of this provisioning application brings with it two additional challenges: deployment synchronization and testing/debugging. The system must support deploying new software to 5,000+ systems without impacting ongoing customer requests and avoiding the drift problems of upgraded systems interacting with yet-to-be-updated systems. Due to its nature, a distributed system is very difficult to execute in a simple deterministic manner under external control, yet GoDaddy engineering must ensure that the system operates correctly by writing unit and functional tests, and using those tests to debug the system in our development environment.

The Actor Model provides the necessary asynchronous and distributed framework for processing distributed requests involving the customer’s servers or external services while Thespian also solves the deployment and testing problems described above.

## How Actors process our requests

Each logical step that must be performed to complete a customer request is implemented as an Actor in order to gain the advantages of concurrency and fault-tolerance provided by an Actor-based system. Every step performs its function independently of all other steps, and any failures or issues related to that step are isolated to the corresponding Actor. In each step the Actor may enlist other Actors on remote systems to run commands on those systems, or it may access external services that provide auxiliary functionality (e.g. allocating a new IP address from a pool of addresses). Failures and delays in those operations similarly affect only those Actors, and only for a single request.

The Actor Model provides the ability to run multiple different requests simultaneously by implementing concurrency at the Actor level allowing each Actor to run simultaneously with other Actors so that the system can process multiple requests at the same time. The Actor Model also allows for automatic recovery of actor failures while isolating the effects of that failure to a single Actor and a single request. This makes the system very resilient to failures.

[![the-actor-model](https://web.archive.org/web/20160304014153im_/http://engineering.godaddy.com/wp-content/uploads/2015/08/the-actor-model.jpg)](https://web.archive.org/web/20160304014153/http://engineering.godaddy.com/wp-content/uploads/2015/08/the-actor-model.jpg)

As shown in the figure above, requests are passed to the backend by creating an “action” object that corresponds to the request in the MySQL database (except ephemeral actions which have no database entry) and sends that message to the top-level Control Actor. Each action object specifies the list of step names that should be executed in order to perform the action. The Control Actor validates the action, then passes the action to each corresponding Step Actor in sequence to perform the action. Successful completion of all of the steps results in the Control Actor marking the MySQL request entry corresponding to the action with a “completed” status.

The Agency Actor acts as a singleton factory of Step Actors. The Control Actor supplies the step name (from the action) and the agency returns the Actor Address of the dynamically loaded and started Step Actor. Multiple actions of the same type can be processed in parallel for instance the first action may be at the second step (i.e. being processed by the second Step Actor) while the second action may be at the first step and being processed by the first Step Actor.  
As the figure above shows, for the reboot request there is a step to validate that the customer’s disk is not 100% full which will prevent a successful boot, followed by the reboot step itself, and then multiple steps which verify the successful restoration of network connectivity for the customer’s server.

Each Step Actor implements whatever functionality is needed to perform that step. Some steps may communicate with external services and some steps must execute commands on the remote host system. In addition to the fault tolerance described above, the Actor Model makes the overall application tolerant of delays meaning it does not matter to the other Actors how long one particular Actor takes to perform its task, and the other Actors can be busy processing other requests in the interim.

## Remote execution

When writing an Actor, it receives messages delivered to it by the Actor System within which it is running. The delivery argument specifies the message and the address of the Actor that sent the message. The messages can be anything, but the Actor Address is an opaque handle to the actor. Actors can create other Actors by making a call to the Actor System and receiving an Actor Address for the newly created Actor in return. In addition, messages can contain Actor Addresses.

When an Actor wishes to communicate with another Actor, it makes a call to send a message, specifying the message itself and the target Actor Address as the arguments. The Actor System is responsible for determining which Actor the Actor Address references and delivering that message to the recipient Actor. This makes the Actor Code itself very simple, as seen in the example below, which contains two Actors that work together to generate a response to an external query.

```python
from thespian.actors import *

class Hello(Actor):
    def receiveMessage(self, message, sender):
        if not hasattr(self, 'world'):
            self.world = self.createActor(World)
        self.send(self.world, (sender, 'Hello, '))

class World(Actor):
    def receiveMessage(self, message, sender):
        orig_sender, greeting = message
        self.send(orig_sender, greeting + "world!")
```

Because Actors reference other Actors using opaque Actor Addresses, each Actor has no real knowledge of the actual circumstances of the other Actor. The GoDaddy Thespian Library allows multiple Actor Systems running on different network nodes to communicate and cooperate in Actor management and message delivery. Thus, an Actor running on the application server can send a message to an Actor running as another process on the same system or to an Actor running on any of the other 5,000+ host systems in exactly the same manner and without being aware of where the target Actor actually exists.

As host systems are created to meet additional customer demand, our Operations Team simply installs Thespian on the newly built systems. When Thespian starts up, it connects to the Thespian Actor System running on the application server to join into the convention of Actor Systems. These systems are now immediately available to host customer servers without the Control Actor or Step Actors ever being aware that there is a new server in the system.

## Thespian Actor capabilities

The Thespian Actor System is responsible for determining whether new Actors should be created on the local system or a remote system running Thespian. This is handled by specifying a set of “capabilities” for each Actor System, based on probing the local environment. The capabilities are simply a key/value pair and can be anything that the code starting the Actor System wishes to supply.

Example Actor System startup with capability specification:

```python

from thespian.actors import *
from database import dbclass
import socket

lcladdr = socket.getaddrinfo(socket.getfqdn(), 0,
                             socket.AF_INET,
                             socket.SOCK_STREAM,
                             socket.IPPROTO_TCP, 0)

capabilities = { 'Convention Address.IPv4': '10.5.1.1:1900',
                 'System Address.IPv4': lcladdr,
               }

try:
    dbconn = dbclass.connect(...)
    if dbconn and 1 == dbconn.runquery('select 1=1'):
        capabilities['Has DB access'] = True
except DBError:
    pass

ActorSystem('multiprocTCPBase', capabilities)
```

Actor definitions can specify what capabilities that Actor requires to run successfully, either via the `actorSystemCapabilityCheck()` static method on the actor class or using the `@requireCapability` class decorator or both. When `createActor()` is called for the Actor, the current Actor System checks to see if its capabilities match the Actor’s requirements. If they do not, it will then attempt to locate another Actor System that satisfies the required capabilities and forwards the createActor operation to that remote Actor System. All of this is handled by the Actor System without requiring any code in the Actors themselves.

**Example Actor specification of its required capabilities:**

```python
from thespian.actors import *
from database import dbclass

@requireCapability('Has DB access')
@requireCapability('LDAP installed')
class DBUpdateFromLDAP(Actor):

    @staticmethod
    def actorSystemCapabilityCheck(capabilities, requirements):
        return capabilities.get('LDAP zone', None) == 'Active'

    def receiveMessage(self, message, sender):
        rows = self.db.query('select * from ...')
        ...
```

This capability-based automatic configuration mechanism also allows the overall application to adapt to individual faults. For example, if one system loses access to the database perhaps due to a mis-applied firewall rule on a network switch, the Actors on that system will exit and be re-created on any other system in the environment that still has access to the database. All other Actors continue to operate as normal without any awareness of the reconfiguration other than receiving a new Actor Address for the Actor requiring database access. In conjunction with the fault tolerant behavior provided by automatically restarting Actors, this makes the system extremely resilient and essentially self-healing.

## Dynamic source updates

As described above, our Hosting Provisioning system handles operational growth automatically, but as the overall environment grew the deployment process quickly became problematic using the conventional yum/spacewalk methodology:

- The entire environment must stop taking requests and become quiescent. The RPM update stops the Actor System and all local Actors, which would drop any actions being processed at the time.
- All 5,000+ systems must be updated, which can take some time and overload the yum servers if too many systems are updated at the same time.
- Version mismatches can still occur if some remote hosts missed the upgrade, either because they were down or just going through the build process while the new deployment was being pushed out.

To resolve this, GoDaddy enhanced Thespian to support loadable code. The Thespian Actor System itself is still deployed using yum, but Thespian is relatively stable and new deployments are infrequent so the provisioning application itself is where most of the changes occur and this code can be dynamically loaded into the currently running Thespian via an Actor System call.

The same abstraction that allows Actors to communicate without being aware of the location of other Actors allows to identical Actors from different versions to run side-by-side. A zipfile containing Python source code can be dynamically loaded into Thespian via the `loadSource()` call which verifies the load as valid by having it authorized by a Source Authority Actor, and then assigns the loaded code a hash signature. When the Django front-end passes actions to the Control Actor, it specifies the source hash id associated with the Control Actor. In this manner, the older sources can still run pre-existing actions through to completion while new actions are directed to the newly loaded source. Once the older source is no longer active it can be unloaded from the Thespian environment.

When the current Actor System does not have the necessary set of capabilities to create an Actor, then the create is deferred to a remote Actor System and the source hash is passed along with the create request. If the remote Actor System does not have the identified sources available, it will automatically retrieve them from the requesting Actor System. This allows new sources to be deployed just to the application server whereupon they will be propagated throughout the rest of the environment on-demand alleviating the need to upgrade all 5,000+ systems at the exact same time which simplifies the deployment and ensures that all systems are using the same version of the software.

## Debugging

A multi-process distributed system is very difficult to debug as setting breakpoints and stepping through code is no longer a viable option when the code is spread across multiple systems or even multiple processes. In addition, unit and functional test frameworks are usually only capable of testing, analyzing, and providing coverage information for a single-threaded application.

An actor-based design can be used to make the debugging and testing efforts considerably easier however. The abstraction of the concurrency methodology and message transport system provided by the Actor System is again the key element to enabling this simplicity.

The Thespian Actor System can be initialized with a parameter that specifies a “system base” that will be used to implement the Actor System. Using different system bases allows the ability to change the concurrency and message transport implementations within the Actor System requiring no code changes to the Actors themselves.

To simplify a large portion of the debugging process as well as enabling code coverage analysis during unit testing, a special system base is used that simply runs all Actors sequentially. Individual messages are delayed on a global queue until they can be sequentially delivered to the target Actor, and all Actors are simply run in the context of the primary test process. Actor code that requires external concurrency will still require fixtures to enable this mode of operation, but the overall system is quickly and simply reduced to a set of sequential operations that can be more easily debugged.

In addition, Thespian will soon be adding functionality similar to the “Goons” as described in the [blog post by Sam Ng about Simulating Faults](https://web.archive.org/web/20160304014153/http://engineering.godaddy.com/simulating-fault-in-cloud-scalable-services/). Allowing a Goon to proxy for an Actor is another great and easy way to test an Actor-based application and help make Thespian-based applications more robust.

## Conclusion

The Actor Model is a powerful yet simple tool for the modern software developer. The Actor Model provides a higher level of abstraction than alternative approaches which enables more focus on the application logic and doesn’t lock in a specific concurrency or transport mechanism enabling future operational flexibility. GoDaddy’s Thespian was developed to support our Hosting Provisioning System which requires an Actor Model that is scalable, fault tolerant, concurrent, modular, and extensible.

GoDaddy is excited to share this technology by open sourcing the [Thespian Library](https://web.archive.org/web/20160304014153/http://github.com/godaddy/Thespian) to Python developers. Please feel free to submit contributions, comments, feature requests, or join us in person…[we’re hiring](https://web.archive.org/web/20160304014153/http://www.godaddy.com/careers)!

<!-- Keywords -->
#actor_model #actorsystem
<!-- /Keywords -->
