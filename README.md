# Adaptive Inference Telemetry Pipeline

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.placeholder.svg)](https://zenodo.org)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

An end-to-end framework demonstrating dynamic model routing for Industrial IoT edge gateways. The system processes normalized telemetry packets locally via an INT8-quantized ONNX engine, triggering cloud model fallbacks only when prediction entropy exceeds calibrated confidence thresholds ($\tau$).

## Key Features
- **INT8-Quantized Local Engine:** Runs on resource-constrained edge CPUs with sub-20ms inference latency.
- **Dynamic Threshold Routing:** Reduces cloud API unit spend by up to ~78% while preserving >0.98 F1-score.
- **Telemetry Benchmarking Suite:** Out-of-the-box benchmarking script for cost, latency, and throughput estimation.

## Architecture
[Sensor Stream] -> [INT8 ONNX Model] -> Confidence >= 0.85 -> [Log Local Action]
-> Confidence < 0.85  -> [Cloud Fallback API]
