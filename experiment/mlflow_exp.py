import mlflow

def mlflow_logging(exp_param, model, params:dict, metrics:dict):

    experiment_name = exp_param['name']
    run_name = exp_param['run_name']
    artifact_path = exp_param['artifact_path']
    model_name = exp_param['model_name']
    signature = exp_param['signature']


    # set experiment
    mlflow.set_experiment(experiment_name)



    # initiate the logging
    with mlflow.start_run(run_name = run_name) as run:
        
        mlflow.log_params(params)

        mlflow.log_metrics(metrics)


        # Log an instance of the trained model for later use
        mlflow.sklearn.log_model(
            sk_model=model,  
            artifact_path=artifact_path,
            registered_model_name= model_name,
            signature=signature
        )







    


