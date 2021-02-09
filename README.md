## Car Identification REST API
A simple REST API to identify Car(s) from the uploaded image
## `/cars`

 - **Parameters**

| Param |Required  |
|--|--|
| page |No  |
| search |No |

---
**Examples**

 1. **No parameters**
 
-  Request :
```bash
curl --location --request GET 'https://127.0.0.1:5000/cars'
```
- Response  [200]:
```json
{
  "cars": [
    {
      "id": 1,
      "name": "AM General Hummer SUV 2000",
      "image": "https://carimage.netlify.app/07684.jpg",
      "fuel_type": "Diesel",
      "fuel_tank_capacity": "159",
      "seating_capacity": "2 to 4",
      "body_type": "Convertible",
      "transmission_type": "Automatic"
    },
    ...
    ],
   "status": 200,
  "invalidPage": false
 }
```
---
2.  **Get Cars (Page 10)**
- Request
```bash
curl --location --request GET 'https://127.0.0.1:5000/cars?page=10'
```
- Response [200]
```json
{
    "cars": [
        {
            "id": 91,
            "name": "Dodge Caliber Wagon 2012",
            "image": "https://carimage.netlify.app/03460.jpg",
            "fuel_type": "Gas",
            "fuel_tank_capacity": "102",
            "seating_capacity": "5",
            "body_type": "Wagon",
            "transmission_type": "Manual"
        },
	       ...
        {
            "id": 100,
            "name": "Dodge Journey SUV 2012",
            "image": "https://carimage.netlify.app/00349.jpg",
            "fuel_type": "Gas",
            "fuel_tank_capacity": "78",
            "seating_capacity": "5",
            "body_type": "SUV",
            "transmission_type": "Automatic"
        }
    ],
    "status": 200,
    "invalidPage": false
}
```
---
3. **Get Cars (Invalid Page)**
- Request
```bash
curl --location --request GET 'https://127.0.0.1:5000/cars?page=500'
```
- Response [400]
```json
{
    "cars": [],
    "status": 400,
    "invalidPage": true
}
```
---
4. **Search Cars**
- Request
```bash
curl --location --request GET 'https://127.0.0.1:5000/cars?search=Maruti&page=2'
```
- Response [200]
```json
{
    "cars": [
        {
            "id": 213,
            "name": "Maruti Suzuki S-Cross",
            "image": "https://carimage.netlify.app/maruti_suzuki_s-cross.jpg",
            "fuel_type": "Petrol",
            "fuel_tank_capacity": "48",
            "seating_capacity": "5",
            "body_type": "SUV",
            "transmission_type": "Automatic"
        },
	     ...
        {
            "id": 219,
            "name": "Maruti Suzuki Wagon R",
            "image": "https://carimage.netlify.app/maruti_suzuki_wagon_r.jpg",
            "fuel_type": "Petrol",
            "fuel_tank_capacity": "32",
            "seating_capacity": "5",
            "body_type": "Hatchback",
            "transmission_type": "Automatic"
        }
    ],
    "status": 200,
    "invalidPage": false
}
```
---
5. **Search Cars (BAD REQUEST example)**
- Request
```bash
curl --location --request GET 'https://127.0.0.1:5000/cars?search=Acuradbasdjbas'
```
- Response
```json
{
    "cars": [],
    "status": 400,
    "invalidPage": true
}
```
---
## `/predict`

- **Parameters**

|  Param| Required |
|--|--|
|  image| Yes |

---
- **Examples**
1.  **Single Car**
- Request 
```bash
curl --location --request POST 'https://127.0.0.1:5000/predict' \
--form 'image=@"/C:/Downloads/omni.jpg"'
```
- Response [200]
```json
{
  "predictions": [
    [
      {
        "confidence": 0.4241812825202942,
        "car_details": {
          "id": 212,
          "name": "Maruti Suzuki Omni",
          "image": "https://carimage.netlify.app/maruti_suzuki_omni.jpg",
          "fuel_type": "Petrol",
          "fuel_tank_capacity": "36",
          "seating_capacity": "5",
          "body_type": "Minivan",
          "transmission_type": "Manual"
        }
      },
      {
        "confidence": 0.33098340034484863,
        "car_details": {
          "id": 135,
          "name": "GMC Savana Van 2012",
          "image": "https://carimage.netlify.app/02290.jpg",
          "fuel_type": "Flex-fuel",
          "fuel_tank_capacity": "117",
          "seating_capacity": "12",
          "body_type": "van",
          "transmission_type": "Automatic"
        }
      },
      {
        "confidence": 0.22958144545555115,
        "car_details": {
          "id": 117,
          "name": "Ford E-Series Wagon Van 2012",
          "image": "https://carimage.netlify.app/05862.jpg",
          "fuel_type": "Flex-fuel",
          "fuel_tank_capacity": "132",
          "seating_capacity": "15",
          "body_type": "van",
          "transmission_type": "Automatic"
        }
      }
    ]
  ],
  "total_cars": 1,
  "status": 200
}
```
---
2. **Multiple Cars**
- Request
```bash
curl --location --request POST 'https://127.0.0.1:5000/predict' \
--form 'image=@"/C:/Downloads/oe.jpg"'
```
- Response[200]
```json
{
  "predictions": [
    [
      {
        "confidence": 0.5640007257461548,
        "car_details": {
          "id": 208,
          "name": "Maruti Suzuki Eeco",
          "image": "https://carimage.netlify.app/maruti_suzuki_eeco.jpg",
          "fuel_type": "CNG",
          "fuel_tank_capacity": "65",
          "seating_capacity": "5",
          "body_type": "Minivan",
          "transmission_type": "Manual"
        }
      },
      {
        "confidence": 0.1736801415681839,
        "car_details": {
          "id": 13,
          "name": "Audi 100 Wagon 1994",
          "image": "https://carimage.netlify.app/03435.jpg",
          "fuel_type": "Gas",
          "fuel_tank_capacity": "80",
          "seating_capacity": "5",
          "body_type": "Sedan",
          "transmission_type": "Automatic"
        }
      },
      {
        "confidence": 0.14361479878425598,
        "car_details": {
          "id": 285,
          "name": "Volkswagen Golf Hatchback 1991",
          "image": "https://carimage.netlify.app/03300.jpg",
          "fuel_type": "Gas",
          "fuel_tank_capacity": "55",
          "seating_capacity": "5",
          "body_type": "Hatchback",
          "transmission_type": "Manual"
        }
      }
    ],
    [
      {
        "confidence": 0.4241812825202942,
        "car_details": {
          "id": 212,
          "name": "Maruti Suzuki Omni",
          "image": "https://carimage.netlify.app/maruti_suzuki_omni.jpg",
          "fuel_type": "Petrol",
          "fuel_tank_capacity": "36",
          "seating_capacity": "5",
          "body_type": "Minivan",
          "transmission_type": "Manual"
        }
      },
      {
        "confidence": 0.33098340034484863,
        "car_details": {
          "id": 135,
          "name": "GMC Savana Van 2012",
          "image": "https://carimage.netlify.app/02290.jpg",
          "fuel_type": "Flex-fuel",
          "fuel_tank_capacity": "117",
          "seating_capacity": "12",
          "body_type": "van",
          "transmission_type": "Automatic"
        }
      },
      {
        "confidence": 0.22958144545555115,
        "car_details": {
          "id": 117,
          "name": "Ford E-Series Wagon Van 2012",
          "image": "https://carimage.netlify.app/05862.jpg",
          "fuel_type": "Flex-fuel",
          "fuel_tank_capacity": "132",
          "seating_capacity": "15",
          "body_type": "van",
          "transmission_type": "Automatic"
        }
      }
    ]
  ],
  "total_cars": 2,
  "status": 200
}
```
---
3. **Invalid File**
- Request
```bash
curl --location --request POST 'https://127.0.0.1:5000/predict' \
--form 'image=@"/C:/Downloads/vim.pdf"'
```
- Response[404]
```json	
{
    "message": {
        "error": "Invalid Filename",
        "status": 404
    }
}
```
  ---
## Download Models

- Gdrive Folder Link : [DL Models](https://bit.ly/dlproject-cv)
- Download the models and copy it to `model_files` folder

## YoloV5

 - Source : [Github](https://github.com/ultralytics/yolov5)

![credits](https://zenodo.org/badge/doi/10.5281/zenodo.4154370.svg)
