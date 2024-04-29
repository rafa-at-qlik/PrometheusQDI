import enum
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
@dataclass_json
@dataclass
class Task:
    """ DataClass to store Replicate tasks QEM metrics:
    https://help.qlik.com/en-US/enterprise-manager/November2023/Content/EnterpriseManager/
    EnterpriseManager_APIGuide/CurlAPI/api_getTaskDetails.htm

    """
    type: str = None
    name: str = ''
    description: str = ''
    state: enum = None
    message: str = ''
    source_endpoint: dict = None
    target_endpoint: dict = None
    cdc_event_counters: dict = None
    full_load_counters: dict = None
    full_load_completed: bool = None
    full_load_start: str = ''
    full_load_end: str = ''
    full_load_throughput: dict = None
    cdc_throughput: dict = None
    cdc_transactions_counters: dict = None
    cdc_latency: dict = None
    profile: str = ''
    task_stop_reason: enum = None
    memory_mb: int = None
    cpu_percentage: int = None
    disk_usage_mb: int = None
    data_error_count: int = None
    profile: str = ''
    options: dict = None
    log_stream_staging: str = ''
    assigned_tags: List[str] = None
