import time
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
import psutil
import asyncio

logger = logging.getLogger(__name__)

@dataclass
class RequestMetrics:
    """Metrics for a single request"""
    request_id: str
    start_time: float
    end_time: Optional[float] = None
    qloo_api_time: Optional[float] = None
    llm_processing_time: Optional[float] = None
    intent_detection_time: Optional[float] = None
    response_generation_time: Optional[float] = None
    success: bool = True
    error_message: Optional[str] = None
    user_language: Optional[str] = None
    intent_detected: Optional[str] = None
    qloo_api_calls: int = 0
    qloo_api_success: int = 0

class MetricsCollector:
    """Metrics collection and analysis system"""
    
    def __init__(self):
        self.requests: List[RequestMetrics] = []
        self.start_time = time.time()
        self._lock = asyncio.Lock()
    
    async def start_request(self, request_id: str) -> RequestMetrics:
        """Start new request"""
        metrics = RequestMetrics(
            request_id=request_id,
            start_time=time.time()
        )
        async with self._lock:
            self.requests.append(metrics)
        return metrics
    
    async def end_request(self, request_id: str, success: bool = True, error_message: str = None):
        """End request"""
        async with self._lock:
            for req in self.requests:
                if req.request_id == request_id:
                    req.end_time = time.time()
                    req.success = success
                    req.error_message = error_message
                    break
    
    async def record_qloo_api_call(self, request_id: str, duration: float, success: bool):
        """Record Qloo API call"""
        async with self._lock:
            for req in self.requests:
                if req.request_id == request_id:
                    if req.qloo_api_time is None:
                        req.qloo_api_time = 0
                    req.qloo_api_time += duration
                    req.qloo_api_calls += 1
                    if success:
                        req.qloo_api_success += 1
                    break
    
    async def record_llm_processing(self, request_id: str, duration: float):
        """Record LLM processing time"""
        async with self._lock:
            for req in self.requests:
                if req.request_id == request_id:
                    req.llm_processing_time = duration
                    break
    
    async def record_intent_detection(self, request_id: str, duration: float, intent: str):
        """Record intent detection time"""
        async with self._lock:
            for req in self.requests:
                if req.request_id == request_id:
                    req.intent_detection_time = duration
                    req.intent_detected = intent
                    break
    
    async def record_response_generation(self, request_id: str, duration: float):
        """Record response generation time"""
        async with self._lock:
            for req in self.requests:
                if req.request_id == request_id:
                    req.response_generation_time = duration
                    break
    
    async def record_language_detection(self, request_id: str, language: str):
        """Record language detection result"""
        async with self._lock:
            for req in self.requests:
                if req.request_id == request_id:
                    req.user_language = language
                    break
    
    def get_system_metrics(self) -> Dict:
        """Get system metrics"""
        try:
            memory = psutil.virtual_memory()
            cpu = psutil.cpu_percent(interval=1)
            
            return {
                "memory_usage_percent": memory.percent,
                "memory_available_gb": round(memory.available / (1024**3), 2),
                "cpu_usage_percent": cpu,
                "uptime_seconds": time.time() - self.start_time,
                "active_connections": len([r for r in self.requests if r.end_time is None])
            }
        except Exception as e:
            logger.error(f"Could not get system metrics: {e}")
            return {}
    
    def get_performance_metrics(self) -> Dict:
        """Get performance metrics"""
        if not self.requests:
            return {}
        
        completed_requests = [r for r in self.requests if r.end_time is not None]
        if not completed_requests:
            return {}
        
        # General metrics
        total_requests = len(completed_requests)
        successful_requests = len([r for r in completed_requests if r.success])
        error_requests = total_requests - successful_requests
        
        # Time metrics
        response_times = [r.end_time - r.start_time for r in completed_requests]
        avg_response_time = sum(response_times) / len(response_times)
        
        # Qloo API metrics
        qloo_times = [r.qloo_api_time for r in completed_requests if r.qloo_api_time is not None]
        avg_qloo_time = sum(qloo_times) / len(qloo_times) if qloo_times else 0
        
        # LLM metrics
        llm_times = [r.llm_processing_time for r in completed_requests if r.llm_processing_time is not None]
        avg_llm_time = sum(llm_times) / len(llm_times) if llm_times else 0
        
        # Intent detection metrics
        intent_times = [r.intent_detection_time for r in completed_requests if r.intent_detection_time is not None]
        avg_intent_time = sum(intent_times) / len(intent_times) if intent_times else 0
        
        return {
            "total_requests": total_requests,
            "successful_requests": successful_requests,
            "error_requests": error_requests,
            "success_rate_percent": round((successful_requests / total_requests) * 100, 2),
            "avg_response_time_ms": round(avg_response_time * 1000, 2),
            "avg_qloo_api_time_ms": round(avg_qloo_time * 1000, 2),
            "avg_llm_processing_time_ms": round(avg_llm_time * 1000, 2),
            "avg_intent_detection_time_ms": round(avg_intent_time * 1000, 2),
            "min_response_time_ms": round(min(response_times) * 1000, 2),
            "max_response_time_ms": round(max(response_times) * 1000, 2)
        }
    
    def get_language_metrics(self) -> Dict:
        """Get language usage metrics"""
        if not self.requests:
            return {}
        
        language_counts = {}
        for req in self.requests:
            if req.user_language:
                language_counts[req.user_language] = language_counts.get(req.user_language, 0) + 1
        
        return language_counts
    
    def get_intent_metrics(self) -> Dict:
        """Get intent detection metrics"""
        if not self.requests:
            return {}
        
        intent_counts = {}
        for req in self.requests:
            if req.intent_detected:
                intent_counts[req.intent_detected] = intent_counts.get(req.intent_detected, 0) + 1
        
        return intent_counts
    
    def get_recent_metrics(self, limit: int = 10) -> List[Dict]:
        """Get metrics for recent requests"""
        recent_requests = sorted(self.requests, key=lambda x: x.start_time, reverse=True)[:limit]
        
        metrics = []
        for req in recent_requests:
            metric = {
                "request_id": req.request_id,
                "start_time": datetime.fromtimestamp(req.start_time).isoformat(),
                "duration_ms": round((req.end_time - req.start_time) * 1000, 2) if req.end_time else None,
                "success": req.success,
                "user_language": req.user_language,
                "intent_detected": req.intent_detected,
                "qloo_api_calls": req.qloo_api_calls,
                "qloo_api_success": req.qloo_api_success
            }
            metrics.append(metric)
        
        return metrics

# Global metrics collector instance
metrics_collector = MetricsCollector() 