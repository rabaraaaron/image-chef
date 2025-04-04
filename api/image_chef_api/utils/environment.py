import os


class Environment:
    _instance = None
    config = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Environment, cls).__new__(cls)
            cls._instance.load_initial_config()
        return cls._instance

    def __init__(self):
        self.config["FLUX_SCHNELL"] = os.environ.get("FLUX_SCHNELL") if os.environ.get(
            "FLUX_SCHNELL") else "C:\\Users\\633578\\Repositories\\image-chef\\api\\image_chef_api\\models\\FLUX.1-schnell"
        self.config["FLUX_FILL"] = os.environ.get("FLUX_FILL") if os.environ.get(
            "FLUX_FILL") else "C:\\Users\\633578\\Repositories\\image-chef\\api\\image_chef_api\\models\\FLUX.1-Fill-dev"
        self.config["FLUX_REFINEMENT"] = os.environ.get("FLUX_REFINEMENT") if os.environ.get(
            "FLUX_REFINEMENT") else "C:\\Users\\633578\\Repositories\\image-chef\\api\\image_chef_api\\models\\stable-diffusion-xl-refiner-1.0"
