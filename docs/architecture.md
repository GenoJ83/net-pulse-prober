# Architecture

```mermaid
flowchart LR
    Target[Target Endpoints] --> DNS[DNS Resolver]
    DNS --> TCP[TCP Handshake]
    TCP --> Jitter[Jitter & SLA Engine]
    Jitter --> Dashboard[HTML Status Page]
```
