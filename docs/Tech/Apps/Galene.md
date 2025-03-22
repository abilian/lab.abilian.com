#public

Galène is a videoconferencing server that is easy to deploy (just copy a few files and run the binary) and that requires moderate server resources. It was originally designed for lectures and conferences (where a single speaker streams audio and video to hundreds or thousands of users), but later evolved to be useful for student practicals (where users are divided into many small groups), and meetings (where a few dozen users interact with each other).

## Docker

https://github.com/deburau/galene-docker

## Alt UI

https://github.com/garage44/pyrite

## Galene vs. Livekit


**Key Differences and Comparison**

| Feature          | Galene                                       | LiveKit                                     |
|-------------------|----------------------------------------------|---------------------------------------------|
| **Primary Focus** | Simple, self-hosted video conferencing        | Scalable, production-grade, real-time communication platform |
| **Architecture** | Single-server (with optional TURN)             | Distributed, multi-node architecture        |
| **Scalability**  | Limited (single server)                         | Highly scalable (designed for many rooms/participants) |
| **Complexity**   | Lower (simpler codebase)                      | Higher (more features, more complex)      |
| **Features**      | - Basic video conferencing (audio, video, screen sharing)- Basic text chat- Group management- Recording- Token-based authentication | - All of Galene's features, plus:- Advanced bandwidth estimation (BWE)- Simulcast (multiple quality levels)- Scalable Forwarding Unit (SFU) model- Dynamic forwarding and quality adjustments- Load balancing and routing- Egress (recording, streaming) services- Ingress (pre-encoding) services- TURN server integration- Webhook events- Extensive SDK support (many languages/platforms)- Client-side adaptive streaming- Advanced server-side configuration options- Prometheus metrics- Advanced logging. |
| **Dependencies** | Minimal (Pion WebRTC)                            | More dependencies (Redis, routing services, etc.) |
| **Deployment**   | Easy, single-server setup                         | More complex, requires infrastructure setup (e.g., Redis) |
| **Target User**  | Individuals, small teams, self-hosting enthusiasts | Developers building production applications, businesses |
| **Licensing**    | MIT License | Apache License 2.0|

**Code-Level Observations**

1.  **Signal Handling (Galene's `main.go`, `rtpconn/rtpconn.go` vs. LiveKit's `service/signal.go`):**

    *   **Galene:** Uses a custom WebSocket-based signaling protocol. Signal messages are plain JSON.  The code directly handles offer/answer and ICE candidate exchange.
    *   **LiveKit:** Uses a dedicated `SignalServer` and `SignalClient` with Protocol Buffers (protobuf) for structured messaging. Leverages PSRPC for internal communication. This makes message definitions explicit, versioned, and easier to manage in a distributed system.

2.  **RTP Handling (Galene's `rtpconn/rtpconn.go` vs. LiveKit's `sfu` package):**

    *   **Galene:** Uses a simpler approach for handling RTP packets.  It has some basic jitter buffer management, but less sophisticated packet reordering/loss handling.
    *   **LiveKit:** Has a much more robust `sfu` package with:
        *   `DownTrack`: Manages sending RTP to a subscriber, including quality adjustments, bandwidth estimation, and keyframe requests.
        *   `Buffer`: Sophisticated buffering, reordering, and NACK handling for incoming RTP packets.
        *   `RTPMunger`:  Handles sequence number and timestamp adjustments needed for forwarding, codec parameters, and other RTP-related operations.
        *   `StreamTracker`: Manages the availability of streams (for simulcast/SVC).

3.  **Bandwidth Estimation (BWE) (LiveKit's `sfu/bwe`):**

    *   **Galene:** Doesn't implement advanced BWE.
    *   **LiveKit:** Uses a combination of sender-side and receiver-side BWE, including:
        *   REMB (Receiver Estimated Maximum Bitrate) processing.
        *   Transport-Wide Congestion Control (TWCC) feedback handling.
        *   Custom congestion control logic based on packet loss, jitter, and RTT.
        *   Support for probing to find available bandwidth.

4.  **Media Processing (Galene's `codecs` package vs. LiveKit's `sfu`, `buffer`, and codec-specific packages):**

    *   **Galene:** Basic codec support is present in `codecs`.
    *   **LiveKit:** More extensive codec support (VP8, VP9, H.264, AV1, Opus, etc.). Has dedicated code for handling codec-specific features (like VP8/VP9/AV1 keyframe detection, H.264 NALU handling).

5.  **Data Channels (Galene's `rtpconn` vs. LiveKit's `sfu/datachannel`):**

    *   **Galene:** Has some basic data channel handling.
    *   **LiveKit:** Uses a dedicated `datachannel` package, with rate limiting and buffer management, showing more focus on reliability and scalability for data channels.

6.  **Scalability (Galene's single server vs. LiveKit's routing/multi-node):**

    *   **Galene:** All logic seems designed for a single instance.
    *   **LiveKit:**  The `routing` package, `LocalRouter`, and `RedisRouter` clearly show a design for distributing load across multiple nodes. The room allocation and node selection strategies are crucial for scaling.

7. **Telemetry and Monitoring (LiveKit's `telemetry` and `prometheus` packages):**

    *   **Galene:** Limited built-in telemetry.
    *   **LiveKit:**  Comprehensive metrics collection and reporting with Prometheus, analytics events, and structured logging.

8. **Configuration:**
    *   **Galene:** Simpler configuration model.
    *   **LiveKit:** Uses a more complex configuration system (likely YAML-based) for tuning various aspects of the system, reflecting the larger number of features and settings.

9. **Extensibility**
    *   **Galene:** There is no interface for user, and all permissions are hardcoded.
    *   **LiveKit:** Provides a flexible model for permissions.

**In Summary**

The provided code highlights the fundamental difference in scope and design goals:

*   **Galene** prioritizes simplicity and ease of deployment for small-scale video conferencing. It's likely more approachable for individual developers or small projects.

*   **LiveKit** is a much more comprehensive platform aimed at building scalable, production-ready, real-time communication applications. It includes all the necessary components for managing large numbers of rooms and participants, optimizing media quality, and handling network conditions.

LiveKit's codebase is clearly more complex due to its broader feature set and distributed nature.  The choice between them depends entirely on the project's requirements.  If you need scalability, advanced features, and production-readiness, LiveKit is the clear choice. If you need something simple and easy to self-host for a small group, Galene is a viable option.




<!-- Keywords -->
#docker
<!-- /Keywords -->
