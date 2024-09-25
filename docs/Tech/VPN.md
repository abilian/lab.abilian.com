We identified several open-source VPN solutions through technological monitoring and experience. Seven solutions were shortlisted for detailed analysis, focusing on their functional scope, implementation capabilities, maintainability, and compliance with security standards.

## Evaluation Criteria

The VPN solutions were evaluated based on:

- Functional scope: native features and extensible modules
- Implementation and maintenance capabilities
- Scalability for large-scale deployment
- Integration simplicity with client systems
- Project sustainability: governance, community size, licensing, and documentation

## Key Features Required

The key features expected from the VPN solutions include:

- Adherence to ANSSI recommendations:
  - Preventing users from altering the VPN connection means
  - Implementing a state-of-the-art IPsec VPN tunnel
  - Blocking split-tunneling and ensuring secure DNS configuration
  - Optional recommendation to block direct communication between mobile access devices
- Double-factor authentication
- Non-dependence on specific OS platforms
- Industrialization: viability, scalability, and maintainability
- Remediation phase to check and update software versions on mobile devices

## VPN Solutions Analyzed

1. **[LibreSwan](https://libreswan.org/)**
   - A community-driven IPsec VPN solution, based on IKEv1 and IKEv2 protocols.
   - Requires strong technical expertise for implementation and maintenance.
   - Limited commercial support and interoperability.

2. **[StrongSwan](https://strongswan.org/)**
   - An IPsec VPN solution with modular architecture, supporting IKEv1 and IKEv2.
   - Provides better industrialization than LibreSwan but faces similar limitations.
   - Recently acquired by Secunet, indicating potential future improvements.

3. **[OpenVPN](https://openvpn.net/)**
   - An SSL/TLS-based VPN solution known for its ease of implementation and use.
   - Supports various OS platforms with a client installation requirement.
   - Not a standard protocol and has some performance limitations.

4. **[WireGuard](https://www.wireguard.com/)**
   - A modern and efficient VPN protocol, simpler to implement than IPsec.
   - Known for high performance and security but lacks industrial features natively.
   - Can be enhanced with third-party solutions like TailScale.

5. **[SoftEther](https://www.softether.org/)**
   - A versatile multi-protocol VPN solution developed by the University of Tsukuba.
   - High performance and extensive protocol support but lacks comprehensive support and French localization.
   - Suitable for scenarios with a wide range of client OS requirements.

6. **[Pritunl](https://pritunl.com/)**
   - A multi-protocol VPN solution tailored for enterprise use, supporting OpenVPN, WireGuard, and IPsec.
   - Provides advanced features like high availability, scalability, and extensive monitoring.
