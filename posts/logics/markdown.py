from django.conf import settings


def add_paths_to_markdown(markdown, paths: list, images_paths):
    for i in range(0, len(paths)):
        markdown = markdown.replace(f'[{paths[i]}_{i}]', f'[API_URL]{images_paths[i]}')
    return markdown


def add_api_url_to_markdown(markdown: str) -> str:
    return markdown.replace('[API_URL]', settings.API_URL)
