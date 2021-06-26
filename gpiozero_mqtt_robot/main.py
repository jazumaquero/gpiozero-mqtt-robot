import click


@click.command()
@click.version_option()
def main():
    click.echo(" This project aims to show how to create some remote controlled robot using Raspberry Pi and MQTT..")


if __name__ == "__main__":
    main(prog_name="gpiozero-mqtt-robot")
