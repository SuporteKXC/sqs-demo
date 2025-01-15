import boto3
import json
import time

sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/00000000000/demo-queue-1'

while True:
    print('Pooling...')
    
    response = sqs.receive_message(
        QueueUrl = queue_url,
        MaxNumberOfMessages=2, # Lê no máximo 2 mensagens da fila
        VisibilityTimeout=15, # Mensagem demora 15 segundos para voltar para a fila, caso não tenha sido excluída
        WaitTimeSeconds=10  # Espera até 10 segundos por uma mensagem
    )
    
    if 'Messages' not in response:
        print('Nenhuma mensagem encontrada...')
        continue
    
    print('Mensagens Consumidas: ', len(response['Messages']))
    
    for message in response['Messages']:
        print('messageId: ', message['MessageId'])
        print(message['Body'])
        
        # Faz algo com a mensagem
        time.sleep(2)
        
        # Exclui a mensagem
        sqs.delete_message(
            QueueUrl = queue_url,
            ReceiptHandle = message['ReceiptHandle']
        )
        
        print('Mensagem Excluída!')
        
        
        