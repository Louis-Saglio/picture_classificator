from src.controller import Controller

# todo: log

controller = Controller("Linux")
controller.theme_manager.add_keyword("Archlinux", 1)
controller.theme_manager.add_ranked_keywords(2, "Open source", "Manjaro", "Kernel", "Wallpaper")
controller.theme_manager.add_ranked_keywords(3, "Debian", "Gentoo", "Slackware")
controller.theme_manager.add_ranked_keywords(4, "Python", "Golang")
controller.theme_manager.search_options["face"] = False
for i in range(10):  # TODO: choisir combien d'images télécharger
    controller.image_downloader.download_images()
controller.image_comparator.build_app()
while True:
    controller.image_comparator.compare()
