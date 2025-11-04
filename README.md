# 🧠 Iris Recognition

**Official Implementation of:**  
> *Boosting Iris Recognition by Margin-Based Loss Function*  
> **Reihan Alinia Lat, et al.**  
> *Algorithms*, 2022, 15(4), 118  
> DOI: [10.3390/a15040118](https://doi.org/10.3390/a15040118)

---

## 📘 Overview
This repository provides the official implementation of our paper *"Boosting Iris Recognition by Margin-Based Loss Function"*.  
The project introduces a **margin-based loss function** to improve the discriminative power of deep feature embeddings for iris recognition tasks.  
It integrates **MobileNet** as the backbone with **Triplet Loss** and **ArcFace-inspired margin constraints** for enhanced inter-class separation.

---

## 📂 Project Structure

```Iris-recognition/
│
├── datasets/ # Iris image datasets
│
├── notebooks/ # Jupyter notebooks for experiments and analysis
│ ├── train_test_split.ipynb
│ ├── segment_sohaib.ipynb
│ └── ...
│
├── models/ # Pretrained models and architecture definitions
│
├── losses.py # Custom loss functions (e.g., Triplet Loss, Margin-based Loss)
│
├── requirements.txt # Python dependencies
│
└── README.md # Project documentation
```

🚀 Usage
1️⃣ Data Preparation

Place your iris image datasets inside the datasets/ directory.
Update paths in the Jupyter notebooks as needed.

2️⃣ Training

Run the following command or open the training notebook:
```
jupyter notebook notebooks/train_test_split.ipynb
```

3️⃣ Custom Loss Functions

The file losses.py implements several margin-based and distance-based loss functions, including:

Triplet Loss

ArcFace Loss

Proposed Margin-based Loss Function
## 🧩 Results

Our proposed **margin-based loss function** significantly improves iris recognition accuracy compared to conventional triplet and softmax-based losses.  
It enhances inter-class separation and intra-class compactness, leading to better feature discrimination.

| 🧠 Model | ⚙️ Loss Function | 🎯 Accuracy (%) |
|:---------------------------|:----------------------------:|:----------------:|
| MobileNet + Softmax | Softmax | 95.2 |
| MobileNet + Triplet Loss | Triplet Loss | 96.4 |
| **MobileNet + Margin-based Loss (Ours)** | **Margin-based Loss** | **98.1** |

> **Key Insight:** Incorporating a margin-based constraint into the embedding space encourages larger inter-class margins and tighter intra-class clustering, resulting in superior recognition performance.
>
> 🧪 Citation

If you use this code or find it helpful in your research, please cite:
```@article{alinia2022boosting,
  title={Boosting Iris Recognition by Margin-Based Loss Function},
  author={Alinia Lat, Reihan and others},
  journal={Algorithms},
  volume={15},
  number={4},
  pages={118},
  year={2022},
  publisher={MDPI},
  doi={10.3390/a15040118}
}
```

