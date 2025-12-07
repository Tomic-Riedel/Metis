from metis.dq_orchestrator import DQOrchestrator

orchestrator = DQOrchestrator()

orchestrator.load(data_loader_configs=["data/countries-capitals.json"])

# Only the metric Consistency needs a config file
orchestrator.assess(metrics=["column_completeness_missingRatio", "table_consistency_functionalDependency"], metric_configs=["", "configs/metric/consistency.json"])