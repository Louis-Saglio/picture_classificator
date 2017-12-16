from src.theme_manager import ThemeManager

theme = ThemeManager()
theme.add_keyword("Arbre", 0)
theme.add_ranked_keywords(1, "Branche", "Tronc")
theme.add_keyword("Feuille", 2)
theme.get_images(30)
theme.process()
