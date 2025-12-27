import click
import os
import requests

@click.command()
@click.option('--prompt', help='Le prompt pour générer du code')
@click.option('--lang', help='Le langage de programmation (ex: python, javascript)')
def meta_ai_command(prompt, lang):
    api_key = os.environ.get('META_AI_API_KEY')
    endpoint = 'https://api.meta-ai.com/v1/code/generate'  # Endpoint personnalisé pour la génération de code
    params = {
        'prompt': prompt,
        'lang': lang,
        'max_tokens': 200,  # Ajuste selon tes besoins
    }
    response = requests.post(endpoint, json=params, headers={'Authorization': f'Bearer {api_key}'})
    if response.status_code == 200:
        click.echo(response.json()['code'])
    else:
        click.echo(f'Erreur: {response.status_code}')
