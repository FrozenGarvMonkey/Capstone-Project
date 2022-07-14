import torch


class CartoonGANConfig:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # dataloader.py
    batch_size = 2
    num_workers = 0
    photo_image_dir = "data/photo/"
    animation_image_dir = "data/animation/"
    edge_smoothed_image_dir = "data/edge_smoothed/"
    test_photo_image_dir = "data/test/"

    # CartoonGAN_train.py
    adam_beta1 = 0.5
    lr = 0.0002
    num_epochs = 100
    initialization_epochs = 10
    content_loss_weight = 20
    print_every = 100
