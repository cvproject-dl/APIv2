
﻿

# Flask API

RESTful Api for pytorch models.

## **URL** : `/`

 - **Method(s)** : `GET`
 - **Example**:
 
 ```
curl  http://127.0.0.1:5000/
```
```json
   {
      "prediction": "/predict",
      "list_of_cars": "/cars"
   }
 ```

## **URL** : `/predict`

- **Method(s)** : `POST`

|Parameters  |Required  |enum	     |
|--          |--        |--      | 
| image | True |nil |
|model|True|(sfcars,indcars)

 - sfcars = stanford cars dataset model
 - indcars = indian cars model

![updated](https://img.shields.io/badge/-updated-yellow?style=for-the-badge)    
 - Total cars
 - Supports detection of multiple cars in the image
```bash
curl -F 'image=@/Users/akshay/Desktop/hummer.jpg' -F 'model=sfcars'  http://127.0.0.1:5000/predict
```

<img src="https://i.pinimg.com/originals/b0/3a/5b/b03a5bb40d7fbc3b48fb07b18a02d7bf.jpg" width=400 height =250>

```json
{
  "predictions": [
    [
      {
        "car_details": {
          "id": 1,
          "name": "AM General Hummer SUV 2000",
          "image": "https://carimage.netlify.app/07684.jpg"
        },
        "confidence": 0.8825132846832275
      },
      {
        "car_details": {
          "id": 149,
          "name": "Jeep Wrangler SUV 2012",
          "image": "https://carimage.netlify.app/03089.jpg"
        },
        "confidence": 0.08587536215782166
      },
      {
        "car_details": {
          "id": 125,
          "name": "HUMMER H3T Crew Cab 2010",
          "image": "https://carimage.netlify.app/04800.jpg"
        },
        "confidence": 0.02418730966746807
      }
    ]
  ],
  "total_cars": 1,
  "status": 200
}

```

![new](https://img.shields.io/badge/-new-brightgreen?style=for-the-badge)    
### Multiclass
```bash
curl -F 'image=@/Users/akshay/Desktop/a.jpg' -F 'model=indcars'  http://127.0.0.1:5000/predict
```
<img src="https://www.cartoq.com/wp-content/uploads/2019/01/omni-eeco-featured.jpg" width=400 height =200>

```json
{
  "predictions": [
    [
      {
        "car_details": {
          "id": 66,
          "name": "Maruti Suzuki Eeco",
          "image": "https://carimage.netlify.app/maruti_suzuki_eeco.jpg"
        },
        "confidence": 0.802731454372406
      },
      {
        "car_details": {
          "id": 18,
          "name": "Chevrolet Tavera Neo 3",
          "image": "https://carimage.netlify.app/chevrolet_tavera_neo_3.jpg"
        },
        "confidence": 0.07866261899471283
      },
      {
        "car_details": {
          "id": 77,
          "name": "Maruti Suzuki Wagon R",
          "image": "https://carimage.netlify.app/maruti_suzuki_wagon_r.jpg"
        },
        "confidence": 0.03110526129603386
      }
    ],
    [
      {
        "car_details": {
          "id": 70,
          "name": "Maruti Suzuki Omni",
          "image": "https://carimage.netlify.app/maruti_suzuki_omni.jpg"
        },
        "confidence": 0.31989696621894836
      },
      {
        "car_details": {
          "id": 57,
          "name": "Mahindra Verito",
          "image": "https://carimage.netlify.app/mahindra_verito.jpg"
        },
        "confidence": 0.07384876906871796
      },
      {
        "car_details": {
          "id": 102,
          "name": "Tata Indigo eCS",
          "image": "https://carimage.netlify.app/tata_indigo_ecs.jpg"
        },
        "confidence": 0.05521629378199577
      }
    ]
  ],
  "total_cars": 2,
  "status": 200
}

```


## **URL** : `/cars`

- **Method(s)** : `GET`
- **Parameters**:

| Parameters | Required | Enum |
|--|--|--|
| model |True  | (sfcars,indcars)
|search|False|nil
|page|False|nil

- **Response** :
```bash
curl 'http://127.0.0.1:5000/cars?model=indcars&search=maruti&page=2'
```

```json
{
  "cars": [
    {
      "id": 70,
      "name": "Maruti Suzuki Omni",
      "image": "https://carimage.netlify.app/maruti_suzuki_omni.jpg"
    },
    {
      "id": 71,
      "name": "Maruti Suzuki S-Cross",
      "image": "https://carimage.netlify.app/maruti_suzuki_s-cross.jpg"
    },
    {
      "id": 72,
      "name": "Maruti Suzuki SX4",
      "image": "https://carimage.netlify.app/maruti_suzuki_sx4.jpg"
    },
  ],
  "status": 200,
  "invalidPage": false
}
```

## Download Models

- Gdrive Folder Link : [DL Models](https://bit.ly/dlproject-cv)
- Download the models and copy it to `model_files` folder

## YoloV5

 - Source : [Github](https://github.com/ultralytics/yolov5)

![credits](https://zenodo.org/badge/doi/10.5281/zenodo.4154370.svg)
