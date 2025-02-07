import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt



def generate_confusion_matrix(
    all_scores, 
    labels_1, labels_2, 
    name=None,
    normalize=False
):

    processed_scores = np.array(all_scores)
    
    if normalize:
        processed_scores = processed_scores/np.max(processed_scores)

    df_cm = pd.DataFrame(
        processed_scores,
        index = [i for i in labels_1],
        columns = [i for i in labels_2]
    )

    wh_constant = 10/7
    h = 3.5
    plt.figure(figsize = (h*wh_constant, h))
    sn.heatmap(df_cm, annot=True)
    plt.tight_layout()

    if name is not None:
        plt.savefig(name+'.pdf')

    return