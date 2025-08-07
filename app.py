def lambda_handler(event, context):
    """
    AWS Lambda function handler.
    
    Args:
        event (dict): The event data passed to the Lambda function.
        context (LambdaContext): The runtime information of the Lambda function.
        
    Returns:
        dict: A response object containing status code and message.
    """
    try:
        # Process the event data
        print("Received event:", event)
        
        # Example processing logic
        result = {"message": "Hello from Lambda!"}
        
        return {
            "statusCode": 200,
            "body": result
        }
    
    except Exception as e:
        print("Error processing event:", e)
        return {
            "statusCode": 500,
            "body": {"error": str(e)}
        }