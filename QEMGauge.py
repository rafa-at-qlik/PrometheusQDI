from prometheus_client import Gauge
from Task import *
from qem_util import *

class QEMGauge(Task):

    def __init__(self):
        self.labels = ["replicate_server", "task_name"]
        # cdc_event_counters
        self.cdc_event_counters__applied_insert_count = \
            Gauge("cdc_event_counters__applied_insert_count",
                  "The number of records added in total for all tables."
                  , self.labels)
        self.cdc_event_counters__applied_update_count = \
            Gauge("cdc_event_counters__applied_update_count",
                  "The number of records updated in total for all tables."
                  , self.labels)
        self.cdc_event_counters__applied_delete_count = \
            Gauge("cdc_event_counters__applied_delete_count",
                  "The number of records deleted in total for all tables.", self.labels)
        self.cdc_event_counters__applied_ddl_count = \
            Gauge("cdc_event_counters__applied_ddl_count",
                  "The total number of metadata changes, such as add column."
                  , self.labels)
        #####
        # full_load_counters
        self.full_load_counters__tables_completed_count = \
            Gauge("full_load_counters__tables_completed_count",
                  "The number of tables that have been loaded into the target endpoint."
                  , self.labels)

        self.full_load_counters__tables_loading_count = \
            Gauge("full_load_counters__tables_loading_count",
                  "The number of tables that are currently being loaded into the target endpoint."
                  , self.labels)
        self.full_load_counters__tables_queued_count = \
            Gauge("full_load_counters__tables_queued_count",
                  "The number of tables that are waiting to be loaded due to an error."
                  , self.labels)

        self.full_load_counters__tables_with_error_count = \
            Gauge("full_load_counters__tables_with_error_count",
                  "The number of tables that could not be loaded due to an error."
                  , self.labels)

        self.full_load_counters__records_completed_count = \
            Gauge("full_load_counters__records_completed_count",
                  "The total number of records that have completed loading into the target endpoint."
                  , self.labels)

        self.full_load_counters__estimated_records_for_all_tables_count = \
            Gauge("full_load_counters__estimated_records_for_all_tables_count",
                  "The estimated number of records remaining to be loaded into the target endpoint."
                  , self.labels)
        #####
        # full_load_throughput
        self.full_load_throughput__source_throughput_records_count = \
            Gauge("full_load_throughput__source_throughput_records_count",
                  "The current source throughput, in rec/sec."
                  , self.labels)

        self.full_load_throughput__source_throughput_volume = \
            Gauge("full_load_throughput__source_throughput_volume",
                  "The current source throughput, in kbyte/sec."
                  , self.labels)

        self.full_load_throughput__target_throughput_records_count = \
            Gauge("full_load_throughput__target_throughput_records_count",
                  "The current target throughput, in rec/sec."
                  , self.labels)

        self.full_load_throughput__target_throughput_volume = \
            Gauge("full_load_throughput__target_throughput_volume",
                  "The current target throughput, in kbyte/sec."
                  , self.labels)
        #####
        # cdc_throughput
        self.cdc_throughput__source_throughput_records_count__current = \
            Gauge("cdc_throughput__source_throughput_records_count__current",
                  "The current source throughput, in rec/sec."
                  , self.labels)

        self.cdc_throughput__source_throughput_volume__current = \
            Gauge("cdc_throughput__source_throughput_volume__current",
                  "The current source throughput, in kbyte/sec."
                  , self.labels)

        self.cdc_throughput__target_throughput_records_count__current = \
            Gauge("cdc_throughput__target_throughput_records_count__current",
                  "The current target throughput, in rec/sec."
                  , self.labels)

        self.cdc_throughput__target_throughput_volume__current = \
            Gauge("cdc_throughput__target_throughput_volume__current",
                  "The current target throughput, in kbyte/sec."
                  , self.labels)
        #####
        # cdc_transactions_counters
        self.cdc_transactions_counters__commit_change_records_count = \
            Gauge("cdc_transactions_counters__commit_change_records_count",
                  "The number of COMMIT change records"
                  , self.labels)

        self.cdc_transactions_counters__rollback_transaction_count = \
            Gauge("cdc_transactions_counters__rollback_transaction_count",
                  "The number of ROLLBACK transactions"
                  , self.labels)

        self.cdc_transactions_counters__rollback_change_records_count = \
            Gauge("cdc_transactions_counters__rollback_change_records_count",
                  "The number of ROLLBACK change records"
                  , self.labels)

        self.cdc_transactions_counters__rollback_change_volume_mb = \
            Gauge("cdc_transactions_counters__rollback_change_volume_mb",
                  "The volume of ROLLBACK change, in MB."
                  , self.labels)

        self.cdc_transactions_counters__applied_transactions_in_progress_count = \
            Gauge("cdc_transactions_counters__applied_transactions_in_progress_count",
                  "The number of transactions in progress."
                  , self.labels)

        self.cdc_transactions_counters__applied_records_in_progress_count = \
            Gauge("cdc_transactions_counters__applied_records_in_progress_count",
                  "The sum of all records/events in all In-Progress transactions."
                  , self.labels)

        self.cdc_transactions_counters__applied_comitted_transaction_count = \
            Gauge("cdc_transactions_counters__applied_committed_transaction_count",
                  "The number of transactions committed"
                  , self.labels)

        self.cdc_transactions_counters__applied_records_comitted_count = \
            Gauge("cdc_transactions_counters__applied_records_comitted_count",
                  "The sum of all records/events in all Completed transactions"
                  , self.labels)

        self.cdc_transactions_counters__applied_volume_comitted_mb = \
            Gauge("cdc_transactions_counters__applied_volume_comitted_mb",
                  "The sum of all volume/events in all Completed transactions, in MB."
                  , self.labels)

        self.cdc_transactions_counters__incoming_accumulated_changes_in_memory_count = \
            Gauge("cdc_transactions_counters__incoming_accumulated_changes_in_memory_count",
                  "The sum of all volume/events in all Completed transactions, in MB."
                  , self.labels)

        self.cdc_transactions_counters__incoming_accumulated_changes_on_disk_count = \
            Gauge("cdc_transactions_counters__incoming_accumulated_changes_on_disk_count",
                  "The number of changes on disk during apply and until target commit."
                  , self.labels)
        #####
        # cdc_latency
        self.cdc_latency__source_latency = \
            Gauge("cdc_latency__source_latency",
                  "The time gap between the original change in the source endpoint "
                  "and capturing it, in seconds."
                  , self.labels)

        self.cdc_latency__total_latency = \
            Gauge("cdc_latency__total_latency",
                  "The overall latency (source latency + target latency + apply latency), in seconds"
                  , self.labels)

        self.memory_mb = \
            Gauge("memory_mb",
                  "The current utilization of memory, in MB. A task's memory utilization "
                  "is sampled every 10 seconds. When the task is not running, the value is set to zero (0)."
                  , self.labels)

        self.cpu_percentage = \
            Gauge("cpu_percentage",
                  "The current CPU usage of the Replicate task process."
                  , self.labels)

        self.disk_usage_mb = \
            Gauge("disk_usage_mb",
                  "The current utilization of disk space, in MB. A task's disk utilization is sampled every minute."
                  , self.labels)

        self.data_error_count = \
            Gauge("data_error_count",
                  "The total number of data errors in all tables involved in the task. The count is "
                  "affected by data errors and the Reset Data Errors option available when you drill down to a task."
                  , self.labels)

    def set_gauges(self, v_task_dc, v_rep_server, v_task_name):

        # cdc_event_counters
        self.cdc_event_counters__applied_insert_count.labels({"replicate_server": v_rep_server},
                                                             {"task_name": v_task_name}).set(
            v_task_dc.cdc_event_counters['applied_insert_count'])

        self.cdc_event_counters__applied_update_count.labels({"replicate_server": v_rep_server},
                                                             {"task_name": v_task_name}).set(
            v_task_dc.cdc_event_counters['applied_update_count'])

        self.cdc_event_counters__applied_delete_count.labels({"replicate_server": v_rep_server},
                                                             {"task_name": v_task_name}).set(
            v_task_dc.cdc_event_counters['applied_delete_count'])

        self.cdc_event_counters__applied_ddl_count.labels({"replicate_server": v_rep_server},
                                                             {"task_name": v_task_name}).set(
            v_task_dc.cdc_event_counters['applied_ddl_count'])

        # full_load_counters
        self.full_load_counters__tables_completed_count.labels({"replicate_server": v_rep_server},
                                                             {"task_name": v_task_name}).set(
            v_task_dc.full_load_counters['tables_completed_count'])

        self.full_load_counters__tables_loading_count.labels({"replicate_server": v_rep_server},
                                                             {"task_name": v_task_name}).set(
            v_task_dc.full_load_counters['tables_loading_count'])

        self.full_load_counters__tables_queued_count.labels({"replicate_server": v_rep_server},
                                                             {"task_name": v_task_name}).set(
            v_task_dc.full_load_counters['tables_queued_count'])

        self.full_load_counters__tables_with_error_count.labels({"replicate_server": v_rep_server},
                                                             {"task_name": v_task_name}).set(
            v_task_dc.full_load_counters['tables_with_error_count'])

        self.full_load_counters__records_completed_count.labels({"replicate_server": v_rep_server},
                                                             {"task_name": v_task_name}).set(
            v_task_dc.full_load_counters['records_completed_count'])

        self.full_load_counters__estimated_records_for_all_tables_count.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.full_load_counters['estimated_records_for_all_tables_count'])
        #####
        # full_load_throughput
        self.full_load_throughput__source_throughput_records_count.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.full_load_throughput['source_throughput_records_count'])

        self.full_load_throughput__source_throughput_volume.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.full_load_throughput['source_throughput_volume'])

        self.full_load_throughput__target_throughput_records_count.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.full_load_throughput['target_throughput_records_count'])

        self.full_load_throughput__target_throughput_volume.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.full_load_throughput['target_throughput_volume'])
        #####
        # cdc_throughput
        self.cdc_throughput__source_throughput_records_count__current.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_throughput['source_throughput_records_count']['current'])

        self.cdc_throughput__source_throughput_volume__current.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_throughput['source_throughput_volume']['current'])

        self.cdc_throughput__target_throughput_records_count__current.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_throughput['target_throughput_records_count']['current'])

        self.cdc_throughput__target_throughput_volume__current.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_throughput['target_throughput_volume']['current'])
        #####
        # cdc_transactions_counters
        self.cdc_transactions_counters__commit_change_records_count.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_transactions_counters['commit_change_records_count'])

        self.cdc_transactions_counters__rollback_transaction_count.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_transactions_counters['rollback_transaction_count'])

        self.cdc_transactions_counters__rollback_change_records_count.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_transactions_counters['rollback_change_records_count'])

        self.cdc_transactions_counters__rollback_change_volume_mb.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_transactions_counters['rollback_change_volume_mb'])

        self.cdc_transactions_counters__applied_transactions_in_progress_count.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_transactions_counters['applied_transactions_in_progress_count'])

        self.cdc_transactions_counters__applied_records_in_progress_count.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_transactions_counters['applied_records_in_progress_count'])

        self.cdc_transactions_counters__applied_comitted_transaction_count.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_transactions_counters['applied_comitted_transaction_count'])

        self.cdc_transactions_counters__applied_records_comitted_count.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_transactions_counters['applied_records_comitted_count'])

        self.cdc_transactions_counters__applied_volume_comitted_mb.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_transactions_counters['applied_volume_comitted_mb'])

        self.cdc_transactions_counters__incoming_accumulated_changes_in_memory_count.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_transactions_counters['incoming_accumulated_changes_in_memory_count'])

        self.cdc_transactions_counters__incoming_accumulated_changes_on_disk_count.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cdc_transactions_counters['incoming_accumulated_changes_on_disk_count'])
        #####
        # cdc_latency
        self.cdc_latency__source_latency.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            get_sec(v_task_dc.cdc_latency['source_latency']))

        self.cdc_latency__total_latency.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            get_sec(v_task_dc.cdc_latency['total_latency']))
        #####
        self.memory_mb.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.memory_mb)

        self.cpu_percentage.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.cpu_percentage)

        self.disk_usage_mb.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.disk_usage_mb)

        self.data_error_count.labels(
            {"replicate_server": v_rep_server}, {"task_name": v_task_name}).set(
            v_task_dc.data_error_count)
