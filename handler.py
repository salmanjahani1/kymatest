def main(event, context):
    message = "Hello World from the Kyma Function "+context['function-name']+" running on "+context['runtime']+ " created by Salman! (Git version)";
    print(message)
    return message
