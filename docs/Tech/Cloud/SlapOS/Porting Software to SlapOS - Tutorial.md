
Porting software to SlapOS involves adapting an application to run seamlessly within the SlapOS distributed cloud operating system. This tutorial provides a step-by-step guide to transforming your software into a reusable and scalable component of the SlapOS ecosystem. By the end of this tutorial, you will be equipped to package, deploy, and manage your application using SlapOS.

### What is SlapOS?

SlapOS is a decentralized, open-source cloud operating system designed to automate the deployment and orchestration of software across distributed infrastructure. It uses **Buildout**, a Python-based build system, to define and manage software installations, making it an ideal solution for deploying complex applications.

### Why Port Software to SlapOS?

Porting your software to SlapOS provides several advantages:

1. **Scalability**: Easily deploy your application across multiple nodes and manage instances dynamically.
2. **Repeatability**: Buildout ensures consistent software installations with pinned dependencies.
3. **Monitoring and Reliability**: SlapOS includes built-in tools for monitoring application health using Promises.
4. **Modularity**: Applications are packaged into reusable software releases, promoting component sharing and reusability.
5. **Distributed Infrastructure**: SlapOS can leverage edge computing, running applications on nodes close to where they are needed.

### Pre-requisites for This Tutorial

Before proceeding, ensure you have the following:

1. **Basic Knowledge**:
    - Familiarity with Python and [[Buildout]].
    - Understanding of basic system administration and software packaging.

1. **Development Environment**:
    - A local SlapOS node or access to a SlapOS Webrunner instance for development and testing.
    - Access to a terminal with administrative privileges.

1. **Software Requirements**:
    - The software you wish to port, including all source code and dependencies.
    - An understanding of how the software is installed and configured.

### What You Will Learn

This tutorial will guide you through:

- Understanding SlapOS architecture and workflows.
- Preparing your software for deployment in SlapOS.
- Writing Software and Instance Profiles.
- Using Promises for monitoring and reliability.
- Packaging and releasing your application for use within the SlapOS ecosystem.

With these foundations in place, let's explore the architecture of SlapOS to understand how software operates within its framework.

### About this Tutorial

This tutorial is based in part on the [official SlapOS documentaion](https://slapos.nexedi.com/).

It is currently a work in progress.

We are already aware of some formatting issues that still need to be addressed.

If you find content errors, please report them by creating issues on <https://github.com/abilian/lab.abilian.com/>.


## Understanding SlapOS Architecture

Before porting software to SlapOS, you will need to understand its architecture and how it orchestrates software deployment across distributed systems. SlapOS relies on several key concepts, which we will explore in this section.

### Overview of SlapOS Concepts

#### Master

The **SlapOS Master** is the central management node of the SlapOS ecosystem. It coordinates tasks such as:

- Assigning software instances to nodes.
- Collecting monitoring data from nodes.
- Managing requests for new services.

The Master acts as a repository for software releases and ensures that all nodes comply with the defined configurations.

#### Nodes

SlapOS **Nodes** are physical or virtual machines that host the deployed software. Each node is divided into isolated containers, called **Computer Partitions**, where individual software instances run. Nodes are managed by the SlapOS Master and periodically report their status and usage metrics.

#### Partitions

In SlapOS, a **Computer Partition** is a lightweight container within a node. It is analogous to a virtual environment where one or more software instances are deployed. Each partition is self-contained and includes:

- Isolated storage.
- Configurations specific to the deployed software.
- Services and processes required by the software instance.

The use of partitions allows efficient resource management and ensures isolation between instances running on the same node.


### Software Releases and Software Instances

#### Software Releases

A **Software Release** is a blueprint that defines how to install and configure software on a node. It consists of a **software profile** (`software.cfg`) that describes:

- Software dependencies.
- Installation steps.
- Configuration templates.

The Software Release is shared across nodes and reused to reduce installation overhead. It does not include instance-specific configurations, allowing multiple instances to use the same base software.

#### Software Instances

A **Software Instance** represents a specific deployment of a Software Release. It is created using an **instance profile** (`instance.cfg.in`) that:

- Configures parameters for the instance (e.g., port numbers, database credentials).
- Defines services and monitoring mechanisms.

Software Instances are instantiated within computer partitions and tailored to specific use cases or user requirements.


### Promises and Monitoring

#### What are Promises?

In SlapOS, **Promises** are lightweight monitoring scripts that ensure the health and reliability of software instances. Each promise performs checks on specific aspects of an instance, such as:

- Ensuring a service is running.
- Verifying that a port is accessible.
- Checking application-specific metrics.

#### Promise Workflow

1. **Sense**: The promise script collects data about the system (e.g., connectivity, response time).
2. **Test**: The script evaluates the data and determines whether the instance is functioning correctly.
3. **Anomaly Detection**: If the last few tests indicate repeated failures, the promise triggers an **anomaly**.
4. **Bang**: In response to an anomaly, SlapOS initiates corrective actions, such as restarting the instance or sending alerts to the Master.

Promises are essential for ensuring service-level agreements (SLAs) and maintaining reliability across distributed nodes.

#### Benefits of Promises

- **Automated Monitoring**: Promises run periodically without human intervention.
- **Fine-Grained Checks**: Each promise targets specific functionality, enabling detailed health checks.
- **Scalability**: Promises scale with the number of software instances without additional overhead.


## Step-by-Step Process

Porting software to SlapOS involves four main steps: preparing the software, creating the Software Profile, creating the Instance Profile, and deploying and testing. Each step ensures that the application is correctly adapted to the SlapOS environment.


### Step 1: Prepare the Software

Before creating profiles, you must prepare the software for integration into SlapOS.

#### Gather Software Dependencies

1. **Identify All Dependencies**:
    - List libraries, frameworks, and external tools required by your software.
    - Check system-level dependencies (e.g., compilers, runtime environments).
2. **Document Installation Steps**:
    - Review how the software is installed manually (e.g., using `pip`, `apt`, or custom scripts).
    - Ensure the source code is accessible and complete.

#### Analyze the Software Architecture

1. **Understand the Application Workflow**:
    - Identify the main entry points, services, and configurations.
    - Determine whether the application requires databases, file storage, or other resources.
2. **Break Down Components**:
    - Separate the application into modular components that can be reused or replaced.
    - For example, a web application may have distinct components for the web server, database, and caching system.

#### Choose a Software Entry Point

1. **Select the Primary Binary or Script**:
    - Identify the main executable or script to start the application.
    - For example, `nginx` for a web server or `python app.py` for a Python application.
2. **Prepare Configuration Templates**:
    - Extract hardcoded configurations and replace them with placeholders.
    - Use Jinja2 templates to make these configurations dynamic during instantiation.


### Step 2: Create a Software Profile

The Software Profile (`software.cfg`) defines how the software is installed and prepared for use.

#### Write a `software.cfg`

1. **Set Up Basic Structure**:

    Start with a minimal `software.cfg` file:

        ```ini
        [buildout]
        parts = app

        [app]
        recipe = hexagonit.recipe.download
        url = https://example.com/mysoftware.tar.gz
        location = ${buildout:parts-directory}/mysoftware
        ```

    This downloads and extracts the software into the appropriate directory.

1. **Add Dependencies**:

    Use existing recipes for common tasks (e.g., `slapos.cookbook:wrapper` for creating wrappers).
    Define dependencies as separate sections:

        ```ini
        [python]
        recipe = zc.recipe.egg
        eggs = flask
        ```


1. **Use Components**:

    Include components from the SlapOS repository for shared libraries or utilities.
    For example:

        ```ini
        extends =
          ../../component/python3/buildout.cfg
          ../../component/nginx/buildout.cfg
        ```


#### Define Components and Dependencies

1. **List External Dependencies**:
    - Ensure external dependencies (e.g., databases, web servers) are included in the `extends` section or defined as parts.

2. **Pin Versions**:
    - Use the `[versions]` section to pin all eggs or libraries to specific versions to ensure repeatability.

#### Test Software Installation on a Local SlapOS Node

1. **Run Buildout**:
    Test the `software.cfg` by running:

        ```bash
        slapos node software --all
        ```

2. **Verify Installation**:
    Check if all dependencies are installed and the software is in the expected directory.


### Step 3: Create an Instance Profile

The Instance Profile (`instance.cfg.in`) customizes the software for specific use cases and defines how it runs.

#### Write an `instance.cfg.in`

1. **Set Up the Base Configuration**:

    Define sections for directories and basic settings:

        ```ini
        [buildout]
        parts = directories app-config app-service

        [directories]
        recipe = slapos.cookbook:makedirectory
        var = ${buildout:directory}/var
        etc = ${buildout:directory}/etc
        ```

2. **Create Configuration Files**:

    Use Jinja2 templates to generate configuration files dynamically:

        ```ini
        [app-config]
        recipe = slapos.recipe.template:jinja2
        template = inline:
          server {
            listen {{ configuration.port }};
            server_name {{ configuration.hostname }};
          }
        rendered = ${directories:etc}/app.conf
        mode = 600
        ```

3. **Define Services**:

    Create a service wrapper to run the application:

        ```ini
        [app-service]
        recipe = slapos.cookbook:wrapper
        command-line = ${buildout:parts-directory}/mysoftware/bin/app --config=${app-config:rendered}
        wrapper-path = ${directories:etc}/run_app
        ```


#### Define Instance-Specific Parameters

1. **Use Instance Parameters**:

    Define parameters in the `[instance-parameter]` section:

        ```ini
        [instance-parameter]
        configuration.hostname = localhost
        configuration.port = 8080
        ```

2. **Expose Parameters**:

    Publish parameters for external access:

        ```ini
        [publish-connection-parameter]
        hostname = ${instance-parameter:configuration.hostname}
        port = ${instance-parameter:configuration.port}
        ```


#### Add Monitoring Using Promises

1. **Write a Promise Script**:
    Create a promise script to check application health:

        ```python
        from slapos.grid.promise.generic import GenericPromise

        class RunPromise(GenericPromise):
            def sense(self):
                self.logger.info("Checking if app is running.")
                # Implement health check logic
        ```

2. **Include the Promise**:
    Add the promise to the instance profile:

        ```ini
        [app-promise]
        recipe = slapos.cookbook:promise.plugin
        module = check_app
        output = ${directories:etc}/plugin/check_app.py
        ```



### Step 4: Deploy and Test

#### Deploy the Software Release on a SlapOS Node

1. **Run the Software Deployment**:

    ```bash
    slapos node instance --all
    ```

2. **Verify Deployment**:
    Ensure all components and services are initialized properly.

#### Test Instances for Functionality and Stability

1. **Access Published Parameters**:
    Use the published parameters to interact with the instance.
2. **Perform Functional Tests**:
    Test the application as if it were deployed in production.

#### Debug Common Issues

1. **Check Logs**:
    Review logs in the `${directories:var}` directory for errors.
2. **Resolve Dependency Conflicts**:
    Ensure all dependencies are correctly installed and pinned.
3. **Adjust Configurations**:
    Update templates and profiles based on test results.


## Adding Advanced Features

Once the basic porting of your software to SlapOS is complete, you can enhance its functionality and maintainability by incorporating advanced features. These features include the use of Jinja2 templates for configuration flexibility, implementing log rotation for better log management, and writing custom recipes for handling complex configurations.


### Using Templates with Jinja2

Jinja2 is a powerful templating engine that allows you to dynamically generate configuration files during the software instantiation process.

#### Why Use Jinja2?

- **Dynamic Configuration**: Easily adjust configuration parameters like ports, hostnames, or paths based on user-defined inputs or instance parameters.
- **Reusability**: Create reusable templates that can adapt to different deployment scenarios.
- **Readability**: Simplify configuration management with structured templates.

#### Integrating Jinja2 Templates

1. **Create a Template File**:

    Create a directory named `template` in your software folder and add a template file. For example, `app.conf.in`:

        ```jinja
        server {
            listen {{ configuration.port }};
            server_name {{ configuration.hostname }};
        }
        ```

2. **Define the Template in `instance.cfg.in`**:

    Use the `slapos.recipe.template:jinja2` recipe to process the template:

        ```ini
        [app-config]
        recipe = slapos.recipe.template:jinja2
        template = ${buildout:directory}/template/app.conf.in
        rendered = ${directories:etc}/app.conf
        mode = 600
        context =
          key configuration.hostname instance-parameter:configuration.hostname
          key configuration.port instance-parameter:configuration.port
        ```

3. **Expose Parameters**:

    Ensure `instance-parameter` includes all required inputs for the template:

        ```ini
        [instance-parameter]
        configuration.hostname = localhost
        configuration.port = 8080
        ```

4. **Verify Rendering**:

    After deployment, confirm that the rendered file (`app.conf`) is correctly generated with the expected values.


### Adding Log Rotation and Monitoring

Effective log management is essential for long-running applications. SlapOS supports log rotation using `logrotate` and automated monitoring using Promises.

#### Implement Log Rotation

1. **Add Logrotate Component**:

    Extend the `logrotate` component in `software.cfg`:

        ```ini
        extends =
          ../../component/logrotate/buildout.cfg
        ```

2. **Define Log Rotation in `instance.cfg.in`**:

    Create a section for log rotation:

        ```ini
        [logrotate]
        recipe = slapos.cookbook:logrotate
        logrotate-binary = ${logrotate:location}/usr/sbin/logrotate
        conf = ${directories:etc}/logrotate.conf
        logrotate-entries = ${directories:etc}/logrotate.d
        state-file = ${directories:var}/logrotate.status
        ```

    Add specific rules for your application's log files:

        ```ini
        [logrotate-entry]
        <= logrotate
        recipe = slapos.cookbook:logrotate.d
        name = app-logrotate
        log = ${directories:var}/app.log
        frequency = daily
        rotatep-num = 7
        notifempty = true
        create = true
        ```

3. **Deploy and Verify**:

    Ensure logs are rotated as per the defined rules.

#### Add Monitoring with Promises

1. **Write a Monitoring Promise**:

    Create a Python promise script to check application logs or functionality:

    ```python
    from slapos.grid.promise.generic import GenericPromise

    class RunPromise(GenericPromise):
        def sense(self):
            log_file = self.getConfig('log-file')
            try:
                with open(log_file, 'r') as f:
                    lines = f.readlines()
                if not lines:
                    self.logger.error("Log file is empty.")
                else:
                    self.logger.info("Log file has content.")
            except Exception as e:
                self.logger.error(f"Error reading log file: {e}")
    ```

1. **Integrate the Promise**:

    Add the promise to the `instance.cfg.in`:

        ```ini
        [log-promise]
        recipe = slapos.cookbook:promise.plugin
        module = check_log_file
        output = ${directories:etc}/plugin/check_log.py
        config-log-file = ${directories:var}/app.log
        ```


### Writing Custom Recipes for Complex Configurations

If your software requires intricate setup or configurations that cannot be handled with existing recipes, you can write a custom recipe.

#### Why Write Custom Recipes?

- To automate unique setup tasks, such as patching source code or managing unusual dependencies.
- To introduce custom logic that standard recipes cannot achieve.

#### Creating a Custom Recipe

1. **Set Up the Recipe**:

    Create a Python module in the `software` directory (e.g., `recipe.py`):

        ```python
        from slapos.recipe.librecipe import GenericBaseRecipe

        class Recipe(GenericBaseRecipe):
            def install(self):
                # Create necessary directories
                self.createDirectory(self.options['directory'])

                # Write a configuration file
                config_path = self.options['config']
                with open(config_path, 'w') as f:
                    f.write("custom configuration")

                return [config_path]
        ```

2. **Integrate the Recipe in `software.cfg`**:

    Add the custom recipe to the `parts` section:

        ```ini
        [custom-recipe]
        recipe = ${buildout:directory}/software/recipe.py
        directory = ${buildout:directory}/custom
        config = ${buildout:directory}/custom/config.conf
        ```

3. **Test the Recipe**:

    Run Buildout and verify that the recipe performs as expected.

1. **Handle Edge Cases**:

    Ensure the recipe gracefully handles missing files, incorrect parameters, or failed installations.



## Freezing and Releasing the Software

After successfully porting and testing your software in SlapOS, the final step is to freeze and release it. This ensures that the software is stable, repeatable, and ready for production. The freezing and releasing process involves pinning dependencies, verifying software integrity, and making the release available for deployment across SlapOS nodes.


### Pin Dependencies and Versions

Freezing a software release involves pinning all dependencies to specific versions. This step is crucial for repeatability and preventing unexpected changes caused by dependency updates.

#### Why Pin Dependencies?

- Ensures consistency across all installations.
- Prevents breaking changes introduced by updates to libraries or components.
- Makes debugging and maintenance easier by locking the software environment.

#### How to Pin Dependencies

1. **Use `[versions]` in `software.cfg`**:

    Add a `[versions]` section in your `software.cfg` and specify the exact versions of your dependencies:

        ```ini
        [versions]
        Flask = 2.2.0
        Jinja2 = 3.1.2
        Werkzeug = 2.2.2
        ```

2. **Generate Dependency Versions Automatically**:

    Run Buildout with the `buildout-versions` extension to generate a list of all versions used during installation:

        ```bash
        buildout buildout-versions
        ```

    Copy the generated versions into the `[versions]` section of `software.cfg`.

3. **Lock Non-Python Components**:

    For external components (e.g., system libraries or tools), ensure you reference specific versions in `extends` or `url` fields:

        ```ini
        [nginx]
        recipe = hexagonit.recipe.cmmi
        url = http://nginx.org/download/nginx-1.21.0.tar.gz
        ```


### Generate MD5 Checksums

MD5 checksums ensure the integrity of files downloaded during the Buildout process. SlapOS requires checksums for all external resources to prevent tampering or corruption.

#### Steps to Generate MD5 Checksums

1. **Download the Resource**:

    Manually download the resource referenced in your `software.cfg` (e.g., a tarball or a configuration file).

2. **Calculate the MD5 Hash**:

    Use a tool like `md5sum` to generate the checksum:

        ```bash
        md5sum mysoftware.tar.gz
        ```

    Output:

        ```plaintext
        abc123def4567890 mysoftware.tar.gz
        ```

3. **Add the MD5 Checksum to `software.cfg`**:

    Include the checksum in the relevant section:

        ```ini
        [mysoftware]
        recipe = hexagonit.recipe.download
        url = http://example.com/mysoftware.tar.gz
        md5sum = abc123def4567890
        ```

4. **Test the Build**:

    Run Buildout to verify that the checksum is correct:

        ```bash
        slapos node software --all
        ```



### Pre-Cache Software Resources in Shacache

Shacache is a distributed cache system used by SlapOS to store pre-compiled software and reduce installation times.

#### Why Pre-Cache Resources?

- Speeds up deployment by avoiding recompilation.
- Ensures all nodes use the same pre-built binaries, reducing discrepancies.

#### Steps to Pre-Cache Resources

1. **Compile the Software Locally**:

    Install the software on your local node to ensure all binaries and dependencies are built.

2. **Upload to Shacache**:

    Use the SlapOS `slapcache` tool to upload compiled files to Shacache:

        ```bash
        slapcache push /path/to/compiled/software
        ```

3. **Verify Upload**:

    Check the Shacache server to ensure the files are correctly stored and accessible.


### Publish the Software Release

Once the software is frozen, tested, and pre-cached, the final step is to publish it as a stable Software Release in SlapOS.

#### Steps to Publish

1. **Tag the Release**:

    Create a tag in your repository to mark the stable release:

        ```bash
        git tag -a v1.0.0 -m "Stable release of MySoftware v1.0.0"
        git push origin v1.0.0
        ```

2. **Update the SlapOS Catalog**:

    Add the Software Release to the SlapOS Master catalog by updating its entry:

        ```json
        {
          "url": "https://git.example.com/mysoftware.git",
          "branch": "v1.0.0",
          "title": "MySoftware",
          "description": "A software application for X."
        }
        ```

3. **Run a Final Deployment Test**:

    Deploy the Software Release on a new node to ensure it installs and runs as expected.


1. **Document the Release**:

    Provide clear documentation, including:
    - Installation instructions.
    - Configuration parameters.
    - Known issues or limitations.


## Example: Porting a Simple Web Application

In this section, we will demonstrate how to port a simple Python Flask application to SlapOS. Flask is a lightweight web framework commonly used for small-scale web applications. This example will guide you through creating a Software Release, configuring an Instance Profile, and deploying the application.


### Step 1: Prepare the Flask Application

#### Application Code

Create a simple Flask application. Save the following code in a file named `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, SlapOS!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

#### Requirements File

List the application's dependencies in a `requirements.txt` file:

```plaintext
Flask==2.2.0
```


### Step 2: Create a Software Profile

The Software Profile (`software.cfg`) will define how to install the application and its dependencies.

#### Basic Software Profile

Create a `software.cfg` file:

```ini
[buildout]
parts = python flask app-wrapper

[python]
recipe = zc.recipe.egg
eggs = setuptools
interpreter = python
```

#### Add Flask Dependency

Extend the `python` part to include Flask:

```ini
[flask]
<= python
eggs += Flask
```

#### Add Application Code

Include a part for the application:

```ini
[app]
recipe = hexagonit.recipe.download
url = https://example.com/app.py
location = ${buildout:parts-directory}/app
```

#### Create a Wrapper

Define a wrapper to run the application:

```ini
[app-wrapper]
recipe = slapos.cookbook:wrapper
command-line = ${python:executable} ${app:location}/app.py
wrapper-path = ${buildout:parts-directory}/bin/run-flask
```


### Step 3: Create an Instance Profile

The Instance Profile (`instance.cfg.in`) configures the Flask application for deployment.

#### Basic Instance Profile

Create an `instance.cfg.in` file:

```ini
[buildout]
parts = directories flask-config flask-service

[directories]
recipe = slapos.cookbook:makedirectory
var = ${buildout:directory}/var
etc = ${buildout:directory}/etc
```

#### Dynamic Configuration

Use a Jinja2 template to allow dynamic configuration of the application:

```ini
[flask-config]
recipe = slapos.recipe.template:jinja2
template = inline:
  host = {{ configuration.host }}
  port = {{ configuration.port }}
rendered = ${directories:etc}/flask.cfg
mode = 600
context =
  key configuration.host instance-parameter:configuration.host
  key configuration.port instance-parameter:configuration.port
```

#### Run the Application

Add a part to create a service wrapper for running the application:

```ini
[flask-service]
recipe = slapos.cookbook:wrapper
command-line = ${buildout:parts-directory}/bin/run-flask --config=${flask-config:rendered}
wrapper-path = ${directories:etc}/run-flask
```

#### Expose Instance Parameters

Expose configuration parameters to customize the Flask application:

```ini
[instance-parameter]
configuration.host = 0.0.0.0
configuration.port = 5000
```


### Step 4: Add Monitoring with Promises

Create a Python promise script to monitor whether the application is running.

#### Promise Script

Save the following as `check_flask.py`:

```python
from slapos.grid.promise.generic import GenericPromise
import socket

class RunPromise(GenericPromise):
    def sense(self):
        host = self.getConfig('host')
        port = int(self.getConfig('port'))
        try:
            with socket.create_connection((host, port), timeout=5):
                self.logger.info(f"Flask is running on {host}:{port}.")
        except Exception as e:
            self.logger.error(f"Error connecting to Flask: {e}")

    def anomaly(self):
        return self._anomaly(result_count=3, failure_amount=3)
```

#### Integrate the Promise

Add the promise to the `instance.cfg.in` file:

```ini
[flask-promise]
recipe = slapos.cookbook:promise.plugin
module = check_flask
output = ${directories:etc}/plugin/check_flask.py
config-host = ${instance-parameter:configuration.host}
config-port = ${instance-parameter:configuration.port}
```


### Step 5: Deploy and Test

#### Deploy the Software Release

1. Run the following command to deploy the Software Release:

    ```bash
    slapos node software --all
    ```

2. Verify that all parts are installed and available.


#### Instantiate the Flask Application

1. Deploy the instance using:

    ```bash
    slapos node instance --all
    ```

2. Verify the application is running by accessing it at the configured host and port:

    ```bash
    curl http://0.0.0.0:5000
    ```


#### Check Monitoring

1. Confirm the promise is reporting the application's health.
2. Inspect logs in the `${directories:var}` folder for any issues.


### Next Steps

- Add log rotation to manage application logs.
- Extend the application to support custom configurations or additional dependencies.
- Publish the Software Release following the steps in the "Freezing and Releasing the Software" section.


## Troubleshooting


When porting software to SlapOS, challenges can arise. This section addresses common issues, troubleshooting techniques, and best practices to ensure efficient, reusable, and modular profiles.

### Dependency Conflicts

- **Problem**: Conflicting versions of libraries or tools cause errors during installation.
- **Solution**:
    - Pin dependencies in the `[versions]` section of `software.cfg`.
    - Use specific URLs for external components to ensure consistency.
    - Test the software with the exact versions listed in the profile.

### Missing or Incorrect Configuration

- **Problem**: The application fails to start due to missing or invalid configuration files.
- **Solution**:
    - Use Jinja2 templates to dynamically generate configurations based on instance parameters.
    - Include default values for all required parameters in `instance.cfg.in`.

### Application Crashes After Deployment

- **Problem**: The application crashes or fails to start in the deployed instance.
- **Solution**:
    - Check logs in the `${directories:var}` folder for errors.
    - Verify that all necessary files and directories are created during the Buildout process.
    - Use promises to monitor the application and identify issues.

### Buildout Errors

- **Problem**: Buildout fails during the software installation or instantiation process.
- **Solution**:
    - Ensure all recipes and components are correctly defined in `software.cfg`.
    - Validate the MD5 checksums of downloaded resources.
    - Use the `--verbosity` flag with Buildout to get detailed error messages:

        ```bash
        buildout -vvvv
        ```


### Promises Failing Consistently

- **Problem**: Monitoring scripts return errors even when the application appears to be functioning.
- **Solution**:
    - Verify the promise script logic and configurations.
    - Test the promise script independently to ensure it behaves as expected.
    - Check network connectivity if the promise monitors external endpoints.


## Best Practices for Creating Reusable and Modular Profiles


### Use Atomic Components

- Break the application into smaller, reusable components.
- Store components in the `component` directory for shared usage.
- Example:
    - Separate the database, web server, and application logic into distinct components.

### Pin Versions and Dependencies

- Always pin versions for Python eggs, libraries, and external components.
- Use Buildout’s `buildout-versions` extension to generate a complete list of dependencies.

### Leverage Existing Recipes

- Use well-tested recipes from `slapos.cookbook` for common tasks like creating directories or wrappers.
- Avoid reinventing solutions for standard operations.

### Implement Promises

- Include at least one promise script to monitor the health of the application.
- Promises should provide meaningful logs for debugging and ensure service reliability.

### Use Dynamic Configuration

- Use Jinja2 templates to generate configurations dynamically based on instance parameters.
- Avoid hardcoding values that may vary between deployments.

### Document Parameters and Profiles

- Clearly document the purpose and usage of instance parameters.
- Provide comments in `software.cfg` and `instance.cfg.in` to explain sections and configurations.

### Test Locally Before Publishing

- Test the software on a local SlapOS node or Webrunner.
- Verify both the Software Release (`software.cfg`) and the Instance Profile (`instance.cfg.in`) independently.


## Conclusion

Porting software to SlapOS involves preparing the application, creating reusable profiles, and leveraging SlapOS features for scalability and reliability. This tutorial provided a structured approach to:

1. Understanding SlapOS architecture and concepts.
2. Preparing software and gathering dependencies.
3. Writing Software and Instance Profiles with dynamic configurations.
4. Adding advanced features like monitoring, log rotation, and custom recipes.
5. Freezing and releasing software for production.
6. Troubleshooting common issues and following best practices.

### Next Steps

1. **Extend Your Profiles**:

    - Add more advanced monitoring and logging.
    - Explore multi-instance deployments for scalability.

2. **Publish Your Software**:

    - Tag and release your Software Release for public or private deployment.
    - Add your release to the SlapOS catalog.

3. **Learn More**:

    - Explore the SlapOS [documentation](https://slapos.nexedi.com/).
    - Study advanced recipes and components from the SlapOS repository.

4. **Experiment with Other Applications**:

    - Apply these principles to port more complex applications like databases, web servers, or distributed systems.

## Glossary

### Anomaly

A recurring failure detected by a **Promise** in SlapOS. When multiple failures are logged over a specified number of tests, the system triggers an alert (called a "bang") to initiate corrective actions.

### Bang

An automated action triggered by SlapOS in response to anomalies detected by Promises. This action can include restarting instances, reinitializing processes, or reporting issues to the Master.

### Buildout

A Python-based build system used by SlapOS to define, install, and manage software environments. It uses configuration files (`software.cfg`, `instance.cfg.in`) to automate the setup and instantiation of applications.

### Computer Partition

A self-contained, lightweight container within a SlapOS Node. It isolates resources (e.g., storage, configurations, services) to host individual software instances securely and efficiently.

### Component

A reusable building block in SlapOS that provides a specific library, utility, or functionality. Components are stored in the `component` directory and shared across multiple software profiles.

### Instance Profile

A configuration file (`instance.cfg.in`) defining how a specific instance of software should behave. It includes instance-specific parameters, dynamic configurations, and monitoring logic.

### Jinja2

A templating engine used in SlapOS to dynamically generate configuration files based on instance parameters. It simplifies configuration management and allows customization during instantiation.

### Logrotate

A utility integrated into SlapOS to manage application logs. It rotates, compresses, and archives logs to ensure efficient storage usage and prevent overflow.

### Master

The central management system in SlapOS. It handles node orchestration, monitors software instances, and manages requests for new deployments.

### MD5 Checksum

A cryptographic hash used to verify the integrity of downloaded resources in SlapOS. Each external resource referenced in `software.cfg` must include its MD5 checksum to ensure consistency and security.

### Node

A physical or virtual machine that hosts SlapOS instances. Each node is divided into **Computer Partitions** managed by the SlapOS Master.

### Promise

A lightweight monitoring script in SlapOS. Promises ensure the reliability of software instances by checking specific metrics, such as process health or network connectivity.

### Sense-Test-Anomaly Workflow

The three-phase process used by Promises in SlapOS:

- **Sense**: Collect system data or metrics.
- **Test**: Evaluate the data to determine the health of the instance.
- **Anomaly**: Trigger corrective actions if repeated failures are detected.

### Shacache

A distributed cache system used by SlapOS to store precompiled binaries and software resources. It speeds up deployments and ensures consistency across nodes.

### SlapOS

An open-source, decentralized cloud operating system that automates the deployment and management of software across distributed infrastructure.

### Software Profile

A configuration file (`software.cfg`) defining how to install software and its dependencies in SlapOS. It provides the blueprint for creating reusable **Software Releases**.

### Software Instance

A specific deployment of a **Software Release** within a **Computer Partition**. Instances are tailored to user requirements using **Instance Profiles**.

### Software Release

A reusable, versioned package of software created using a **Software Profile**. It includes all dependencies and installation instructions but lacks instance-specific configurations.

### Wrapper

A script or executable created by SlapOS to manage the execution of software or services. Wrappers often include parameters, paths, and environmental variables specific to the instance.
