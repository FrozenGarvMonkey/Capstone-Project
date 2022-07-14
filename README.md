# Capstone 2 - README

# Modules

```pip install -r requirements.txt```

## Run
```python CartoonGAN_main.py --test --model_path checkpoints/CartoonGAN/ModifiedGAN.ckpt --use_modified_model```

## Train

To train a new model, 
- Replace the cartoon image templates in data/photo.
- Run preprocessing.py for edge smoothing
- Run ```python CartoonGAN_main.py --use_modified_model``` 


## Training Adjustment

To adjust model parameters only change values in ```config.py```

