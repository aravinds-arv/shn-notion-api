import typer

app = typer.Typer()

@app.command()
def add(description: typer.Argument(None)):
    typer.secho("Added new task", fg=typer.colors.BRIGHT_GREEN)

if __name__ == '__main__':
    app()
