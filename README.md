# Hand Detection Model

Outputs X,Y coordinate for center of hand.

Intended for VR applications. Built for RCOS 2019.

## Endpoints

| Endpoints       | Parameters  | Description                            |
| --------------- | ----------- | -------------------------------------- |
| `GET /`         |             | Show how to use this service           |
| `POST /predict` | `imagefile` | Predicts where bounding box is located |

### POST /predict

Predicts location of bounding box on hand, returning `{x,y}` coordinates if successful or `{}` if no hand detected.

| Input Parameter | Description               |
| --------------- | ------------------------- |
| `imagefile`     | multipart/form-data image |

| Output | Description                                                                                    |
| ------ | ---------------------------------------------------------------------------------------------- |
| x      | `number` indicating location of hand in image from 0 to 1, where 1 is 100% of the image width  |
| y      | `number` indicating location of hand in image from 0 to 1, where 1 is 100% of the image height |

Output: `{x: number, y: number}` center of bounding box
