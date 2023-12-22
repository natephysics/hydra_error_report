import hydra


@hydra.main(version_base="1.3", config_path=".", config_name="config.yaml")
def my_app(cfg):
    print(type(cfg.get("country", "Amerika")))


if __name__ == "__main__":
    my_app()
