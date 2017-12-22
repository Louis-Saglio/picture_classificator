class ImageSelector:

    def __init__(self, controller):
        """
        :type controller: src.controller.Controller
        """
        self.controller = controller

    def get_image_nbr_by_pct(self, pct):
        return round((len(self.controller.image_comparator.images) * pct) / 100)

    def get_x_best_images(self, nbr):
        return sorted(
            self.controller.image_comparator.images, key=lambda x: self.controller.image_comparator.images[x]
        )[:-nbr]

    def get_x_pct_best_images(self, pct):
        return self.get_x_best_images(self.get_image_nbr_by_pct(pct))

    def delete_x_worst_images(self, nbr):
        images = sorted(
            self.controller.image_comparator.images, key=lambda x: self.controller.image_comparator.images[x]
        )[:nbr]
        for image in images:
            del self.controller.image_comparator.images[image]
            self.controller.file_manager.remove_image_file(image)

    def delete_x_pct_worst_images(self, pct):
        self.delete_x_worst_images(self.get_image_nbr_by_pct(pct))
