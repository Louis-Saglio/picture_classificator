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
controller.image_selector.get_x_pct_best_images(10)
controller.image_selector.delete_x_pct_worst_images(50)
controller.image_comparator.compare_loop()
