import typer
from datetime import datetime
from notion import NotionClient
from config import TOKEN,DATABASE_ID
# import speech_recognition as sr
# import gtts
# from playsound import playsound

app = typer.Typer()
# r = sr.Recognizer()

client = NotionClient(TOKEN, DATABASE_ID)

@app.command()
def createtask(task : str):

    now = datetime.now().astimezone().isoformat()
    res = client.create_page(task, now, status="Active")
    if res.status_code == 200:
            typer.secho(f"Added new task: {task}", fg=typer.colors.BRIGHT_GREEN)
            
            
# @app.command()
# def deletetask():
#     for row in cv.collection.get_rows():
#         row.remove(permanently=False)

# @app.command()
# def completed():
#     # newchild.checked = True
# # if(task_completed):  
#     pass 


























ADDTASK_COMMAND = "add"
DELTASK_COMMAND = "remove"
CHKTASK_COMMAND = "check"
UNCHKTASK_COMMAND = "uncheck"
LIST_COMMAND = "list"
HELP_COMMAND = "help"
EXIT_COMMAND = "exit"

def get_audio_init():
    with sr.Microphone() as source:
        typer.secho("Listening...", fg=typer.colors.BRIGHT_GREEN)
        audio = r.listen(source)
    return audio

def get_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
    return audio

def audio_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Did not get you.. Please try again")
    except sr.RequestError:
        print("Something went wrong.. Please try again after a few minutes")
    except Exception as e:
        print("Something went wrong")
    return text

def process_commands(text):
    if ADDTASK_COMMAND in text.lower():
        playsound("What task so you have in mind?")
        task = get_audio()
        task = audio_to_text(task)
        if task:
            playsound(f"Added new task: {task}")
            print()
            typer.secho(f"Added new task: {task}", fg=typer.colors.BRIGHT_BLUE)
    elif DELTASK_COMMAND in text.lower():
        playsound("Please specify the ID of the task you want to remove")
        task = get_audio()
        task = audio_to_text(task)
        task = int(task)
        if task:
            playsound(f"Removed task: {task}")
            print()
            typer.secho(f"Removed task: {task}", fg=typer.colors.BRIGHT_RED)
    elif CHKTASK_COMMAND in text.lower():
        playsound("Please specify the ID of the task you want to check")
        task = get_audio()
        task = audio_to_text(task)
        task = int(task)
        if task:
            playsound(f"Checked task: {task}")
            print()
            typer.secho(f"Checked task: {task}", fg=typer.colors.BRIGHT_YELLOW)
    elif UNCHKTASK_COMMAND in text.lower():
        playsound("Please specify the ID of the task you want to uncheck")
        task = get_audio()
        task = audio_to_text(task)
        task = int(task)
        if task:
            playsound(f"Unchecked task: {task}")
            print()
            typer.secho(f"Unchecked task: {task}", fg=typer.colors.BRIGHT_YELLOW)
    elif LIST_COMMAND in text.lower():
        playsound("Here's the list of tasks to be completed")
        typer.secho(f"List of available tasks", fg=typer.colors.BRIGHT_MAGENTA)
    elif HELP_COMMAND in text.lower():
        playsound(" Here are the list of available voice commands..")
        typer.secho("  List of available voice commands", fg=typer.colors.GREEN)
        typer.secho('''$ slate add - To add a new task to your notion database
        $ slate remove - To remove an existing task from your notion database
        $ slate check - To check an existing task in your notion database
        $ slate uncheck - To uncheck an existing task in your notion database
        $ slate list - To list all existing unchecked tasks in your notion database
        $ slate help - To open this help
        $ slate exit - To exit slate''', fg=typer.colors.BRIGHT_BLUE)
    elif EXIT_COMMAND in text.lower():
        playsound("Exiting slate..")
        typer.secho("Exiting Slate..", fg=typer.colors.BRIGHT_MAGENTA)
        raise typer.Exit()
    else:
        playsound("That is an unrecognised command, try saying 'slate help' to see all available commands")
        typer.secho("That is an unrecognised command, try saying 'slate help'", fg=typer.colors.BRIGHT_MAGENTA)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        banner = typer.style('''
                    ███████╗██╗      █████╗ ████████╗███████╗
                    ██╔════╝██║     ██╔══██╗╚══██╔══╝██╔════╝
                    ███████╗██║     ███████║   ██║   █████╗  
                    ╚════██║██║     ██╔══██║   ██║   ██╔══╝  
                    ███████║███████╗██║  ██║   ██║   ███████╗
                    ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝

        ▀▄▀▄▀▄  𝙰𝚞𝚝𝚑𝚘𝚛𝚜: 𝔄𝔯𝔞𝔳𝔦𝔫𝔡 𝔖 & 𝔄𝔯𝔧𝔲𝔫 𝔐𝔖 𝚅𝚎𝚛𝚜𝚒𝚘𝚗: 𝟢.𝟣.𝟢     ▀▄▀▄▀
    ''',  fg=typer.colors.WHITE)
        typer.echo(banner)
        typer.secho('''                     《《Get things done with Slate..! 》》''', fg=typer.colors.BRIGHT_YELLOW,  bold=True)
    # while True:
    #     a = get_audio_init()
    #     text = audio_to_text(a)
    #     process_commands(text)

if __name__ == "__main__":
    app()