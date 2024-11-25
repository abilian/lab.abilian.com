
Monitoring the power consumption of a Linux machine is critical for optimizing resource use, maintaining energy efficiency, and supporting sustainability efforts. Below, we explore various methods and tools to measure real-time power consumption from the server's outlet, CPU, or other hardware components.

### Overview

This guide outlines methods to measure the real-time power usage of a Linux system. We’ll explore techniques using built-in hardware sensors, software tools, and external power meters to gather precise measurements of power consumption. These methods apply to servers, desktops, and laptops configured with Linux.


### Methods for Measuring Real-Time Power Usage

#### Using the `powercap` Interface and RAPL

Intel's Running Average Power Limit (RAPL) framework provides detailed power consumption metrics for CPUs, DRAM, and GPUs. This is particularly useful for modern servers equipped with Intel processors.

- **Checking Instantaneous Power Usage:**

    ```bash
    sudo cat /sys/class/powercap/intel-rapl/intel-rapl:0/energy_uj
    ```

    - The value represents energy consumption in microjoules.
    - To calculate power (in watts), take two readings over a time interval and compute:

        ```bash
        time=1
        T0=$(cat /sys/class/powercap/intel-rapl/intel-rapl:0/energy_uj)
        sleep $time
        T1=$(cat /sys/class/powercap/intel-rapl/intel-rapl:0/energy_uj)
        echo "scale=2; ($T1 - $T0) / ($time * 1e6)" | bc
        ```

- **Tool Integration:** The `turbostat` utility, included in the `linux-tools-common` package, also provides power consumption information.

    ```bash
    sudo turbostat --Summary
    ```



#### Monitoring with `lm-sensors`

`lm-sensors` provides access to voltage, temperature, and power sensors embedded in the server hardware. It is particularly effective for servers with supported ACPI or motherboard sensors.

- **Installation:**

    ```bash
    sudo apt install lm-sensors
    sudo sensors-detect
    ```

- **Usage:**

    ```bash
    sensors
    ```

    - Look for power metrics like `power1`.


#### GPU Power Monitoring

For servers equipped with discrete GPUs, power consumption can be measured using vendor-specific tools:

- **NVIDIA GPUs:** Use the `nvidia-smi` tool:

    ```bash
    nvidia-smi --query-gpu=power.draw --format=csv
    ```

- **AMD GPUs:** Use `rocm-smi`:

    ```bash
    rocm-smi --showpower
    ```



#### Using Tools Like `powertop` and `powerstat`

- **Powertop:** Provides real-time power estimates and a breakdown by process:

    ```bash
    sudo powertop
    ```

    - Offers detailed insights into power-intensive processes and suggestions for power optimization.
- **Powerstat:** Tracks and logs power consumption:

    ```bash
    sudo apt install powerstat
    powerstat -d 0 1 60
    ```

    - Customizable for intervals and sampling frequency, providing averaged and peak power data.


#### Advanced Power Profiling with External Tools

For precise and reliable power usage metrics, external power meters such as **Kill A Watt** or **intelligent PDUs** are ideal. These devices monitor real-time power draw from the power outlet, accounting for total system consumption, including inefficiencies in the power supply unit (PSU).

- **Setup:** Plug the server into the power meter, which in turn connects to the power outlet.
- **Benefits:**
    - Provides highly accurate measurements.
    - Includes variance from dynamic workloads and PSU efficiency.
- **Advanced Meters:** Some models can transmit real-time data to networked devices for logging and visualization.


### Practical Considerations

#### Factors Impacting Measurements

- **Dynamic Workloads:** CPU/GPU load fluctuations can impact readings.
- **PSU Efficiency:** Power usage from the outlet is higher than internal component consumption due to PSU inefficiencies.

#### Limitations of Software-Based Methods

Software tools rely on hardware sensors and may not account for total power usage. They are best used for profiling specific components, like CPUs or GPUs, rather than total system power.

#### External Meters for Accurate Server Monitoring

In scenarios requiring precise total consumption data (e.g., for billing or capacity planning), external meters are essential.


### Conclusion

Monitoring power consumption in Linux servers can be accomplished using various tools and methods, depending on the desired level of accuracy and the specific use case. While software-based tools like `powercap`, `lm-sensors`, and `powertop` provide quick and accessible insights, external hardware solutions are necessary for precise measurements. By leveraging these techniques, administrators can better manage energy costs, improve efficiency, and contribute to sustainable operations.
