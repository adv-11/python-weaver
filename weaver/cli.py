# weaver/cli.py

import sys
import click
from weaver.project import Project
from weaver.exceptions import WeaverError

@click.group()
def cli():
    """python-weaver CLI: Create and run long-duration LLM workflows."""
    pass

@cli.command()
@click.argument("project_name")
@click.argument("project_goal")
def init(project_name, project_goal):
    """Initialize a new weaver project."""
    try:
        project = Project(project_name, project_goal)
        click.echo(f"[weaver] Initialized project '{project_name}'.")
    except WeaverError as e:
        click.echo(f"[weaver][error] {e}", err=True)
        sys.exit(1)

@cli.command()
@click.argument("project_name")
@click.argument("sources", nargs=-1, type=click.Path(exists=True))
def ingest(project_name, sources):
    """Ingest local files or URLs into an existing project."""
    try:
        project = Project(project_name, project.load_state_path())
        project.ingest(list(sources))
        click.echo(f"[weaver] Ingested {len(sources)} sources into '{project_name}'.")
    except WeaverError as e:
        click.echo(f"[weaver][error] {e}", err=True)
        sys.exit(1)

@cli.command()
@click.argument("project_name")
def plan(project_name):
    """Generate a step-by-step plan for an existing project."""
    try:
        project = Project(project_name, project.load_state_path())
        project.plan()
        click.echo(f"[weaver] Plan generated. Edit '{project_name}/blueprint.csv' if desired.")
    except WeaverError as e:
        click.echo(f"[weaver][error] {e}", err=True)
        sys.exit(1)

@cli.command()
@click.argument("project_name")
@click.option("--no-human-feedback", is_flag=True, help="Run without pausing for CSV edits.")
@click.option("--steps", default=0, help="Number of tasks to run (0 = all).")
def run(project_name, no_human_feedback, steps):
    """Execute the project’s tasks."""
    try:
        project = Project(project_name, project.load_state_path())
        project.run(human_feedback=not no_human_feedback, steps=steps)
        click.echo(f"[weaver] Execution complete for '{project_name}'.")
    except WeaverError as e:
        click.echo(f"[weaver][error] {e}", err=True)
        sys.exit(1)

def main():
    cli()

if __name__ == "__main__":
    main()
