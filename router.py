#### File 2: `router.py`
```python
"""
Adaptive Inference Telemetry - Edge Dynamic Router
Author: Paarth Parag Doshi
"""
import time
import numpy as np

class MockAdaptiveRouter:
    def __init__(self, confidence_threshold: float = 0.85):
        self.tau = confidence_threshold
        
    def edge_infer(self, packet: np.ndarray):
        start = time.perf_counter()
        # Simulated lightweight inference logic
        scores = np.abs(packet) / np.sum(np.abs(packet))
        pred_class = int(np.argmax(scores))
        conf = float(np.max(scores))
        lat = (time.perf_counter() - start) * 1000 + 14.2 # Base edge latency ms
        return pred_class, conf, lat

    def cloud_fallback(self):
        start = time.perf_counter()
        time.sleep(0.05)  # Simulate network hop
        lat = (time.perf_counter() - start) * 1000 + 410.0
        return "CLOUD_VERIFIED_ANOMALY", 0.0025, lat

    def process(self, packet: np.ndarray):
        pred, conf, edge_lat = self.edge_infer(packet)
        if conf >= self.tau:
            return {
                "route": "EDGE_LOCAL",
                "pred": pred,
                "confidence": round(conf, 4),
                "latency_ms": round(edge_lat, 2),
                "cost_usd": 0.00
            }
        else:
            cloud_pred, cost, cloud_lat = self.cloud_fallback()
            return {
                "route": "CLOUD_FALLBACK",
                "pred": cloud_pred,
                "confidence": "VERIFIED",
                "latency_ms": round(edge_lat + cloud_lat, 2),
                "cost_usd": cost
            }

if __name__ == "__main__":
    router = MockAdaptiveRouter(confidence_threshold=0.85)
    sample_packet = np.random.randn(8)
    result = router.process(sample_packet)
    print("Telemetry Routing Result:", result)
