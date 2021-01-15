import torch
import torch.nn as nn
from torchvision import transforms, models
import PIL.Image as Image
from dbmodels import Cars
from multiclass import get_imgs


def load_model(checkpoint_path):
    f"""
    :param checkpoint_path: path to the saved model
   
    :return: 
    """
    checkpoint = torch.load(checkpoint_path)

    model = models.resnet34(pretrained=True)
    model.cpu()

    num_ftrs = model.fc.in_features

    model.fc = nn.Linear(num_ftrs, 293)

    model.load_state_dict(checkpoint['state_dict'])

    return model


def getpred(images, model):
    model.eval()
    # transforms for the input image

    loader = transforms.Compose([transforms.Resize((400, 400)),
                                 transforms.ToTensor(),
                                 transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    preds = []
    for image in images:
        image = loader(image).float()
        image = torch.autograd.Variable(image, requires_grad=True)
        image = image.unsqueeze(0)
        image = image.cpu()
        output = model(image)
        p = torch.nn.functional.softmax(output)
        top_probs, top_labs = p.topk(3)
        results = []
        for (lab, prob) in zip(top_labs[0], top_probs[0]):
            car_info = dict()
            car_info["confidence"] = float(prob)
            car_info["car_details"] = Cars.get_item_by_id(idno=int(lab) + 1)
            results.append(car_info)
        preds.append(results)
    return preds


def predict(fileloc, model):
    f"""
     :param fileloc: path to the image
     :param model: pass model after loading
     :return: 
    """
    images, total_cars = get_imgs(fileloc)
    return getpred(images, model), total_cars
