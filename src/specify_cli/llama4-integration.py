import click
from huggingface_hub import InferenceClient

@click.command()
@click.option('--prompt', help='Le prompt pour Llama 4')
def llama4_command(prompt):
    client = InferenceClient("meta-llama/Llama-4")
    response = client.text_generation(prompt, max_new_tokens=200)
    click.echo(response.generated_text)
