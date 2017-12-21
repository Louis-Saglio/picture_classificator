import src.exceptions
from src.controller import Controller

# todo: log

controller = Controller("Linux")
controller.settings.DEBUG = False
controller.theme_manager.add_keyword("Archlinux", 1)
controller.theme_manager.add_ranked_keywords(2, "Open source", "Manjaro", "Kernel", "Wallpaper")
controller.theme_manager.add_ranked_keywords(3, "Debian", "Gentoo", "Slackware")
controller.theme_manager.add_ranked_keywords(4, "Python", "Golang")
controller.theme_manager.search_options["face"] = False
controller.image_downloader.download_images(image_nbr=5)
controller.image_comparator.build_app()
while True:
    try:
        controller.image_comparator.compare()
    except src.exceptions.EndProgramSignal:
        print("Le programme s'est terminé normalement.")
        controller.save()
        exit(0)
