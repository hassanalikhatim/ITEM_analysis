import pandas as pd
import numpy as np



def generate_negativity_scores(
    ba,
    column_name=None,
    save_col=None,
    save_path=None
):
    """
    Input:
    Output:
    """
    
    from transformers import pipeline
    
    if column_name is None:
        column_name = 'feedback'
    if save_col is None:
        save_col = column_name + '_negativity'

    if save_col not in ba.columns.tolist():
        negativity_scores = np.zeros((len(ba))).tolist()
    else:
        negativity_scores = ba[save_col].tolist()

    pipe = pipeline("text-classification")

    feedbacks = ba[column_name].tolist()

    for f, feedback in enumerate(feedbacks):

        if feedback != 0:

            print('\r', (f+1)/len(ba), end="")

            values = pipe(feedback)[0]
            
            if values['label'] == 'NEGATIVE': negativity_score = values['score']
            elif values['label'] == 'POSITIVE': negativity_score = 1 - values['score']
            negativity_scores[f] = negativity_score

            if save_path is not None:
                ba_new = pd.DataFrame(
                    {save_col: negativity_scores}
                )
                ba_new.to_excel( save_path+'.xlsx', index=False)

    return negativity_scores