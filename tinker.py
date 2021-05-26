import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_name="config")
def run(cfg: DictConfig):
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    run()
