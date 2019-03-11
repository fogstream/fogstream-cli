import click

from fogstream_cli.commands import InitprojectCommand


@click.group()
def cli():
    pass


@cli.command()
@click.argument('project_name')
@click.argument('git-url')
@click.option('-d', default=None, help='path to project directory')
def initproject(git_url, project_name, d):
    InitprojectCommand(
        git_url=git_url,
        project_name=project_name,
        dist_dir=d
    ).run()


def main():
    cli()
