import settings


def height_percentage(percentage):
    return str((settings.Height / 100) * percentage)


def width_percentage(percentage):
    return str((settings.Width / 100) * percentage)