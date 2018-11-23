#!/usr/bin/env python
import click
import os


def create_folders(directory, js=True, css=True):
    if not os.path.exists(directory):
        os.makedirs(directory)

        ''' Create JS and CSS folders inside the requested dir '''
        ''' Only if js and css = True '''

        if js:
            os.makedirs(directory + '/js')

        if css:
            os.makedirs(directory + '/css')

        ''' Create index.html with basic structure '''
        f = open(directory + "/index.html", "w")

        f.write("<!DOCTYPE html> \n"
                "<html> \n"
                "<head>\n"
                "</head>\n"
                "<body> \n"
                "</body>\n"
                "</html>")
        f.close()
    else:
        print('This folder already exist.')


@click.command()
@click.argument('directory_name')
@click.option('--js', default=True, type=bool, help='If you want to create JS folder, True by default')
@click.option('--css',  default=True, type=bool, help='If you want to create CSS folder, True  by default')
def main(directory_name, js, css):
    create_folders(directory_name, js, css)


if __name__ == "__main__":
    main()
