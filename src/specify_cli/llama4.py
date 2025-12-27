import click
from huggingface_hub import InferenceClient
import os

@click.command()
@click.option('--prompt', help='Le prompt pour Llama 4')
@click.option('--token', help='Token d\'API Hugging Face', default=os.getenv('HUGGINGFACE_TOKEN'))
def llama4_command(prompt, token):
    if not token:
        click.echo("Erreur : Token d'API Hugging Face manquant")
        return
    client = InferenceClient("meta-llama/Llama-4", token=token)
    response = client.text_generation(prompt, max_new_tokens=200)
    click.echo(response.generated_text)
