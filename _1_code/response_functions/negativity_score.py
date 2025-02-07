import pandas as pd
import numpy as np
import os
import torch



device = 'cuda' if torch.cuda.is_available() else 'cpu'


class Negativity_Score:

    def __init__(self, batch_size=32):

        self.model_name = 'siebert/sentiment-roberta-large-english'
        self.batch_size = batch_size

        self.prepare_model()

        return


    def prepare_model(self):

        # Load model directly
        from transformers import AutoTokenizer, AutoModelForSequenceClassification

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name).to(device)

        tokenized_input = self.tokenizer(
            'I hate you', return_tensors='pt', max_length=128, truncation=True
        ).input_ids.to(device)

        print('Negativity: ', self.model(tokenized_input).logits[0].detach().cpu().numpy()[0])

        return


    def get_negativity(self, sentences):

        num_batches = int(len(sentences) / self.batch_size)
        if num_batches * self.batch_size < len(sentences): num_batches += 1

        negativity_scores = []
        for i in range(num_batches):
            print('\rGenerating score on batch: {}/{}'.format(i+1, num_batches), end='')

            try:
                scores = self.model(
                    **self.tokenizer(
                        sentences[i*self.batch_size : min(len(sentences), (i+1)*self.batch_size)],
                        return_tensors='pt', max_length=1000, truncation=True, padding=True
                    ).to(device)
                ).logits.detach().cpu().numpy()[:, 0]

            except:
                scores = []
                for sentence in sentences[i*self.batch_size : min(len(sentences), (i+1)*self.batch_size)]:
                    try:
                        scores.append(
                            self.model(
                                **self.tokenizer(
                                    [sentence],
                                    return_tensors='pt', max_length=1000, truncation=True, padding=True
                                ).to(device)
                            ).logits.detach().cpu().numpy()[0, 0]
                        )
                    except:
                        scores.append(0)

            if i == 0:
                negativity_scores = scores.copy()
            else:
                negativity_scores = np.append(negativity_scores, scores, axis=0)

        return negativity_scores


    def generate_negativity_scores(
        self, ba,
        column_name=None,
        save_col=None,
        save_path=None,
        overwrite=False
    ):
        """
        Input:
        Output:
        """

        if column_name is None:
            column_name = 'feedback'
        if save_col is None:
            save_col = column_name + '_negativity'
        if save_path:
            if not save_path.split('.')[-1] == 'xlsx':
                save_path += '.xlsx'
            print('Going to save file at {} in column {}'.format(save_path, save_col))

            if os.path.isfile(save_path):
                ba_new = pd.read_excel(save_path, engine='openpyxl')
            else:
                ba_new = pd.DataFrame()

        if (save_col not in ba_new.columns) or overwrite:
            feedbacks = ba[column_name].tolist()
            negativity_scores = self.get_negativity(feedbacks)

            if save_path:
                ba_new[save_col] = negativity_scores
                ba_new.to_excel(save_path, index=False)
        else:
            print('The analysis has already been done.')
            negativity_scores = ba_new[save_col].tolist()

        return negativity_scores
    
    