import requests

distances = []
for i in range(1,4):

    res = requests.post("http://127.0.0.1:5000/predict", files={"imagefile": open("images/test{}.jpg".format(i),'rb')}).json()
    [_, xc, yc, _, _] = [float(n) for n in open("images/test{}.txt".format(i)).read().split(" ")]

    dist = ((res["x"] - xc)**2 + (res["y"] - yc)**2)**0.5

    distances.append(dist)

print("All Distances")
print("\n".join(["{:.2f}%".format(f*100) for f in distances]))
print("Average Distance", "{:.2f}%".format(sum(distances) / len(distances)*100))
