import click
import datetime
import getpass


class Note(object):
    def __init__(self, text, user):
        self.text = text
        self.user = user
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@click.group()
def setup_directory():
    pass


@setup_directory.command()
@click.argument('save_directory')
def setup(save_directory):
    # create setup file
    '''
        Provide the location where you want your notes to be safe, default file name is notes.txt,
        that cannot be change yet.

        Here is an example of how you should use this command argument:
        takeNotes.py setup /home/username/some_folder
     '''
    with open("setup.txt", "w") as file:
        file.write(save_directory + "/notes.txt")


@click.group()
def note_taking():
    pass


@note_taking.command()
@click.argument('note')
def note(note):
    '''
        This command only receive the notes under quotes.

        Example:
        takeNotes.py note "This is a cool note!"
    '''
    with open("setup.txt", "r") as file:
        with open(file.readline(), "a") as notes:
            n = Note(note, getpass.getuser())
            notes.write(n.text + "/" + str(n.user) + "/" + str(n.date) + "\n")


@click.group()
def list_notes():
    pass


@list_notes.command()
def list():
    '''
        This command does not take any argument.

        This command will return all your notes, in the order of writing from top to bottom, there is not any sort
        implementation yet.

        Example:
        takeNotes.py list
    '''
    with open("setup.txt", "r") as file:
        with open(file.readline(), "r") as note:
            for l in note:
                l = l.strip('\n')
                n = l.split('/')
                click.echo(f"{n[1]}: {n[0]} - {n[2]}")


main = click.CommandCollection(sources=[setup_directory, note_taking, list_notes])


if __name__ == '__main__':
    main()
