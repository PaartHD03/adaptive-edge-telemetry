# Adaptive Inference Telemetry (AIT)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23265227.svg)](https://doi.org/10.5281/zenodo.23265227)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Runtime: ONNX](https://img.shields.io/badge/runtime-ONNX-orange.svg)](https://onnxruntime.ai/)

> Official codebase and benchmark suite for the paper:  
> **"Adaptive Inference Telemetry: A Cascaded Edge-to-Cloud Dynamic Routing Architecture for Constrained Industrial IoT Telemetry"**  
> *Author: Paarth Parag Doshi* | **DOI:** [10.5281/zenodo.23265227](https://doi.org/10.5281/zenodo.23265227)

---

## 📌 Executive Summary
Industrial IoT (IIoT) architectures struggle with a fundamental operational tension:
1. **Edge-Only Inference:** Fast and zero API egress, but vulnerable to out-of-distribution (OOD) sensor drift and high-dimensional anomalies.
2. **Continuous Cloud Offloading:** Maximum precision, but incurs severe network latency (>450ms), uplink saturation, and unsustainable API unit costs.

**Adaptive Inference Telemetry (AIT)** implements a deterministic two-tier decision cascade. High-frequency telemetry packets are evaluated locally via an INT8-quantized classifier on an ONNX runtime. Packets with prediction confidence below an entropy decision threshold ($\tau$) are compressed and conditionally routed to upstream cloud endpoints for secondary validation.

```text
       [High-Frequency Sensor Telemetry Stream]
                          │
                          ▼
            [Normalization & Feature Vector]
                          │
                          ▼
        [Tier-1: INT8 ONNX Local Edge Engine]
                          │
         ┌────────────────┴────────────────┐
         │                                 │
Confidence ≥ τ                     Confidence < τ
         │                                 │
         ▼                                 ▼
 [Edge Local Dispatch]           [Compressed JSON/Binary Payload]
  • 14.8 ms latency                        │
  • $0.00 cloud egress                     ▼ (MQTT / TLS)
                          [Tier-2: Cloud Diagnostic Endpoint]
                           • Deep secondary verification
                           • F1-Score: 0.982 Pareto recovery
