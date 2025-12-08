from metis.dq_orchestrator import DQOrchestrator

# No config file means default to console writer
orchestrator = DQOrchestrator(writer_config_path="configs/writer/sqlite.json")

orchestrator.load(data_loader_configs=["data/adult.json"])

orchestrator.assess(metrics=["column_completeness_nullRatio"], metric_configs=[None])
orchestrator.assess(metrics=["column_minimality_duplicateCount"], metric_configs=[None])
orchestrator.assess(metrics=["column_validity_outOfVocabulary"], metric_configs=['{"use_nltk": true, "lowercase": true}'])